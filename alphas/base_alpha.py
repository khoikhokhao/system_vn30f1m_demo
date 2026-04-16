from abc import ABC, abstractmethod
import pandas as pd
import logging
from datetime import datetime

# Import 2 công cụ mới từ thư mục gốc
import state_manager
import trade_logger

class BaseAlpha(ABC):
    def __init__(self, name: str, params: dict = None, timeframe: int = 5):
        self.name = name
        self.params = params or {}
        self.timeframe = timeframe
        self.logger = logging.getLogger(self.name)
        
        # --- BỘ NHỚ TRẠNG THÁI MẶC ĐỊNH ---
        self.position = 0          
        self.entry_price = 0.0     
        self.entry_time = None     
        self.bars_held = 0         
        self.cooldown_timer = 0    
        self.current_tp = 0.0      
        self.current_sl = 0.0      
        
        # [MỚI] Biến chuyên dụng để đếm nến gồng (Tách biệt khỏi entry_time kế toán)
        self.hold_anchor_time = None
        
        self.exit_time = None      
        self.cooldown_target = 0   

        # --- KHÔI PHỤC TRÍ NHỚ (NẾU CÓ TRONG Ổ CỨNG) ---
        saved_state = state_manager.load_state(self.name)
        if saved_state:
            self.position = saved_state.get('position', 0)
            self.entry_price = saved_state.get('entry_price', 0.0)
            self.entry_time = saved_state.get('entry_time', None)
            
            # Khôi phục mốc đếm nến (Nếu file cũ chưa có, lấy tạm entry_time)
            self.hold_anchor_time = saved_state.get('hold_anchor_time', self.entry_time)
            
            self.bars_held = saved_state.get('bars_held', 0)
            self.cooldown_timer = saved_state.get('cooldown_timer', 0)
            self.current_tp = saved_state.get('current_tp', 0.0)
            self.current_sl = saved_state.get('current_sl', 0.0)
            
            self.exit_time = saved_state.get('exit_time', None)
            self.cooldown_target = saved_state.get('cooldown_target', 0)
            
            self.load_custom_state(saved_state)
            
            if self.position != 0 or self.cooldown_timer > 0:
                self.logger.info(f"🔄 ĐÃ KHÔI PHỤC TRÍ NHỚ: Đang ôm {self.position} HĐ (Giá vốn: {self.entry_price}) | Đồng hồ Cooldown: {self.cooldown_timer}/{self.cooldown_target}")

    def validate_data(self, df: pd.DataFrame, min_bars: int) -> bool:
        if df is None or df.empty or len(df) < min_bars:
            return False
        return True

    def process_bar(self, df: pd.DataFrame) -> int:
        self.current_bar_time = df['Date'].iloc[-1]

        # 1. BÙ GIỜ TỰ ĐỘNG CHO BARS_HELD (Sử dụng hold_anchor_time thay vì entry_time)
        if self.position != 0 and self.hold_anchor_time:
            anchor_dt = pd.to_datetime(self.hold_anchor_time)
            self.bars_held = len(df[df['Date'] > anchor_dt])

        # 2. BÙ GIỜ TỰ ĐỘNG CHO COOLDOWN
        if self.cooldown_target > 0 and self.exit_time:
            exit_dt = pd.to_datetime(self.exit_time)
            bars_since_exit = len(df[df['Date'] > exit_dt])
            self.cooldown_timer = max(0, self.cooldown_target - bars_since_exit)
            
            if self.cooldown_timer == 0:
                self.cooldown_target = 0
                self.exit_time = None
        
        # 3. CHẶN LOGIC NẾU ĐANG BỊ PHẠT COOLDOWN
        if getattr(self, 'cooldown_timer', 0) > 0:
            self._save_state()
            return 0 

        # 4. XỬ LÝ LOGIC ENTRY/EXIT CHÍNH
        if self.position != 0:
            self.check_exit(df) 
        else:
            self.check_entry(df)

        # 5. AUTO-SAVE
        self._save_state()
        return self.position

    def _save_state(self):
        state_dict = {
            'position': self.position,
            'entry_price': self.entry_price,
            'entry_time': str(self.entry_time) if self.entry_time else None,
            'hold_anchor_time': str(self.hold_anchor_time) if self.hold_anchor_time else None,
            'bars_held': self.bars_held,
            'cooldown_timer': self.cooldown_timer,
            'current_tp': self.current_tp,
            'current_sl': self.current_sl,
            'exit_time': str(self.exit_time) if self.exit_time else None,
            'cooldown_target': self.cooldown_target
        }
        state_dict.update(self.get_custom_state()) 
        
        import state_manager
        state_manager.save_state_to_memory(self.name, state_dict)

    def _execute_entry(self, direction: int, price: float, time, tp_val: float = None, sl_val: float = None):
        self.position = direction
        self.entry_price = price
        self.entry_time = time
        self.hold_anchor_time = time # [MỚI] Neo thời gian đếm nến bằng đúng giờ vào lệnh
        self.bars_held = 0
        self.current_tp = tp_val
        self.current_sl = sl_val
        self.exit_time = None      
        self.cooldown_target = 0    
        
        side_str = "LONG" if direction == 1 else "SHORT"
        self.logger.info(f"🟢 VÀO LỆNH {side_str} tại {price} | TP: {tp_val}, SL: {sl_val}")

    def _execute_exit(self, price: float, reason: str, cooldown_bars: int = 0):
        side_str = "LONG" if self.position == 1 else "SHORT"
        pnl = (price - self.entry_price) * self.position
        self.logger.info(f"🔴 ĐÓNG LỆNH {side_str} ({reason}) tại {price} | PnL: {pnl:.2f} | Bắt đầu Cooldown: {cooldown_bars} nến")
        
        trade_logger.log_trade(
            alpha=self.name,
            side=side_str,
            entry_time=self.entry_time,
            exit_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            entry_price=self.entry_price,
            exit_price=price,
            pnl=pnl,
            reason=reason
        )

        self.exit_time = getattr(self, 'current_bar_time', datetime.now())
        self.cooldown_target = cooldown_bars

        self.position = 0
        self.entry_price = 0.0
        self.hold_anchor_time = None
        self.bars_held = 0
        self.current_tp = 0.0
        self.current_sl = 0.0
        self.cooldown_timer = cooldown_bars

    def get_custom_state(self) -> dict: return {}
    def load_custom_state(self, state_dict: dict): pass

    @abstractmethod
    def check_entry(self, df: pd.DataFrame): pass

    @abstractmethod
    def check_exit(self, df: pd.DataFrame): pass