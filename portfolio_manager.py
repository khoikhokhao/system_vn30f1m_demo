import pandas as pd
import logging
import datetime as dt

class PortfolioManager:
    def __init__(self, execution_engine, alphas: list, trade_symbol: str, exp_path: str = r"D:\tailieu\expiration_date.csv"):
        self.engine = execution_engine 
        self.logger = logging.getLogger("PortfolioManager")
        self.alphas = alphas
        self.trade_symbol = trade_symbol
        self.required_timeframes = sorted(list(set([getattr(alpha, 'timeframe', 5) for alpha in self.alphas])))
        
        self.virtual_position = sum([getattr(alpha, 'position', 0) for alpha in self.alphas])
        self.logger.info(f"Khôi phục vị thế Ảo từ trí nhớ Alphas: {self.virtual_position} HĐ")
        
        # ... (Phần còn lại của __init__ giữ nguyên) ...

        # KHÔI PHỤC LẠI ĐOẠN ĐỌC FILE ĐÁO HẠN BỊ THIẾU
        try:
            exp_df = pd.read_csv(exp_path)
            date_col = next((c for c in exp_df.columns if "date" in c.lower() or "exp" in c.lower()), exp_df.columns[0])
            self.exp_set = set(pd.to_datetime(exp_df[date_col]).dt.date)
            self.logger.info(f"📅 Đã nạp thành công {len(self.exp_set)} ngày đáo hạn từ {exp_path}")
        except Exception as e:
            self.logger.error(f"❌ Lỗi đọc file đáo hạn {exp_path}: {e}")
            self.exp_set = set()

    def _resample_data(self, df: pd.DataFrame, sample_duration: int, type_data: str = "Min") -> pd.DataFrame:
        if sample_duration == 1:
            return df.copy() 
            
        df = df.copy()
        df['Date'] = pd.to_datetime(df['Date'])
        
        ohlc_dict = {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'}
        
        rule = f"{sample_duration}{type_data}"
        
        # [VÁ LỖI CỐT LÕI SỐ 1]: Ép Pandas neo vào 00:00:00 để nến 3M luôn là 00, 03, 06...
        df_resampled = pd.DataFrame(df.resample(rule, on='Date', label='left', origin='start_day').apply(ohlc_dict).dropna()).reset_index()
        return df_resampled

    def process_new_bar(self, df_1m: pd.DataFrame, current_datetime: dt.datetime):
        if df_1m.empty: return
            
        current_price = df_1m['Close'].iloc[-1]
        last_dt = pd.to_datetime(df_1m['Date'].iloc[-1]) if 'Date' in df_1m.columns else pd.to_datetime(df_1m.index[-1])
        curr_date = last_dt.date()
        curr_time = last_dt.time()
        
        current_minute = current_datetime.minute
        active_timeframes = []
        is_atc = (current_datetime.hour == 14 and current_minute == 45)
        
        for tf in self.required_timeframes:
            # [VÁ LỖI CỐT LÕI SỐ 2]: Đợi nến đóng hoàn toàn bằng (minute + 1)
            if is_atc or ((current_minute + 1) % tf == 0):
                active_timeframes.append(tf)

        if curr_date in self.exp_set and curr_time >= dt.time(14, 29):
            self.logger.warning(f"🚨 [ĐÁO HẠN] Đã đến {curr_time}. Kích hoạt CƯỠNG CHẾ ĐÓNG toàn bộ vị thế!")
            any_open = False
            for alpha in self.alphas:
                if getattr(alpha, 'position', 0) != 0:
                    alpha._execute_exit(price=current_price, reason="EXPIRATION_FORCE_EXIT", cooldown_bars=30)
                    any_open = True
            if any_open:
                self.logger.info("-> Đã reset trí nhớ tất cả Alpha. Bắn lệnh Clear ra sàn.")
                self.sync_with_broker(target_net_pos=0, current_price=current_price)
            else:
                self.logger.info("-> Không có vị thế nào đang mở. An toàn nghỉ ngơi.")
            return 

        if not active_timeframes:
            return

        self.logger.info(f"Các Dataframe đang được nhào nặn: {active_timeframes}M")
        
        df_dict = {}
        for tf in active_timeframes:
            df_tf = self._resample_data(df_1m, tf, "Min")
            
            if tf > 1:
                # [VÁ LỖI CỐT LÕI SỐ 3]: Cột VN30 cũng phải resample với origin='start_day'
                df_vn30_tf = df_1m[['Date', 'vn30_close']].set_index('Date').resample(f'{tf}min', label='left', origin='start_day').last().reset_index()
                df_tf = pd.merge(df_tf, df_vn30_tf, on='Date', how='left')
                df_tf['vn30_close'] = df_tf['vn30_close'].ffill()
                
            df_tf['Volume'] = df_tf['Volume'].fillna(0)
            df_dict[tf] = df_tf
        
        target_net_pos = 0
        votes = []
        
        for alpha in self.alphas:
            alpha_tf = getattr(alpha, 'timeframe', 5)
            
            if alpha_tf not in active_timeframes:
                target_net_pos += alpha.position
                votes.append(f"{alpha.name}: {alpha.position} (Wait)")
                continue
                
            df_target = df_dict[alpha_tf].copy()
            alpha_desired_pos = alpha.process_bar(df_target)
            
            target_net_pos += alpha_desired_pos
            votes.append(f"{alpha.name}: {alpha_desired_pos}")
            
        # =========================================================
        # PHẦN IN LOG "HÒM PHIẾU" 
        # =========================================================
        votes_str = " | ".join(votes)
        self.logger.info(f"Hòm phiếu: [{votes_str}]")
        self.logger.info(f"-> TỔNG VỊ THẾ MỤC TIÊU: {target_net_pos} HĐ")
        
        self.sync_with_broker(target_net_pos, current_price)
        
        # [THÊM LỆNH XẢ RAM SAU KHI MỌI THỨ ĐÃ XONG XUÔI]
        try:
            import state_manager
            state_manager.flush_to_disk()
        except ImportError:
            pass

    def sync_with_broker(self, target_net_pos: int, current_price: float):
        """
        Bàn giao con số tổng cho Execution Engine với MÃ GIAO DỊCH THẬT
        """
        # [QUAN TRỌNG]: Nhớ để dry_run=False khi bác đánh thật!
        success = self.engine.sync_position(
            target_pos=target_net_pos, 
            symbol=self.trade_symbol,  # <--- BẮN BẰNG MÃ THẬT
            dry_run=False
        )
        
        if success:
            self.virtual_position = target_net_pos