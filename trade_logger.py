import csv
import os
from datetime import datetime

# Neo chặt thư mục 'logs' vào cùng thư mục với file code này
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True) # Tự động tạo thư mục logs

TRADE_FILE = os.path.join(LOG_DIR, "trades.csv")

def log_trade(alpha, side, entry_time, exit_time, entry_price, exit_price, pnl, reason):
    """Ghi lại lệnh vừa đóng vào file CSV để cuối tuần xem lại"""
    file_exists = os.path.isfile(TRADE_FILE)
    
    with open(TRADE_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Nếu là file mới tinh, ghi thêm dòng Tiêu đề (Header)
        if not file_exists:
            writer.writerow(['Record Time', 'Alpha Name', 'Side', 'Entry Time', 'Exit Time', 'Entry Price', 'Exit Price', 'Net PnL', 'Exit Reason'])
        
        # Ghi thông tin lệnh vừa đóng
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            alpha, side, entry_time, exit_time, entry_price, exit_price, round(pnl, 2), reason
        ])