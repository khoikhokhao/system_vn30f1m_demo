import pandas as pd
import numpy as np
import datetime as dt
from .base_alpha import BaseAlpha

class Alpha11Gravity(BaseAlpha):
    def __init__(self, name="Alpha11_Gravity", params=None):
        # [QUAN TRỌNG]: Khai báo timeframe=1 để Portfolio Manager biết đường mớm nến 1M
        super().__init__(name, params, timeframe=1)
        
        # --- BỘ THAM SỐ TỪ BACKTEST V1 ---
        if not self.params:
            self.params = {
                # Cấu trúc Khối lượng (Macro)
                'vwap_window': 480,       
                'gravity_limit': 0.0025,  
                
                # Động lượng Phá vỡ (Micro - 1M)
                'escape_vol_window': 10,  
                'vol_spike_ratio': 2.05,  
                'escape_price_roc': 0,    
                
                # Quản trị lệnh (Swing Trade)
                'tp_long': 0.033,         
                'sl_long': 0.01,          
                'tp_short': 0.033,
                'sl_short': 0.012,
                
                'max_hold_bars': 1500,    
            }
        
        # vwap_window = 480, lấy max_lookback = 600 để bộ đệm chạy mượt mà
        self.max_lookback = 1500

    def _is_valid_entry_time(self, current_time: dt.time) -> bool:
        """Tối ưu hóa bộ lọc thời gian Entry: Cấm từ 08:45-09:14 và cấm sau 14:24"""
        if current_time < dt.time(9, 15): return False
        if current_time >= dt.time(14, 25): return False
        return True

    def _is_valid_exit_time(self, current_time: dt.time) -> bool:
        """Cấm chốt lệnh trong ATC hoặc sát ATC (14:25 - 14:45)"""
        if dt.time(14, 25) <= current_time <= dt.time(14, 45): return False
        return True

    def check_entry(self, df: pd.DataFrame):
        """Logic tìm kiếm sự giải phóng khỏi lực hút VWAP"""
        if not self.validate_data(df, self.max_lookback): return

        df_calc = df.tail(self.max_lookback).copy()
        p = self.params
        last_time = df_calc['Date'].iloc[-1].time()
        
        # 1. Lọc thời gian
        if not self._is_valid_entry_time(last_time): return
        
        H = df_calc['High']
        L = df_calc['Low']
        C = df_calc['Close']
        V = df_calc['Volume'].fillna(0)
        
        # 2. Trọng tâm Khối lượng (VWAP)
        typical_price = (H + L + C) / 3
        tpv = typical_price * V
        
        rolling_tpv = tpv.rolling(p['vwap_window']).sum()
        rolling_vol = V.rolling(p['vwap_window']).sum()
        cm_vol = rolling_tpv / (rolling_vol + 1e-9)
        
        # 3. Lực hấp dẫn (Gravity Pull)
        g_pull = np.abs(C - cm_vol) / (cm_vol + 1e-9)
        is_compressed = g_pull < p['gravity_limit']
        
        # 4. Xung lượng thoát ly (Escape Velocity)
        price_roc = C.diff(p['escape_vol_window'])
        vol_5m = V.rolling(p['escape_vol_window']).sum()
        vol_avg_150m = V.rolling(150).mean() * p['escape_vol_window']
        vol_spike = vol_5m / (vol_avg_150m + 1e-9)
        
        # Lấy giá trị của nến cuối cùng và nến áp chót (shift 1)
        curr_C = C.iloc[-1]
        curr_cm_vol = cm_vol.iloc[-1]
        curr_price_roc = price_roc.iloc[-1]
        curr_vol_spike = vol_spike.iloc[-1]
        
        # Trạng thái nén ở nến ngay trước đó
        last_is_compressed = is_compressed.iloc[-2] 

        # 5. Kích hoạt Tín hiệu (Breakaway)
        cond_long = (
            last_is_compressed and 
            (curr_C > curr_cm_vol) and 
            (curr_price_roc > p['escape_price_roc']) and 
            (curr_vol_spike > p['vol_spike_ratio'])
        )
        
        cond_short = (
            last_is_compressed and 
            (curr_C < curr_cm_vol) and 
            (curr_price_roc < -p['escape_price_roc']) and 
            (curr_vol_spike > p['vol_spike_ratio'])
        )
        
        # 6. Khớp lệnh & Tính Absolute TP/SL để Log đẹp
        curr_dt = df_calc['Date'].iloc[-1]
        
        if cond_long and not cond_short:
            tp_val = curr_C * (1 + p['tp_long'])
            sl_val = curr_C * (1 - p['sl_long'])
            self._execute_entry(1, curr_C, curr_dt, tp_val=tp_val, sl_val=sl_val)
            
        elif cond_short and not cond_long:
            tp_val = curr_C * (1 - p['tp_short'])
            sl_val = curr_C * (1 + p['sl_short'])
            self._execute_entry(-1, curr_C, curr_dt, tp_val=tp_val, sl_val=sl_val)

    def check_exit(self, df: pd.DataFrame):
        """Quản lý lệnh: Cắt lỗ, Chốt lời tĩnh, và Giới hạn thời gian gồng"""
        last_bar = df.iloc[-1]
        curr_price = last_bar['Close']
        curr_high = last_bar['High']
        curr_low = last_bar['Low']
        curr_time = last_bar['Date'].time()
        p = self.params
        
        # Bỏ qua giờ cấm thoát lệnh (VD: Sát ATC)
        if not self._is_valid_exit_time(curr_time): return
        
        # A. PHE MUA (LONG EXIT)
        if self.position == 1:
            if curr_low <= self.current_sl:
                self._execute_exit(curr_price, "EXIT_SL")
                return 
            elif curr_high >= self.current_tp:
                self._execute_exit(curr_price, "EXIT_TP")
                return
            elif self.bars_held >= p['max_hold_bars']:
                self._execute_exit(curr_price, "EXIT_MAX_HOLD")
                return
                
        # B. PHE BÁN (SHORT EXIT)
        elif self.position == -1:
            if curr_high >= self.current_sl:
                self._execute_exit(curr_price, "EXIT_SL")
                return
            elif curr_low <= self.current_tp:
                self._execute_exit(curr_price, "EXIT_TP")
                return
            elif self.bars_held >= p['max_hold_bars']:
                self._execute_exit(curr_price, "EXIT_MAX_HOLD")
                return