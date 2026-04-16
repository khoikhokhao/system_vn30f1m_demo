import time
import os
import logging
import traceback
from datetime import datetime
import datetime as dt
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv
import pytz

# Khai báo các Module Live Trading
from dnse_live_client import DNSELiveClient
from execution_engine import ExecutionEngine
from portfolio_manager import PortfolioManager

# [NHỚ THÊM Alpha CỦA BÁC VÀO ĐÂY]
# Để an toàn cho lệnh chạy thử, bác TẠM THỜI chỉ gọi 1 con Alpha ra thôi nhé.
from alphas import Alpha3BVM,Alpha11Gravity,Alpha48TPT,Alpha73LFI


# ==========================================================
# 1. CẤU HÌNH LOGGING 
# ==========================================================
os.makedirs("logs", exist_ok=True) 
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = TimedRotatingFileHandler("logs/bot_live.log", when="midnight", interval=1, backupCount=30, encoding="utf-8")
file_handler.setFormatter(log_formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
logging.basicConfig(level=logging.INFO, handlers=[file_handler, stream_handler])
logger = logging.getLogger("MAIN_LIVE")

VN_TZ = pytz.timezone('Asia/Ho_Chi_Minh')

def is_market_open(now: datetime) -> bool:
    if now.weekday() >= 5: return False
    t = now.time()
    morning_session = dt.time(8, 45) <= t <= dt.time(11, 35)
    afternoon_session = dt.time(12, 55) <= t <= dt.time(15, 0)
    return morning_session or afternoon_session

def main():
    load_dotenv()
    
    # -----------------------------------------------------------------
    # BƯỚC 1: XÁC THỰC DNSE LIVE CLIENT (YÊU CẦU OTP)
    # -----------------------------------------------------------------
    logger.info("Đang khởi tạo Liên Lạc Viên DNSE...")
    client = DNSELiveClient(
        api_key=os.getenv("DNSE_API_KEY"),
        api_secret=os.getenv("DNSE_API_SECRET"),
        account_no=os.getenv("accountNo")
    )
    
    otp_success = False
    while not otp_success:
        smart_otp = input("\n🔐 YÊU CẦU BẢO MẬT: Bác mở App DNSE lấy 6 số Smart OTP nhập vào đây: ").strip()
        if not smart_otp: continue
        otp_success = client.activate_trading_token(smart_otp)
        if not otp_success:
            logger.error("❌ Nhập sai OTP hoặc đã quá hạn 30s. Vui lòng lấy lại mã và nhập lại!")
    if not client.check_derivative_account_status():
        logger.critical("🛑 BOT TỰ HỦY: Tiểu khoản của bác không được phép đánh phái sinh. Vui lòng kiểm tra lại file cấu hình!")
        return  # Lệnh return này sẽ kết thúc hoàn toàn chương trình main()

    # -----------------------------------------------------------------
    # BƯỚC 2: KHỞI TẠO TAY SÚNG BẮN TỈA & CẦU DAO AN TOÀN
    # -----------------------------------------------------------------
    # SIÊU THAM SỐ: Chỉnh MAX_NET_POSITION = 1 để vừa vốn 38 triệu.
    engine = ExecutionEngine(
        live_client=client, 
        max_net_position=1,   # Tối đa ôm 1 HĐ
        max_order_qty=2       # Tối đa bắn 1 HĐ/lần
    )

    # -----------------------------------------------------------------
    # BƯỚC 3: LẮP RÁP PORTFOLIO MANAGER
    # -----------------------------------------------------------------
    # TẠM THỜI CHẠY 1 ALPHA ĐỂ TEST LOGIC
    CURRENT_TRADE_SYMBOL = "41I1G4000" 
    
    my_alphas = [Alpha11Gravity(),Alpha48TPT(),Alpha73LFI() ]
    
    
    # Nạp Engine vào Portfolio
    # Nạp Engine và Mã giao dịch thật vào Portfolio
    portfolio = PortfolioManager(
        execution_engine=engine, 
        alphas=my_alphas,
        trade_symbol=CURRENT_TRADE_SYMBOL  # <--- BƠM MÃ VÀO ĐÂY
    )

    logger.info("==========================================================")
    logger.info("🚀 HỆ THỐNG LIVE ĐÃ VÀO VỊ TRÍ CHIẾN ĐẤU (DRY RUN ON) 🚀")
    logger.info("==========================================================")

    # -----------------------------------------------------------------
    # BƯỚC 4: VÒNG LẶP TIMING THỰC CHIẾN
    # -----------------------------------------------------------------
    last_processed_minute = None 

    while True:
        try:
            now = datetime.now(VN_TZ)
            
            # CHẾ ĐỘ NGỦ SÂU
            if not is_market_open(now):
                time.sleep(60) 
                continue
                
            current_minute = now.minute
            current_second = now.second
            
            # Bắn tín hiệu vào giây thứ 55
            is_atc_minute = (now.hour == 14 and current_minute == 45)
            trigger_sec = 5 if is_atc_minute else 55
            
            if current_second >= trigger_sec and current_minute != last_processed_minute:
                
                time_str = now.strftime('%H:%M')
                logger.info(f"\n========== NHỊP QUÉT ĐỘNG ({time_str}) ==========")
                
                # Gọi API kéo nến 1M đầy đủ
                df_1m = client.get_market_data_for_alphas(limit=30000)
                
                if not df_1m.empty:
                    # Giao việc cho Portfolio nhào nặn
                    portfolio.process_new_bar(df_1m, now)
                    last_processed_minute = current_minute 
                    logger.info("Xử lý xong. Hệ thống ngủ đông chờ nhịp tiếp theo...")
                else:
                    logger.warning("Không lấy được dữ liệu API. Đang retry lại ngay lập tức...")
                    time.sleep(2) 
            
        except Exception as e:
            logger.error(f"LỖI NGHIÊM TRỌNG TRONG VÒNG LẶP MAIN: {e}")
            traceback.print_exc()
            logger.info("Bot đang tự động hồi sinh sau 5 giây...")
            time.sleep(5)
            
        time.sleep(0.5)

if __name__ == "__main__":
    main()