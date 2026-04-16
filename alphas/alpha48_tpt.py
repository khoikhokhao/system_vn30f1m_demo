import pandas as pd
import numpy as np
import datetime as dt
from .base_alpha import BaseAlpha

class Alpha48TPT(BaseAlpha):
    def __init__(self, name="Alpha48_TPT", params=None):
        # [QUAN TRỌNG]: Chạy trên nến 3 Phút
        super().__init__(name, params, timeframe=3)
        
        if not self.params:
            self.params = {
                # Cấu trúc Entropy Lõi
                'tpt_window': 35,        
                'bins': 10,               
                
                # Môi trường Động (Adaptive Entropy Z-Score)
                'z_window': 120,          
                'z_thresh': -2.5,        
                
                # Quản trị lệnh (Let profits run - TP 15%)
                'tp': 0.07,              
                'sl': 0.017,              
                'max_hold': 800,        
            }
        
        # Max lookback cần đủ cho: tpt_window (30) -> delta_H (1) -> z_window (70)
        # Tổng cộng = 101. Lấy 150 nến 3M làm bộ đệm an toàn.
        self.max_lookback = 800

    def _is_valid_entry_time(self, current_time: dt.time) -> bool:
        """Bộ lọc thời gian nhiễu (Khớp 100% logic Backtest)"""
        invalid_times = [
            dt.time(14, 0), dt.time(14, 3), dt.time(14, 6), dt.time(14, 9),
            dt.time(14, 12), dt.time(14, 15), dt.time(14, 18), 
            dt.time(14, 21), dt.time(14, 24), dt.time(14, 27), 
            dt.time(14, 30), dt.time(14, 45)
        ]
        if current_time in invalid_times: return False
        
        # Logic valid_time: Không vào trước 9:15
        if current_time < dt.time(9, 15): return False
        
        # Cấm nốt toàn bộ từ 14:30 trở đi
        if current_time > dt.time(14, 30): return False
        
        return True

    def _is_valid_exit_time(self, current_time: dt.time) -> bool:
        """Cấm chốt lệnh trong phiên ATC để gồng qua đêm"""
        if current_time == dt.time(14, 30) or current_time == dt.time(14, 45): return False
        return True

    @staticmethod
    def calc_shannon_entropy(x, num_bins):
        """Hàm nội bộ tính Shannon Entropy được tối ưu cho rolling.apply"""
        x = x[~np.isnan(x)]
        if len(x) < 2: return 0.0
        hist, _ = np.histogram(x, bins=num_bins, density=False)
        p = hist / np.sum(hist)
        p = p[p > 0] # Bỏ các bin có xác suất = 0 để tránh lỗi log(0)
        return -np.sum(p * np.log(p))

    def check_entry(self, df: pd.DataFrame):
        """Logic Thermodynamic Phase Transition (TPT)"""
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
        w = p['tpt_window']
        z_w = p['z_window']
        bins = p['bins']
        
        # --- 1. Tính toán chuỗi Returns nội hàm ---
        rets = C.diff()
        
        # --- 2. Đo lường Shannon Entropy ---
        entropy = rets.rolling(w).apply(lambda x: self.calc_shannon_entropy(x, bins), raw=True)
        
        # --- 3. Tính Gia tốc sụp đổ (Delta H) ---
        delta_H = entropy.diff(1)
        
        # --- 4. Chuẩn hóa sự sụp đổ (Adaptive Z-Score) ---
        dh_mean = delta_H.rolling(z_w).mean()
        dh_std = delta_H.rolling(z_w).std()
        
        z_delta_H = (delta_H - dh_mean) / (dh_std + 1e-9)
        
        # --- 5. Vector Hướng đi ---
        direction = C - C.shift(w)
        
        # Trích xuất dữ liệu nến cuối
        curr_z_H = z_delta_H.iloc[-1]
        curr_dir = direction.iloc[-1]
        curr_C = C.iloc[-1]
        curr_dt = df_calc['Date'].iloc[-1]

        # --- 6. Kích hoạt Tín hiệu ---
        is_collapse = curr_z_H < p['z_thresh']
        
        cond_long = is_collapse and (curr_dir > 0)
        cond_short = is_collapse and (curr_dir < 0)

        # --- 7. Khớp lệnh ---
        if cond_long and not cond_short:
            tp_val = curr_C * (1 + p['tp'])
            sl_val = curr_C * (1 - p['sl'])
            self._execute_entry(1, curr_C, curr_dt, tp_val=tp_val, sl_val=sl_val)
            
        elif cond_short and not cond_long:
            tp_val = curr_C * (1 - p['tp'])
            sl_val = curr_C * (1 + p['sl'])
            self._execute_entry(-1, curr_C, curr_dt, tp_val=tp_val, sl_val=sl_val)

    def check_exit(self, df: pd.DataFrame):
        """Quản lý lệnh: Cắt lỗ tĩnh, Thả rông chốt lời (15%) và Giới hạn thời gian gồng"""
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