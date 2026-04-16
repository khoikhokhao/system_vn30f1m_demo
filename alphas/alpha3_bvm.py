import pandas as pd
import numpy as np
import datetime as dt
from .base_alpha import BaseAlpha

class Alpha3BVM(BaseAlpha):
    # Cho phép truyền params từ bên ngoài vào (phục vụ WFO sau này)
    def __init__(self, name="Alpha3_BVM", params=None):
        # Khai báo rõ timeframe=5 để đồng bộ hệ thống
        super().__init__(name, params, timeframe=5)
        
        # Chỉ nạp tham số mặc định nếu không có params truyền từ bên ngoài
        if not self.params:
            self.params = {
                # Tính năng cốt lõi
                'z_window': 30,          
                'atr_short': 13,         
                'atr_long': 80,          
                'basis_trend_window': 70,
                'corr_window': 10,       
                
                # Lọc nhiễu
                'min_vol_ratio': 1.1,   
                'min_atr_value': 1.25,  
                'min_corr': 0.2,         
                'price_breakout_window': 6,
                'signal_persistence': 2, 
                
                # Cấu hình Điểm vào
                'entry_threshold_long': 1.5, 
                'entry_threshold_short': 1.8,
                
                # Cấu hình Chốt lời / Cắt lỗ cứng (Fixed)
                'tp_long': 0.03,             
                'sl_long': 0.008,            
                'tp_short': 0.025,           
                'sl_short': 0.009,           
                'max_hold_bars': 250,        
                
                # Bộ lọc Thời gian
                'skip_entry_times': [dt.time(14,45), dt.time(14,30), dt.time(14,25), 
                                     dt.time(14,10), dt.time(14,15), dt.time(14,5), dt.time(14,0)],
                'skip_exit_times':  [dt.time(14,45), dt.time(14,30), dt.time(14,25)]
            }
        
        # Tham số dài nhất là atr_long = 80. Lấy 150 để đảm bảo dư dả tính toán
        self.max_lookback = 350

    def check_entry(self, df: pd.DataFrame):
        """Logic tìm kiếm cú nổ (Breakout Volatility Momentum)"""
        if not self.validate_data(df, self.max_lookback): return
        if 'vn30_close' not in df.columns: return

        df_calc = df.tail(self.max_lookback).copy()
        p = self.params
        last_time = df_calc['Date'].iloc[-1].time()
        
        if last_time in p['skip_entry_times']: return
        
        H, L, C = df_calc['High'], df_calc['Low'], df_calc['Close']
        
        # 1. Volatility Metrics
        prevC = C.shift(1)
        tr = pd.concat([(H-L).abs(), (H-prevC).abs(), (L-prevC).abs()], axis=1).max(axis=1)
        atr_short = tr.rolling(p['atr_short']).mean()
        atr_long = tr.rolling(p['atr_long']).mean()
        vol_ratio = atr_short / atr_long
        
        # 2. Basis Metrics
        basis = C - df_calc['vn30_close']
        basis = basis.fillna(0)
        basis_mean = basis.rolling(p['z_window']).mean()
        basis_std = basis.rolling(p['z_window']).std()
        z_basis = (basis - basis_mean) / basis_std
        basis_trend = basis.rolling(p['basis_trend_window']).mean()
        
        # 3. Price Breakout & Correlation
        donchian_high = H.rolling(p['price_breakout_window']).max().shift(1)
        donchian_low = L.rolling(p['price_breakout_window']).min().shift(1)
        synchro_score = C.rolling(p['corr_window']).corr(basis).fillna(0)
        
        # 4. BVM Score
        bvm_score = z_basis * (vol_ratio ** 2)
        
        # 5. Lọc Tín Hiệu (Signal Filter)
        common_filter = (vol_ratio > p['min_vol_ratio']) & \
                        (atr_short > p['min_atr_value']) & \
                        (synchro_score > p['min_corr'])
        
        raw_long = (bvm_score > p['entry_threshold_long']) & common_filter & \
                   (basis > basis_trend) & (C > donchian_high)
                   
        raw_short = (bvm_score < -p['entry_threshold_short']) & common_filter & \
                    (basis < basis_trend) & (C < donchian_low)
        
        # 6. Persistence Check (Bắt buộc duy trì 2 nến) -> Ép kiểu int để tránh lỗi Pandas
        sig_long = raw_long.astype(int).rolling(p['signal_persistence']).min() == 1
        sig_short = raw_short.astype(int).rolling(p['signal_persistence']).min() == 1
        
        
        # 7. Khớp Tín hiệu
        if sig_long.iloc[-1] and not sig_short.iloc[-1]:
            # Tính giá TP/SL tuyệt đối cho Long
            tp_absolute = C.iloc[-1] * (1 + p['tp_long'])
            sl_absolute = C.iloc[-1] * (1 - p['sl_long'])
            self._execute_entry(1, C.iloc[-1], df_calc['Date'].iloc[-1], tp_val=tp_absolute, sl_val=sl_absolute)
            
        elif sig_short.iloc[-1] and not sig_long.iloc[-1]:
            # Tính giá TP/SL tuyệt đối cho Short
            tp_absolute = C.iloc[-1] * (1 - p['tp_short'])
            sl_absolute = C.iloc[-1] * (1 + p['sl_short'])
            self._execute_entry(-1, C.iloc[-1], df_calc['Date'].iloc[-1], tp_val=tp_absolute, sl_val=sl_absolute)

    def check_exit(self, df: pd.DataFrame):
        """Thoát lệnh bằng Fixed TP/SL và Time Stop"""
        last_bar = df.iloc[-1]
        curr_price = last_bar['Close']
        curr_high = last_bar['High']
        curr_low = last_bar['Low']
        curr_time = last_bar['Date'].time()
        p = self.params
        
        if curr_time in p['skip_exit_times']: return
        
        # A. PHE MUA (LONG EXIT)
        if self.position == 1:
            sl_price = self.entry_price * (1 - p['sl_long'])
            tp_price = self.entry_price * (1 + p['tp_long'])
            
            if curr_low <= sl_price:
                self._execute_exit(curr_price, "EXIT_SL")
            elif curr_high >= tp_price:
                self._execute_exit(curr_price, "EXIT_TP")
            elif self.bars_held >= p['max_hold_bars']:
                self._execute_exit(curr_price, "EXIT_MAX_HOLD")
                
        # B. PHE BÁN (SHORT EXIT)
        elif self.position == -1:
            sl_price = self.entry_price * (1 + p['sl_short'])
            tp_price = self.entry_price * (1 - p['tp_short'])
            
            if curr_high >= sl_price:
                self._execute_exit(curr_price, "EXIT_SL")
            elif curr_low <= tp_price:
                self._execute_exit(curr_price, "EXIT_TP")
            elif self.bars_held >= p['max_hold_bars']:
                self._execute_exit(curr_price, "EXIT_MAX_HOLD")