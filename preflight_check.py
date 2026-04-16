import os
import json
from dotenv import load_dotenv
from dnse_live_client import DNSELiveClient

def run_preflight_check():
    print("="*70)
    print("🚁 BẮT ĐẦU KIỂM TRA SỨC KHỎE TÀI KHOẢN (PRE-FLIGHT CHECK) 🚁")
    print("="*70)

    # Load biến môi trường
    load_dotenv()
    api_key = os.getenv("DNSE_API_KEY")
    api_secret = os.getenv("DNSE_API_SECRET")
    account_no = os.getenv("accountNo")

    if not all([api_key, api_secret, account_no]):
        print("❌ LỖI: Chưa cấu hình đủ DNSE_API_KEY, DNSE_API_SECRET hoặc accountNo trong file .env!")
        return

    # Khởi tạo Client (Không cần nhập OTP cho các thao tác check thông tin)
    client = DNSELiveClient(api_key, api_secret, account_no)

    # ---------------------------------------------------------
    # 1. KIỂM TRA QUYỀN PHÁI SINH
    # ---------------------------------------------------------
    print("\n[1/4] Kiểm tra Quyền giao dịch Phái sinh...")
    is_valid = client.check_derivative_account_status()
    if not is_valid:
        print("❌ THẤT BẠI: Tài khoản không có quyền giao dịch phái sinh hoặc bị khóa.")
        return
    print("  -> Trạng thái: OK")

    # ---------------------------------------------------------
    # 2. KIỂM TRA TÀI SẢN (SỐ DƯ CỌC)
    # ---------------------------------------------------------
    print("\n[2/4] Kiểm tra Tài sản và Tiền cọc (Ký quỹ)...")
    status, body = client.client.get_balances(account_no=account_no, dry_run=False)
    
    remain_secure = 0
    if status == 200:
        if isinstance(body, str):
            body = json.loads(body)
        
        deriv_balance = body.get("derivative", {})
        remain_secure = deriv_balance.get("remainSecure", 0)
        used_secure = deriv_balance.get("usedSecure", 0)
        pending_dw = deriv_balance.get("pendingDepositWithdraw", 0)
        
        print(f"  💰 Tiền cọc CÒN LẠI (Sẵn sàng mua bán): {remain_secure:,.0f} VNĐ")
        print(f"  🔒 Tiền cọc đang sử dụng (Ôm vị thế):  {used_secure:,.0f} VNĐ")
        print(f"  ⏳ Tiền nộp/rút đang chờ xử lý:       {pending_dw:,.0f} VNĐ")
    else:
        print(f"❌ Lỗi lấy thông tin tài sản: {body}")
        return

    # ---------------------------------------------------------
    # 3. LẤY TỶ LỆ KÝ QUỸ (GÓI VAY TỐI ƯU)
    # ---------------------------------------------------------
    print("\n[3/4] Tìm kiếm Gói vay (Margin) tối ưu nhất...")
    symbol = "41I1G4000"
    initial_rate = 1.0
    
    status, body = client.client.get_loan_packages(account_no=account_no, market_type="DERIVATIVE", symbol=symbol, dry_run=False)
    if status == 200:
        if isinstance(body, str):
            body = json.loads(body)
        
        packages = body.get('loanPackages', [])
        if packages:
            best_pkg = min(packages, key=lambda x: x.get('initialRate', 1.0))
            initial_rate = best_pkg.get('initialRate', 1.0)
            
            print(f"  ✅ Gói tối ưu nhất: {best_pkg.get('name')} (ID: {best_pkg.get('id')})")
            print(f"  📊 Tỷ lệ Ký quỹ yêu cầu (Initial Rate): {initial_rate * 100:.2f}%")
            print(f"  ⚠️ Tỷ lệ Force Sell (Liquid Rate):    {best_pkg.get('liquidRate', 0) * 100:.2f}%")
        else:
            print("❌ Không tìm thấy gói vay nào trên hệ thống!")
            return
    else:
        print(f"❌ Lỗi lấy thông tin gói vay: {body}")
        return

    # ---------------------------------------------------------
    # 4. TÍNH TOÁN SỨC MUA THỰC TẾ
    # ---------------------------------------------------------
    print("\n[4/4] Tính toán Sức mua thực tế...")
    print("  Đang kéo giá VN30F1M cuối cùng để ước tính...")
    
    df_candles = client.get_historical_candles("VN30F1M", resolution=1, limit=1)
    if not df_candles.empty:
        last_price = df_candles['Close'].iloc[-1]
        print(f"  📈 Giá VN30F1M tham chiếu: {last_price:,.1f} điểm")
        
        # Công thức phái sinh: Ký quỹ = Giá * Hệ số nhân (100,000) * Tỷ lệ ký quỹ
        margin_per_contract = last_price * 100000 * initial_rate
        
        max_contracts = int(remain_secure // margin_per_contract)
        
        print(f"  💸 Ký quỹ yêu cầu cho 1 Hợp đồng:  {margin_per_contract:,.0f} VNĐ")
        print(f"  🚀 SỨC MUA TỐI ĐA (MAX CONTRACTS): {max_contracts} Hợp đồng")
        
        if max_contracts >= 1:
            print("\n🎉 KẾT LUẬN: TÀI KHOẢN ĐÃ SẴN SÀNG 100% ĐỂ ĐÁNH LỚN! 🎉")
        else:
            shortfall = margin_per_contract - remain_secure
            print(f"\n⚠️ CẢNH BÁO: Số dư cọc của bác KHÔNG ĐỦ để đánh 1 Hợp đồng!")
            print(f"   -> Bác cần nộp thêm tối thiểu: {shortfall:,.0f} VNĐ vào đuôi Phái sinh.")
    else:
        print("  ❌ Không lấy được giá hiện tại. Bác kiểm tra lại mạng nhé.")

if __name__ == "__main__":
    run_preflight_check()