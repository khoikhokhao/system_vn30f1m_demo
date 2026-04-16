import requests
import pandas as pd
import datetime as dt
import logging
import time
import json
from dnse import DNSEClient

class DNSELiveClient:
    def __init__(self, api_key: str, api_secret: str, account_no: str):
        self.account_no = account_no
        self.logger = logging.getLogger("DNSE_LIVE")
        
        self.client = DNSEClient(
            api_key=api_key,
            api_secret=api_secret,
            base_url="https://openapi.dnse.com.vn"
        )
        
        self.trading_token = None
        self.cached_data = None

    def activate_trading_token(self, smart_otp: str) -> bool:
        try:
            status, body = self.client.create_trading_token(
                otp_type="smart_otp", 
                passcode=smart_otp, 
                dry_run=False
            )
            if status == 200:
                if isinstance(body, str):
                    body = json.loads(body)
                
                self.logger.info(f"🔍 DỮ LIỆU SÀN TRẢ VỀ: {body}")
                
                token_str = body.get('token') or body.get('tradingToken') or body.get('trading_token')
                if not token_str and 'data' in body:
                    token_str = body['data'].get('token') or body['data'].get('tradingToken')
                
                if token_str:
                    self.trading_token = token_str
                    self.client.trading_token = self.trading_token
                    self.logger.info("✅ Kích hoạt Token Đặt Lệnh thành công (Hạn 8 tiếng).")
                    return True
                else:
                    self.logger.error("❌ Không tìm thấy Token trong dữ liệu trả về!")
                    return False
            else:
                self.logger.error(f"❌ Sai mã OTP hoặc lỗi hệ thống: {body}")
                return False
        except Exception as e:
            self.logger.error(f"❌ Lỗi mạng khi lấy Token: {e}")
            return False
    def check_derivative_account_status(self) -> bool:
        """Kiểm tra xem tiểu khoản có quyền giao dịch phái sinh và đang ACTIVE hay không"""
        self.logger.info("🔍 Đang khám sức khỏe tiểu khoản, kiểm tra quyền Phái sinh...")
        try:
            # Gọi API get_accounts theo tài liệu SDK
            status, body = self.client.get_accounts(dry_run=False)
            
            if status == 200:
                if isinstance(body, str):
                    body = json.loads(body)
                    
                accounts = body.get('accounts', [])
                
                # Quét tìm đúng cái tiểu khoản bác đang cài đặt
                for acc in accounts:
                    if acc.get('id') == self.account_no:
                        is_derivative = acc.get('derivativeAccount', False)
                        deriv_status = acc.get('derivative', {}).get('status', 'INACTIVE')
                        
                        if is_derivative and deriv_status == 'ACTIVE':
                            self.logger.info("✅ TÀI KHOẢN ĐẠT CHUẨN: Quyền Phái sinh [BẬT], Trạng thái [ACTIVE].")
                            return True
                        else:
                            self.logger.critical(f"🚫 TÀI KHOẢN BỊ KHÓA HOẶC SAI TIỂU KHOẢN! (derivativeAccount={is_derivative}, status={deriv_status})")
                            self.logger.critical("-> Bác kiểm tra lại xem có copy nhầm ID tiểu khoản cơ sở vào file .env không nhé!")
                            return False
                
                self.logger.error(f"❌ Không tìm thấy tiểu khoản {self.account_no} trong danh sách tài khoản của bác!")
                return False
            else:
                self.logger.error(f"❌ Lỗi truy vấn thông tin tài khoản (Code {status}): {body}")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Lỗi mạng khi kiểm tra quyền tài khoản: {e}")
            return False

    def get_real_position(self, symbol="VN30F1M") -> int:
        try:
            status, body = self.client.get_positions(
                account_no=self.account_no, 
                market_type="DERIVATIVE", 
                dry_run=False
            )
            
            if status == 200:
                if isinstance(body, str):
                    body = json.loads(body)
                    
                positions = body.get('positions', []) if isinstance(body, dict) else body
                
                net_pos = 0
                for pos in positions:
                    if pos.get('symbol') == symbol:
                        # [ĐÃ SỬA LỖI TỬ HUYỆT]: Dùng đúng biến openQuantity theo tài liệu DNSE
                        volume = int(pos.get('openQuantity', 0))
                        side = pos.get('side', '')
                        if side == 'NB': net_pos += volume
                        elif side == 'NS': net_pos -= volume
                return net_pos
            else:
                self.logger.warning(f"⚠️ Sàn từ chối cung cấp vị thế (Code {status}): {body}")
                return 0
        except Exception as e:
            self.logger.error(f"❌ Lỗi kết nối khi soi vị thế: {e}")
            return 0
    def get_best_loan_package(self, symbol="VN30F1M") -> int:
        """Gọi API hỏi sàn danh sách các gói vay Phái sinh và chọn gói tốt nhất"""
        self.logger.info(f"🔎 Đang truy vấn các gói vay (Margin) cho mã {symbol}...")
        try:
            status, body = self.client.get_loan_packages(
                account_no=self.account_no,
                market_type="DERIVATIVE",
                symbol=symbol,
                dry_run=False
            )
            
            if status == 200:
                if isinstance(body, str):
                    body = json.loads(body)
                    
                packages = body.get('loanPackages', [])
                if not packages:
                    self.logger.error("❌ Sàn không trả về bất kỳ gói vay nào cho tài khoản này!")
                    return None
                    
                # In ra log để bác tự giám sát tỷ lệ ký quỹ của mình
                for p in packages:
                    self.logger.info(f"   + Gói [{p.get('id')}]: {p.get('name')} | Ký quỹ ban đầu: {p.get('initialRate')*100}% | Xử lý: {p.get('liquidRate')*100}%")
                
                # Logic chọn gói: Ưu tiên chọn gói có tỷ lệ ký quỹ (initialRate) thấp nhất để tối ưu vốn
                best_package = min(packages, key=lambda x: x.get('initialRate', 1.0))
                best_id = best_package.get('id')
                
                self.logger.info(f"✅ Đã chốt chọn gói vay ID: {best_id} (Ký quỹ: {best_package.get('initialRate')*100}%)")
                return best_id
            else:
                self.logger.error(f"❌ Lỗi truy vấn gói vay (Code {status}): {body}")
                return None
        except Exception as e:
            self.logger.error(f"❌ Lỗi mạng khi truy vấn gói vay: {e}")
            return None

    def place_order(self, symbol: str, side: str, quantity: int, order_type: str = "MTL", price: float = 0, dry_run: bool = False):
        if not self.trading_token:
            self.logger.error("🚫 CHƯA CÓ TRADING TOKEN! Vui lòng khởi động lại Bot và nhập OTP.")
            return None

        if order_type != "LO":
            price = 0

        # LẤY ID GÓI VAY TRƯỚC KHI ĐẶT LỆNH
        loan_pkg_id = self.get_best_loan_package(symbol)
        if not loan_pkg_id:
            self.logger.error("🚫 KHÔNG TÌM THẤY GÓI VAY! Hủy bỏ lệnh đặt để bảo toàn vốn.")
            return None

        mode_str = "THỰC CHIẾN" if not dry_run else "DIỄN TẬP (DRY RUN)"
        self.logger.warning(f"🔫 KÉO CÒ [{mode_str}]: {side} {quantity} HĐ {symbol} (Lệnh {order_type} | Gói vay: {loan_pkg_id}).")
        
        try:
            payload_data = {
                "accountNo": self.account_no,
                "symbol": symbol,
                "side": side,
                "orderType": order_type,
                "price": price,
                "quantity": quantity,
                "loanPackageId": loan_pkg_id  # <--- ĐÃ BỔ SUNG YẾU TỐ BẮT BUỘC
            }
            
            status, body = self.client.post_order(
                market_type="DERIVATIVE",
                order_category="NORMAL",
                payload=payload_data,
                trading_token=self.trading_token,
                dry_run=dry_run
            )
            
            if dry_run and status is None:
                self.logger.info("🎯 [DRY RUN] LỆNH GIẢ LẬP ĐÃ LÊN NÒNG HOÀN HẢO (Bóp phanh an toàn, không bắn thật)!")
                return {"status": "DRY_RUN_SUCCESS"}

            if status == 200:
                if isinstance(body, str):
                    body = json.loads(body)
                self.logger.info(f"🎯 LỆNH ĐÃ ĐƯỢC ĐẨY LÊN SÀN THÀNH CÔNG: {body}")
                return body
            else:
                self.logger.error(f"❌ SÀN TỪ CHỐI LỆNH (Code {status}): {body}")
                return None
                
        except Exception as e:
            self.logger.error(f"💥 LỖI NGHIÊM TRỌNG KHI BẮN LỆNH: {e}")
            return None
    def get_historical_candles(self, symbol: str, resolution: int = 1, limit: int = 30000) -> pd.DataFrame:
        try:
            end_time = int(dt.datetime.now().timestamp())
            start_time = end_time - (limit * resolution * 60 * 3) 
            url = "https://services.entrade.com.vn/chart-api/v2/ohlcs/derivative"
            if symbol == "VN30": url = "https://services.entrade.com.vn/chart-api/v2/ohlcs/index"
            params = {"symbol": symbol, "resolution": resolution, "from": start_time, "to": end_time}
            res = requests.get(url, params=params, timeout=15)
            res.raise_for_status()
            data = res.json()
            if 't' not in data or len(data['t']) == 0: return pd.DataFrame()
            df = pd.DataFrame({
                'Date': pd.to_datetime(data['t'], unit='s').tz_localize('UTC').tz_convert('Asia/Ho_Chi_Minh').tz_localize(None),
                'Open': data['o'], 'High': data['h'], 'Low': data['l'], 'Close': data['c'], 'Volume': data['v']
            })
            return df.sort_values('Date').tail(limit).reset_index(drop=True)
        except Exception as e: return pd.DataFrame()

    def get_market_data_for_alphas(self, derivative_symbol="VN30F1M", base_symbol="VN30", limit=30000) -> pd.DataFrame:
        if self.cached_data is None:
            df_f1m = self.get_historical_candles(derivative_symbol, resolution=1, limit=limit)
            df_vn30 = self.get_historical_candles(base_symbol, resolution=1, limit=limit)
            if df_f1m.empty or df_vn30.empty: return pd.DataFrame()
            df_f1m.set_index('Date', inplace=True)
            df_vn30.set_index('Date', inplace=True)
            df_f1m = df_f1m.join(df_vn30['Close'].rename('vn30_close'), how='left')
            df_f1m['vn30_close'] = df_f1m['vn30_close'].ffill()
            self.cached_data = df_f1m.reset_index()
            return self.cached_data
        else:
            df_f1m_new = self.get_historical_candles(derivative_symbol, resolution=1, limit=10)
            df_vn30_new = self.get_historical_candles(base_symbol, resolution=1, limit=10)
            if df_f1m_new.empty: return self.cached_data 
            df_f1m_new.set_index('Date', inplace=True)
            if not df_vn30_new.empty:
                df_vn30_new.set_index('Date', inplace=True)
                df_f1m_new = df_f1m_new.join(df_vn30_new['Close'].rename('vn30_close'), how='left')
            else:
                import numpy as np
                df_f1m_new['vn30_close'] = np.nan
            df_f1m_new['vn30_close'] = df_f1m_new['vn30_close'].ffill()
            df_new_formatted = df_f1m_new.reset_index()
            combined = pd.concat([self.cached_data, df_new_formatted], ignore_index=True)
            combined = combined.drop_duplicates(subset=['Date'], keep='last')
            combined['vn30_close'] = combined['vn30_close'].ffill()
            self.cached_data = combined.tail(limit).reset_index(drop=True)
            return self.cached_data