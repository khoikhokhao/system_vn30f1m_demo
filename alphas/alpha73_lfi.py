import pandas as pd
import numpy as np
import datetime as dt
from .base_alpha import BaseAlpha

class Alpha73LFI(BaseAlpha):
    def __init__(self, name="Alpha73_LFI", params=None):
        # [QUAN TRỌNG]: Chạy trên nến 3 Phút
        super().__init__(name, params, timeframe=3)
        
        if not self.params:
            self.params = {
                # Cấu trúc LFI
                'vol_ma_window': 30,     
                'z_window': 70,          
                'z_thresh': -1,        
                'price_window': 40,      
                
                # Quản trị lệnh (RR 1:1)
                'tp': 0.03,             
                'sl': 0.015,             
                'max_hold': 400,         
            }
        
        # Max lookback cần đủ cho: z_window (80). 
        # Ta lấy 120 nến 3M để đảm bảo bộ đệm an toàn tuyệt đối.
        self.max_lookback = 500

    def _is_valid_entry_time(self, current_time: dt.time) -> bool:
        """Bộ lọc thời gian nhiễu (Khớp 100% logic Backtest)"""
        # Cấm vào trước 09:15
        if current_time < dt.time(9, 15): return False
        
        # Cấm toàn bộ từ 14:27 trở đi (Chặn mọi nến 3M sau giờ này)
        if current_time >= dt.time(14, 27): return False
        
        return True

    def _is_valid_exit_time(self, current_time: dt.time) -> bool:
        """Cấm chốt lệnh trong phiên ATC để gồng qua đêm"""
        if current_time == dt.time(14, 30) or current_time == dt.time(14, 45): return False
        return True

    def check_entry(self, df: pd.DataFrame):
        """Logic Liquidity Friction Index (LFI)"""
        if not self.validate_data(df, self.max_lookback): return

        df_calc = df.copy()
        
        # Lọc data trong giờ hành chính để loại bỏ nhiễu
        df_calc['time'] = df_calc['Date'].dt.time
        df_calc = df_calc[(df_calc['time'] >= dt.time(9, 0)) & (df_calc['time'] <= dt.time(14, 45))]
        
        df_calc = df_calc.tail(self.max_lookback).copy()
        p = self.params
        last_time = df_calc['time'].iloc[-1]
        
        if not self._is_valid_entry_time(last_time): return
        
        C = df_calc['Close']
        O = df_calc['Open']
        H = df_calc['High']
        L = df_calc['Low']
        V = df_calc['Volume'].fillna(0)
        
        # --- 1. Volume MA ---
        vol_ma = V.rolling(p['vol_ma_window']).mean()
        
        # --- 2. Volume Efficiency (VE) ---
        body = (C - O).abs()
        spread = H - L + 1e-9
        
        ve = (body / spread) * (V / (vol_ma + 1e-9))
        ve = ve.clip(0, 10)
        
        # --- 3. VE Z-Score ---
        ve_mean = ve.rolling(p['z_window']).mean()
        ve_std = ve.rolling(p['z_window']).std()
        
        z_ve = (ve - ve_mean) / (ve_std + 1e-9)
        
        # --- 4. Xác định giá min/max ---
        min_price = C.rolling(p['price_window']).min()
        max_price = C.rolling(p['price_window']).max()
        
        # Trích xuất dữ liệu nến cuối cùng
        curr_z_ve = z_ve.iloc[-1]
        curr_min_price = min_price.iloc[-1]
        curr_max_price = max_price.iloc[-1]
        curr_C = C.iloc[-1]
        curr_dt = df_calc['Date'].iloc[-1]

        # --- 5. Kích hoạt Tín hiệu (Bắt đỉnh/Đáy khi ma sát cao) ---
        cond_long = (curr_z_ve < p['z_thresh']) and (curr_C >= curr_max_price)
        cond_short = (curr_z_ve < p['z_thresh']) and (curr_C <= curr_min_price)

        # --- 6. Khớp lệnh ---
        if cond_long and not cond_short:
            tp_val = curr_C * (1 + p['tp'])
            sl_val = curr_C * (1 - p['sl'])
            self._execute_entry(1, curr_C, curr_dt, tp_val=tp_val, sl_val=sl_val)
            
        elif cond_short and not cond_long:
            tp_val = curr_C * (1 - p['tp'])
            sl_val = curr_C * (1 + p['sl'])
            self._execute_entry(-1, curr_C, curr_dt, tp_val=tp_val, sl_val=sl_val)

    def check_exit(self, df: pd.DataFrame):
        """Quản lý lệnh: Cắt lỗ/Chốt lời tĩnh và Giới hạn thời gian gồng"""
        last_bar = df.iloc[-1]
        curr_price = last_bar['Close']
        curr_high = last_bar['High']
        curr_low = last_bar['Low']
        curr_time = last_bar['Date'].time()
        p = self.params
        
        if not self._is_valid_exit_time(curr_time): return
        
        if self.position == 1:
            if curr_low <= self.current_sl:
                self._execute_exit(curr_price, "EXIT_SL")
                return 
            elif curr_high >= self.current_tp:
                self._execute_exit(curr_price, "EXIT_TP")
                return
            elif self.bars_held >= p['max_hold']:
                self._execute_exit(curr_price, "EXIT_MAX_HOLD")
                return
                
        elif self.position == -1:
            if curr_high >= self.current_sl:
                self._execute_exit(curr_price, "EXIT_SL")
                return
            elif curr_low <= self.current_tp:
                self._execute_exit(curr_price, "EXIT_TP")
                return
            elif self.bars_held >= p['max_hold']:
                self._execute_exit(curr_price, "EXIT_MAX_HOLD")
                return