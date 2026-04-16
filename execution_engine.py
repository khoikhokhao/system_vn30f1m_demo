import logging
import time

class ExecutionEngine:
    def __init__(self, live_client, max_net_position: int = 1, max_order_qty: int = 1):
        """
        Bộ Khớp Lệnh Thực Tế (Execution Engine)
        :param live_client: Đối tượng giao tiếp sàn DNSE (Đã viết ở Bước 1)
        :param max_net_position: [SIÊU THAM SỐ] Số HĐ tối đa được phép ôm (Chặn theo sức mua).
        :param max_order_qty: [SIÊU THAM SỐ] Khối lượng tối đa 1 lần bắn lệnh (Chặn lỗi béo tay).
        """
        self.client = live_client
        self.max_net_position = max_net_position
        self.max_order_qty = max_order_qty
        self.logger = logging.getLogger("EXEC_ENGINE")

    def sync_position(self, target_pos: int, symbol: str = "VN30F1M", dry_run: bool = True):
        self.logger.info("==================================================")
        self.logger.info(f"🔄 NHẬN LỆNH TỪ PORTFOLIO: Mục tiêu Net Position = {target_pos} HĐ")
        
        # -------------------------------------------------------------
        # 1. BẢO VỆ SỨC MUA (Ép Target Position không vượt quá MAX_NET_POSITION)
        # -------------------------------------------------------------
        original_target = target_pos
        if target_pos > self.max_net_position:
            target_pos = self.max_net_position
        elif target_pos < -self.max_net_position:
            target_pos = -self.max_net_position
            
        if original_target != target_pos:
            self.logger.warning(f"⚠️ CẦU DAO TỔNG: Ép vị thế từ {original_target} xuống {target_pos} để vừa sức mua ({self.max_net_position} HĐ).")

        # -------------------------------------------------------------
        # 2. SOI VỊ THẾ THẬT TẾ TRÊN SÀN (Double Check)
        # -------------------------------------------------------------
        actual_pos = self.client.get_real_position(symbol)
        self.logger.info(f"📊 Vị thế hiện tại trên sàn: {actual_pos} HĐ")

        # -------------------------------------------------------------
        # 3. TÍNH CHÊNH LỆCH ĐỂ VÀO LỆNH
        # -------------------------------------------------------------
        diff = target_pos - actual_pos

        if diff == 0:
            self.logger.info("✅ Sàn đã khớp hoàn toàn với tính toán. Đứng im.")
            self.logger.info("==================================================\n")
            return True

        side = "NB" if diff > 0 else "NS"
        quantity =int( abs(diff))

        # -------------------------------------------------------------
        # 4. BẢO VỆ TRƯỢT GIÁ (Chặn số lượng 1 lần đặt lệnh)
        # -------------------------------------------------------------
        if quantity > self.max_order_qty:
            self.logger.critical(f"🚫 CẦU DAO LỆNH: Yêu cầu bắn {quantity} HĐ vượt giới hạn {self.max_order_qty} HĐ/Lệnh!")
            self.logger.critical("-> TỪ CHỐI BẮN LỆNH NÀY ĐỂ BẢO VỆ TÀI KHOẢN.")
            self.logger.info("==================================================\n")
            return False

        # -------------------------------------------------------------
        # 5. KÉO CÒ
        # -------------------------------------------------------------
        order_res = self.client.place_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            order_type="MTL",
            price=0,
            dry_run=dry_run
        )

        if order_res and not dry_run:
            self.logger.info("Đang nán lại 2s chờ Sở khớp lệnh MTL...")
            time.sleep(2)
            new_pos = self.client.get_real_position(symbol)
            self.logger.info(f"🏁 Vị thế mới trên sàn sau khi bắn: {new_pos} HĐ.")
        
        self.logger.info("==================================================\n")
        return bool(order_res)