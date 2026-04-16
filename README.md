# 📈 MK QuantLab - VN30F1M Algorithmic Trading System

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![DNSE](https://img.shields.io/badge/Broker-DNSE_EntradeX-red.svg)
![Status](https://img.shields.io/badge/Status-Live_Testing-green.svg)

Hệ thống giao dịch thuật toán tự động hoàn toàn (Fully Automated Algorithmic Trading System) được thiết kế riêng cho Thị trường Phái sinh Việt Nam (Hợp đồng tương lai VN30F1M). Hệ thống sử dụng kiến trúc đa chiến lược (Multi-Alpha Ensemble) và xử lý đa khung thời gian (Multi-Timeframe) với khả năng quản trị rủi ro nghiêm ngặt.

## 🌟 Kiến trúc Hệ thống (System Architecture)

Hệ thống được thiết kế theo mô hình chuẩn của các quỹ Quant, chia thành 4 lớp độc lập:

1. **🧠 Alphas Engine (`alphas/`):** Nơi chứa các chiến lược giao dịch độc lập. Mỗi Alpha chịu trách nhiệm tính toán tín hiệu (Entry/Exit) trên một khung thời gian riêng biệt.
2. **⚖️ Portfolio Manager (`portfolio_manager.py`):** Lớp tổng hợp tín hiệu (Ensembling). Thu thập "phiếu bầu" từ các Alphas, xử lý xung đột tín hiệu và đưa ra quyết định Vị thế mục tiêu (Target Net Position).
3. **🔫 Execution Engine (`execution_engine.py`):** "Tay súng" khớp lệnh. So sánh Vị thế mục tiêu với Vị thế thực tế trên sàn để ra quyết định Mua/Bán. Tích hợp các "Cầu dao" (Circuit Breakers) để chặn lỗi hệ thống.
4. **🌐 Broker Client (`dnse_live_client.py`):** Lớp giao tiếp trực tiếp với API của sàn chứng khoán DNSE, quản lý Trading Token, lấy dữ liệu nến (OHLCV) và bắn lệnh.

## 🚀 Các Chiến Lược Hiện Có (Active Alphas)

Hệ thống hiện đang chạy tổ hợp các chiến lược có độ tương quan (Correlation) cực thấp để làm mượt đường cong vốn:

- **Alpha11_Gravity (1M):** Giao dịch phá vỡ lực hút VWAP (Volume Weighted Average Price) kết hợp xung lượng khối lượng trên khung 1 Phút.
- **Alpha48_TPT (3M):** Ứng dụng lý thuyết Chuyển pha Nhiệt động lực học (Thermodynamic Phase Transition) thông qua việc đo lường Shannon Entropy để bắt các cú sập gãy cấu trúc trên khung 3 Phút.
- **Alpha73_LFI (3M):** Chỉ số Ma sát Thanh khoản (Liquidity Friction Index). Phát hiện các điểm nghẽn thanh khoản cực đoan để bắt đỉnh/đáy ngắn hạn.

## 🛡️ Cơ Chế Bảo Vệ & Quản Trị Rủi Ro (Fail-Safes)

- **Position Clamping:** Giới hạn tổng vị thế tối đa (`max_net_position = 1`), ngăn chặn việc nhồi lệnh quá sức mua của tài khoản.
- **Order Quantity Limit:** Cầu dao chặn khối lượng 1 lần đặt lệnh (`max_order_qty = 2`) để chống trượt giá và lỗi vòng lặp vô tận.
- **Time Filters:** Bộ lọc cấm giao dịch trong thời gian nhiễu (Ví dụ: Đầu phiên ATO, cuối phiên ATC 14:30 - 14:45).
- **State Recovery:** Tự động lưu trạng thái vị thế ảo của từng Alpha vào file `.json`. Nếu máy tính mất điện hoặc sập, Bot sẽ tự khôi phục vị thế khi khởi động lại mà không bị mất dấu (`state_manager.py`).
- **Pre-flight Check:** Kịch bản khám sức khỏe tài khoản, kiểm tra quyền phái sinh và đo lường sức mua thực tế trước khi tham chiến.

## ⚙️ Hướng Dẫn Cài Đặt (Installation)

**1. Clone Repository:**

```bash
git clone https://github.com/your-username/system_vn30f1m_demo.git
cd system_vn30f1m_demo
```

**2. Cài đặt thư viện:**

```bash
pip install pandas numpy python-dotenv requests
```

**3. Cấu hình Biến Môi Trường (`.env`):**

Tạo file `.env` ở thư mục gốc và điền thông tin API của DNSE:
DNSE_API_KEY=your_api_key_here
DNSE_API_SECRET=your_api_secret_here
accountNo=your_derivative_account_id_here
**4. Khởi tạo danh sách ngày đáo hạn:**

Đảm bảo file `expiration_date.csv` chứa danh sách các ngày đáo hạn phái sinh của năm để Portfolio Manager nhận diện.

## 🕹️ Hướng Dẫn Sử Dụng (Usage)

**Bước 1: Khám sức khỏe tài khoản** *(Nên chạy trước phiên giao dịch)*

Kiểm tra xem cọc phái sinh còn đủ để đánh hay không, không yêu cầu mã OTP.

```bash
python preflight_check.py
```

**Bước 2: Khởi động Bot chạy Live**

Cập nhật mã hợp đồng hiện tại trong file `main.py` (Biến `CURRENT_TRADE_SYMBOL`). Sau đó chạy lệnh:

```bash
python main.py
```

Hệ thống sẽ yêu cầu nhập 6 số Smart OTP từ ứng dụng DNSE. Sau khi xác thực thành công, Bot sẽ tự động lấy data, phân tích và nằm chờ cơ hội.

## 📂 Cấu trúc Thư mục

```plaintext
├── alphas/                  # Chứa logic các chiến lược (Alpha)
│   ├── base_alpha.py        # Class nền tảng cho mọi chiến lược
│   ├── alpha11_gravity.py
│   ├── alpha48_tpt.py
│   └── alpha73_lfi.py
├── dnse/                    # Thư viện core kết nối API DNSE
├── .env                     # File chứa keys bảo mật (Không push lên Git)
├── dnse_live_client.py      # Lớp Wrapper bọc API sàn DNSE
├── execution_engine.py      # Bộ phận kiểm duyệt và khớp lệnh
├── main.py                  # Entry point: Nơi khởi chạy hệ thống
├── portfolio_manager.py     # Lớp quản lý vốn và phân bổ tín hiệu
├── preflight_check.py       # Script kiểm tra tài khoản, sức mua tĩnh
├── state_manager.py         # Quản lý bộ nhớ (Virtual positions)
└── trade_logger.py          # Ghi nhận lịch sử giao dịch ra CSV

````



## ⚠️ Khuyến Cáo (Disclaimer)

Hệ thống này được xây dựng cho mục đích nghiên cứu định lượng (Quantitative Research) và tự động hóa giao dịch cá nhân. Giao dịch phái sinh tiềm ẩn rủi ro rất cao và có thể dẫn đến mất toàn bộ số vốn ký quỹ. Tác giả không chịu trách nhiệm cho bất kỳ tổn thất tài chính nào phát sinh từ việc sử dụng mã nguồn này. Hãy kiểm thử kỹ lưỡng bằng tài khoản Demo hoặc thiết lập `dry_run=True` trước khi giao dịch tiền thật.

---

*Developed by MK QuantLab - 2026*
