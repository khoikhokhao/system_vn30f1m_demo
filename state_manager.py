import json
import os
import logging

# Neo chặt thư mục gốc
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, "portfolio_states.json")

logger = logging.getLogger("STATE_MANAGER")

# TRÍ NHỚ RAM (In-memory Cache)
_global_state = {}

def load_all_states():
    """Tải toàn bộ trí nhớ của 100 Alpha từ ổ cứng lên RAM lúc khởi động"""
    global _global_state
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                _global_state = json.load(f)
            logger.info("✅ Đã nạp thành công dữ liệu Portfolio State từ ổ cứng.")
        except json.JSONDecodeError:
            logger.error("❌ File State bị lỗi định dạng. Bắt đầu với trí nhớ trống.")
            _global_state = {}
    return _global_state

def load_state(alpha_name: str) -> dict:
    """Alpha gọi hàm này để lấy trí nhớ của riêng nó từ RAM"""
    global _global_state
    if not _global_state:  # Lần gọi đầu tiên sẽ kích hoạt tải file
        load_all_states()
    return _global_state.get(alpha_name, None)

def save_state_to_memory(alpha_name: str, state_dict: dict):
    """Alpha gọi hàm này sau mỗi nến: CHỈ LƯU VÀO RAM, KHÔNG GHI Ổ CỨNG"""
    global _global_state
    _global_state[alpha_name] = state_dict

def flush_to_disk():
    """Hàm này chỉ được gọi 1 LẦN DUY NHẤT sau khi cả 100 Alpha đã chạy xong 1 nến"""
    global _global_state
    if not _global_state:
        return
        
    # [CƠ CHẾ ATOMIC WRITE]: Ghi ra file tạm, sau đó đổi tên ghi đè file chính.
    # Đảm bảo chống corrupt file 100% nếu crash giữa chừng.
    temp_file = STATE_FILE + ".tmp"
    try:
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(_global_state, f, default=str, indent=4)
        
        # Hàm replace ghi đè nguyên tử trên hệ điều hành
        os.replace(temp_file, STATE_FILE)
    except Exception as e:
        logger.error(f"❌ Lỗi khi xả State xuống ổ cứng: {e}")