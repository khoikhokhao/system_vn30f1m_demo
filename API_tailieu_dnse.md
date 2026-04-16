
---
sidebar_position: 1
---

#  DNSE API Platform
---

### Giới thiệu

Chào mừng khách hàng và đối tác đến với tài liệu ***LightSpeed API*** của DNSE cung cấp. Dịch vụ OpenAPI mang đến trải nghiệm đầu tư toàn diện, linh hoạt và hiện đại với những lợi thế vượt trội:

- **Chủ động trong việc xây dựng hành trình đầu tư:** Từ theo dõi biến động thị trường, đưa ra quyết định đến đặt lệnh – mọi thao tác đều có thể được lập trình và quản lý chủ động bởi người dùng.
- **Nguồn dữ liệu thị trường đa dạng:** Cung cấp đầy đủ từ độ sâu thị trường, biến động giá thị trường, thông tin OHLC, các chỉ số indices và nhiều loại dữ liệu khác.
- **Tốc độ xử lý vượt trội:** Cập nhật realtime thông tin biến động tài sản, sổ lệnh giao dịch.
- **Khả năng mở rộng và tích hợp đa nền tảng:** Xây dựng ứng dụng giao dịch chủ động đơn giản cho cá nhân đến hệ thống phân tích và nền tảng giao dịch phức tạp dành cho tổ chức.

### Đối tượng sử dụng

- Nhà đầu tư cá nhân muốn số hóa chiến lược và quản lý danh mục realtime.
- Doanh nghiệp Công nghệ Tài chính muốn tích hợp dữ liệu thị trường và giao dịch vào sản phẩm.
- Đối tác Tổ chức Tài chính cần giám sát danh mục và xử lý số lượng lệnh lớn hay mở rộng dịch vụ tích hợp.
- Nhà phát triển công nghệ xây dựng giao dịch chủ động, dashboard hoặc công cụ phân tích.

### Sơ đồ hệ thống

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/sd1.png)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/sd1.png)
</div>

### Mô hình đa tầng bảo mật

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/sd2.png)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/sd2.png)
</div>

Sau khi đăng ký thành công, khách hàng sẽ nhận được bộ chuỗi bảo mật bao gồm: API Key, API secret.

**API Key**

- API Key được cung cấp sau khi đăng ký sử dụng OpenAPI, đây là khóa định danh duy nhất, đóng vai trò nhận diện và xác minh danh tính khi kết nối với hệ thống.
- API Key phải được giữ bí mật và chỉ dùng cho mục đích gọi API. Khách hàng có thể chủ động tạo mới hoặc thu hồi bất kỳ lúc nào.
- Khi tạo mới hoặc hủy API Key, bộ khóa cũ sẽ lập tức vô hiệu lực, giảm thiểu rủi ro khi bị lộ hoặc không còn nhu cầu sử dụng.

**API Secret**

- API Secret là một chuỗi ký tự mật dùng để xác minh và bảo vệ API, được sử dụng để sinh chữ ký số Signature cần thiết cho hầu hết các REST API.
- API Key và API Secret là cặp khóa luôn đi cùng nhau, có thể hiểu tương tự như tên người dùng và mật khẩu.
- API Secret chỉ hiển thị duy nhất một lần khi đăng ký thành công để bảo mật cho tài khoản. Khách hàng cần chủ động lưu lại và quản lý thông tin này.

**Phương thức xác thực lớp thứ 2 (2FA)**

Bên cạnh API Key và API Secret, hệ thống áp dụng thêm lớp xác thực thứ hai (2FA) với giao dịch đặt lệnh.

- Tại mỗi thời điểm, chỉ một phương thức xác thực lớp thứ hai được kích hoạt và là phương thức duy nhất được hệ thống chấp nhận khi thực hiện xác thực OTP.
- Khách hàng lựa chọn và có thể thay đổi giữa Smart OTP hoặc Email OTP.

Việc kết hợp API Key, API Secret và xác thực lớp thứ hai đảm bảo rằng chỉ các yêu cầu được thực hiện bởi đúng chủ tài khoản, đáp ứng đầy đủ điều kiện xác thực mới được hệ thống chấp nhận và xử lý.

--- 

:::tip[Lưu ý]

Các chuỗi bảo mật DNSE đã cung cấp trên là thông tin nhạy cảm cần được bảo mật nghiêm ngặt. Tuyệt đối không chia sẻ hoặc tiết lộ cho bất kỳ cá nhân hay tổ chức nào không thuộc phạm vi được ủy quyền sử dụng. Việc bảo mật tốt giúp ngăn chặn các rủi ro về truy cập trái phép và bảo vệ tài khoản.

:::
---
sidebar_position: 2
---

# Đăng ký & Quản lý dịch vụ
---

### Đăng ký sử dụng

Để bắt đầu tích hợp và sử dụng Lightspeed API của DNSE, khách hàng có thể thực hiện đăng ký dễ dàng qua [trang web giao dịch trực tuyến](https://entradex.dnse.com.vn) chính thức của DNSE

#### Bước 1: Truy cập trang web OpenAPI DNSE
Khách hàng chọn **Đăng ký** tại trang chủ OpenAPI: <a href="https://developers.dnse.com.vn"></a>

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk.png)
</div>

Hệ thống sẽ chuyển đến trang giao dịch trực tuyến của DNSE để khách hàng đăng nhập (hoặc tạo tài khoản mới nếu chưa có). Sau khi đăng nhập sẽ điều hướng đến trang thông tin Lightspeed API.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk2.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk2.png)
</div>

Hoặc ngay tại giao diện đã đăng nhập của trang giao dịch trực tuyến DNSE, khách hàng chọn Họ tên để đến trang Thông tin tài khoản, chọn tiếp LightSpeed API.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk3.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk3.png)

</div>

#### Bước 2: Thực hiện đăng ký
Khách hàng lựa chọn duy nhất 1 phương thức xác thực lớp thứ hai để nhận mã OTP khi thực hiện giao dịch đặt lệnh qua OpenAPI.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk4.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk4.png)

</div>

**Smart OTP**

- Để chọn phương thức, tài khoản chứng khoán cần phải kích hoạt sử dụng SmartOTP trên ứng dụng DNSE.
- Mã OTP để đặt lệnh lấy trực tiếp tại ứng dụng DNSE trên thiết bị di động đã đăng ký SmartOTP.

**Email OTP**

- Để chọn phương thức, tài khoản chứng khoán cần có Email hợp lệ và đã được xác thực.
- Mã OTP để đặt lệnh được gửi về địa chỉ Email đã đăng ký.
- Khách hàng có thể sử dụng tối đa 2 địa chỉ Email để nhận mã OTP.

Sau khi đã lựa chọn phương thức xác thực lớp thứ hai, chọn **Đăng ký**.

Khách hàng kiểm tra lại thông tin, thực hiện Xác nhận và Xác thực OTP để hoàn tất đăng ký.

#### Bước 3: Đăng ký thành công
Xác thực thành công, hệ thống sẽ hiển thị trạng thái Đã đăng ký và các thông tin quan trọng để kết nối OpenAPI.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk5.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk5.png)
</div>

API Secret chỉ hiển thị một lần duy nhất sau khi đăng ký thành công. Khách hàng cần chủ động lưu lại và quản lý thông tin này.

Tham khảo chi tiết về các khóa bảo mật <a href="https://developers.dnse.com.vn/docs/guide/trading-api/authentication">tại đây.</a>

---
### Quản lý API Key

Sau khi đăng ký thành công, khách hàng có thể chủ động quản lý vòng đời API Key của mình, bao gồm :
- **Tạo lại API Key:** Bộ khóa API Key và API Secret sẽ tự động bị vô hiệu hóa và không thể tiếp tục sử dụng. Một bộ khóa mới sẽ được sinh ra và API Secret chỉ hiển thị một lần duy nhất. Việc Tạo lại này không ảnh hưởng tới phương thức xác thực lớp thứ 2 đang sử dụng.
- **Hủy API Key:** Đồng nghĩa với Hủy sử dụng dịch vụ OpenAPI, nếu muốn sử dụng lại, khách hàng cần thực hiện đăng ký mới từ đầu.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk6.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk6.png)
</div>

Quản lý API Key giúp đảm bảo an toàn bảo mật, đặc biệt trong trường hợp nghi ngờ bị lộ thông tin hoặc không còn nhu cầu sử dụng.

:::tip[Lưu ý]

Thông tin về API key, API secret là thông tin nhạy cảm cần được bảo mật nghiêm ngặt. Tuyệt đối không chia sẻ hoặc tiết lộ cho bất kỳ cá nhân hay tổ chức nào không thuộc phạm vi được ủy quyền sử dụng. Việc bảo mật tốt giúp ngăn chặn các rủi ro về truy cập trái phép và bảo vệ tài khoản.


:::

---
### Thay đổi phương thức xác thực lớp thứ 2

Tại một thời điểm, chỉ có một phương thức xác thực lớp thứ 2 được sử dụng cho OpenAPI. Sau khi đăng ký thành công, khách hàng có thể thay đổi cách nhận mã OTP bất kỳ lúc nào giữa Smart OTP và Email OTP.

Khách hàng chọn **Đổi phương thức xác thực** và thao tác xác thực OTP để hoàn tất.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk7.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk7.png)
</div>

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk8.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk8.png)
</div>

Việc thay đổi phương thức xác thực không ảnh hưởng tới các khóa API Key và API Secret hiện tại.

#### Lưu ý sử dụng Email OTP

Hệ thống hỗ trợ tối đa 2 địa chỉ Email để nhận mã OTP

- Trường hợp đăng ký mới: Khách hàng cần chọn Email OTP → Thêm Email thứ 2 → gửi yêu cầu Đăng ký.
- Trường hợp đã đăng ký:

  - Nếu khách hàng đang sử dụng Email OTP → Thêm Email thứ 2 → xác nhận OTP cập nhật Email.
  - Nếu khách hàng đang sử dụng Smart OTP → Thêm Email thứ 2 → Đổi phương thức xác thực.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk9.png?ts=123456)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/dk9.png)
</div>

Khách hàng cần xác thực Email thứ 2 để kích hoạt nhận mã OTP về địa chỉ mail này. Đường link xác thực sẽ được gửi về địa chỉ Email thứ 1 để đảm bảo an toàn và bảo mật.
---
sidebar_position: 3
---

# Xác thực
---

### Bước xác thực thứ 1

Trong giao tiếp giữa ứng dụng của Người dùng và hệ thống DNSE, việc xác minh danh tính và bảo vệ tính toàn vẹn của dữ liệu là yêu cầu bắt buộc. Hầu hết các RESTful API cần kèm theo đủ hai thông tin là API Key và Signature (chữ ký số) trong Headers để hệ thống xác thực và cho phép xử lý yêu cầu.

#### API Key
- API Key là khóa định danh duy nhất được cấp cho từng tài khoản khi đăng ký sử dụng LightSpeed API.
- Trong mỗi request, API Key là thành phần bắt buộc để nhận diện ứng dụng và áp dụng cơ chế phân quyền, giới hạn truy cập.
- API Key cần được quản lý cẩn trọng và tránh chia sẻ công khai. Người dùng có thể chủ động tạo mới hoặc thu hồi API Key trong trường hợp nghi ngờ lộ thông tin hoặc không còn nhu cầu sử dụng.
- Trường hợp bị rò rỉ, các yêu cầu trái phép sẽ không được chấp nhận nếu không có Signature hợp lệ đi kèm.

#### Signature

- Signature chữ ký số là lớp bảo mật bổ sung để xác nhận tính chính xác và toàn vẹn của từng yêu cầu, tránh giả mạo hay sửa đổi giữa đường truyền.
- Được tạo bằng các thành phần: API Secret, Path, Timestamp, Nonce, Query params (nếu có).
  Tất cả đưa vào thuật toán hashing (HMAC SHA256) theo quy tắc hệ thống cung cấp để sinh ra Signature.
- Nếu Signature bị sai hoặc không được gửi kèm theo, yêu cầu sẽ bị từ chối ngay lập tức.

Ví dụ Headers:

```json lines
{
  "method": "GET",
  "path": "/accounts",
  "headers": {
    "x-api-key": "lB58g6iWzyrNx2EhwwQXeYeoAnkzlaXkJWi",  // APIKey được cấp khi đăng ký dịch vụ
    "x-signature": "96299733e5b56aaa6c91a8f88b472c9721fde161e0d89df8c",  // Chữ ký số theo thuật toán HMAC SHA256
    "date":"Fri, 16 Jan 2026 07:11:30 +0000"  // Thời gian tạo yêu cầu (UTC)
  },
}
```
DNSE cung cấp SDKs tự động tạo Signature cho mỗi Request giúp giảm độ phức tạp và hạn chế lỗi xác thực khi tích hợp. Tham khảo [tại đây.](https://github.com/dnse-tech/openapi-sdk)

----

### Bước xác thực thứ 2

Nếu API Key đóng vai trò là lớp bảo mật thứ nhất, thì Trading Token là lớp bảo mật thứ 2 đối với giao dịch đặt lệnh theo cơ chế 2FA – Two Factor Authentication.

Trading Token được cung cấp sau khi người dùng hoàn tất xác thực OTP, và là thông tin bắt buộc phải được truyền kèm trong các API đặt lệnh.

Ví dụ trong Headers

```json lines
{
  "method": "POST",
  "path": "/accounts/orders",
  "headers": {
    "x-api-key": "lB58g6iWzyrNx2EhwwQXeYeoAnkzlaXkJWi",   // APIkey được cấp khi đăng ký dịch vụ
    "x-signature": "fjsdhfryt6aaa6c91a8f88b472c9721fde161e0d89df8c",    // Chữ ký số theo thuật toán HMAC SHA256
    "trading-token": "7ceef658-9f01-414e-8b3e-faa77bb9061e",    // Token đặt lệnh         
    "date": "Fri, 16 Jan 2026 07:11:30 +0000"   // Thời gian tạo yêu cầu (UTC)
  },
}
```

#### Phương thức OTP

OpenAPI hiện hỗ trợ hai phương thức Email OTP hoặc Smart OTP để xác thực và tạo Trading Token. Tại mỗi thời điểm, chỉ một phương thức OTP duy nhất được hoạt động.

##### Email OTP

- Mã OTP được gửi về địa chỉ email mà người dùng đã đăng ký, có hiệu lực trong 2 phút.
- Ưu điểm:
  - Quản lý linh hoạt, có thể tự động hóa trong quy trình xác thực, mang lại trải nghiệm liền mạch cho người dùng khi xây dựng hệ thống giao dịch qua OpenAPI.
- Hạn chế:
  - Thời gian nhận email phụ thuộc vào bên thứ 3.

Tham khảo Endpoint <a href="https://developers.dnse.com.vn/docs/dnse/send-email-otp">Gửi Email OTP</a>

##### Smart OTP

- Mã OTP được lấy trực tiếp trên ứng dụng DNSE đã đăng ký SmartOTP, có hiệu lực trong 30 giây.
- Ưu điểm:
  - Mã luôn có sẵn trên ứng dụng và chỉ sinh trên thiết bị đã đăng ký.
  - Độ bảo mật cao do, giảm thiểu nguy cơ giả mạo hoặc truy cập trái phép.
- Hạn chế:
  - Người dùng cần thao tác thủ công vào ứng dụng để lấy mã khi cần thực hiện xác thực.
- Hướng dẫn:
  - Tại app EntradeX by DNSE trên thiết bị di động, người dùng chọn mục SmartOTP từ menu, chọn Lấy mã OTP cho thiết bị khác.

  <div className="guideImg">

  [![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/otp.png)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/otp.png)

  </div>

#### Xác thực OTP

Để lấy Trading Token, người dùng thực hiện gửi yêu cầu đến Endpoint <a href="https://developers.dnse.com.vn/docs/dnse/2-fa-verification">xác thực OTP.</a>, trong đó:

```json lines
{
  "method": "POST",
  "path": "/openapi/registration/trading-token",
  "headers": {
    "x-api-key": "lB58g6iWzyrNx2EhwwQXeYeoAnkzlaXkJWi",        // APIkey được cấp khi đăng ký dịch vụ
    "signature": "fjsdhfryt6aaa6c91a8f88b472c9721fde161e0d89df8c",     // Chữ ký số theo thuật toán HMAC SHA256
    "date":"Fri, 16 Jan 2026 07:11:30 +0000",  // Thời gian tạo yêu cầu (UTC)  
    "Content-Type": "application/json"
  },
  "body": {
    "otpType": "email_otp",   // Phương thức OTP đang sử dụng (email_otp hoặc smart_otp)
    "passcode": "1234"     // Mã OTP tương ứng phương thức
  }
}
```

Tại một thời điểm, tài khoản chỉ được đăng ký sử dụng duy nhất 1 phương thức và cần truyền đúng trường tương ứng `smart-otp` hoặc `email-otp`. Trường hợp tài khoản đăng ký sử dụng Smart OTP nhưng truyền lên `email-otp` (hoặc ngược lại) yêu cầu gửi đến hệ thống sẽ bị từ chối.

Nếu thông tin hợp lệ, hệ thống sẽ trả về Trading Token có hiệu lực trong 8 giờ. Người dùng có thể thực hiện nhiều giao dịch liên tiếp mà không cần xác thực lại OTP. Khi Trading Token hết hiệu lực, người dùng cần thực hiện lại bước xác thực OTP để tạo token mới.
---
sidebar_position: 2
---

#  Tài khoản giao dịch
---

Mỗi nhà đầu tư khi mở tài khoản tại DNSE sẽ có các thông tin định danh duy nhất trên hệ thống. Một tài khoản có thể sở hữu một hoặc nhiều tiểu khoản giao dịch. Việc nắm rõ cấu trúc này rất quan trọng để người dùng tích hợp và sử dụng API đúng cách.

Các thông tin này được trả ra trong response của <a
href="https://developers.dnse.com.vn/docs/dnse/get-accounts">/get-accounts</a>


```json lines
{
  "name": "Nguyen Hoang A",         // Họ tên khách hàng
  "custodyCode": "064CAA8386",      // Số tài khoản lưu ký tại VSD
  "investorId": "1002003456",       // Mã định danh khách hàng tại DNSE
  "accounts": [                     // Danh sách tiểu khoản thuộc tài khoản
    {
      "id": "0001009212",           // Số tiểu khoản giao dịch
      "dealAccount": true,          // Tiểu khoản theo Deal hoặc không (true/ false)
      "derivativeAccount": true,    // Tiểu khoản được phép giao dịch phái sinh hoặc không (true/ false)
      "derivative": {
        "status": "ACTIVE"          // Trạng thái tiểu khoản phái sinh (ACTIVE: Hoạt động/ INACTIVE: Ngưng hoạt động)
      }
    },
    {
      "id": "0001177757",           // Số tiểu khoản giao dịch            
      "dealAccount": true,          // Tiểu khoản theo Deal hoặc không (true/ false)
      "derivativeAccount": false,    // Tiểu khoản được phép giao dịch phái sinh hoặc không (true/ false)
      "derivative": {}
    }
  ]
}
```
---
sidebar_position: 3
---

# Margin tại DNSE
---

Khác với cách quản trị rủi ro trên tài khoản tổng, với Margin tại DNSE - mỗi một Deal (bao gồm một mã chứng khoán và một gói vay ký quỹ) khác nhau của khách hàng sẽ được quản trị tách bạch:

- Các Deals khác nhau về tỷ lệ vay được quản lý tách biệt, danh mục của khách hàng có thể gồm nhiều Deals vay khác nhau.
- Cách tính giá trung bình, giá hòa vốn của mỗi Deal (đã bao gồm lãi vay và các chi phí khác) rõ ràng, chính xác hơn so với giá vốn truyền thống.
- Tỷ lệ ký quỹ của mỗi Deal được kiểm soát độc lập. DNSE sẽ chỉ yêu cầu ký quỹ bổ sung hoặc bán giải chấp Deal có tỷ lệ xuống dưới mức cảnh báo mà không ảnh hưởng tới các Deal an toàn khác.

Đây là sự khác biệt mà DNSE xây dựng để khách hàng của mình quản lý tài sản minh bạch hơn (mô hình Isolated Margin)

### Gói vay (Loan packages)

Gói vay là khái niệm đại diện cho chính sách sản phẩm tại DNSE. Mỗi gói vay quy định các điều kiện áp dụng cho giao dịch, bao gồm: phí giao dịch, tỷ lệ vay, tỷ lệ ký quỹ, lãi suất vay, kỳ hạn và một số thông tin khác.

Các gói vay được áp dụng cho từng mã chứng khoán được trả về trong response Endpoint <a href="https://developers.dnse.com.vn/docs/dnse/get-loan-packages">/Danh sách gói vay</a>

**Danh sách gói vay cơ sở**

VD: Danh sách gói vay cho mã HPG

```json lines
{
  "symbol": "HPG",         // Mã chứng khoán
  "marketType": "STOCK",   // Loại thị trường (STOCK: cơ sở / DERIVATIVE: phái sinh)
  "loanPackages": [       // Danh sách gói vay 
    {
      "id": 1775,         // Mã gói vay
      "name": "Mana RocketX LS 5.99% HPG - KQ 100%",    // Tên gói vay 
      "initialRate": 1,             // Tỷ lệ ký quỹ ban đầu 
      "interestRate": 0.0599,       // Tỷ lệ lãi vay (nếu phát sinh ứng sức mua, nợ margin)
      "liquidRate": 0.3,            // Tỷ lệ xử lý (force sell)
      "maintenanceRate": 0.4,       // Tỷ lệ duy trì (call margin)
      "type": "M",              // Loại gói vay (M: gói vay margin/ N: gói tiền mặt)
      "brokerFirmBuyingFeeRate": 0,     //  Phí mua chứng khoán cơ sở DNSE thu
      "brokerFirmSellingFeeRate": 0     //  Phí bán chứng khoán cơ sở DNSE thu
    },
    {
      "id": 1769,       // Mã gói vay
      "name": "Rocket X LS 5.99% HPG - KQ 50%",    // Tên gói vay 
      "initialRate": 0.5,           // Tỷ lệ ký quỹ ban đầu 
      "interestRate": 0.0599,       // Tỷ lệ lãi vay (nếu phát sinh ứng sức mua, nợ margin)
      "liquidRate": 0.3,            // Tỷ lệ xử lý (force sell)
      "maintenanceRate": 0.4,       // Tỷ lệ duy trì (call margin)
      "type": "M",                  // Loại gói vay (M: gói vay margin/ N: gói tiền mặt)
      "brokerFirmBuyingFeeRate": 0.00045,     //  Phí mua chứng khoán cơ sở DNSE thu
      "brokerFirmSellingFeeRate": 0.00045     //  Phí bán chứng khoán cơ sở DNSE thu
    }  
  ]
}
```

VD: Danh sách gói vay cho mã VGI

```json lines
{
  "symbol": "VGI",      // Mã chứng khoán
  "marketType": "STOCK",      // Loại thị trường (STOCK: cơ sở / DERIVATIVE: phái sinh)
  "loanPackages": [     // Danh sách gói vay 
    {
      "id": 1036,   // Mã gói vay
      "name": "GD tiền mặt",    // Tên gói vay 
      "type": "N",      // Loại gói vay (M: gói vay margin/ N: gói tiền mặt)
      "brokerFirmBuyingFeeRate": 0,     //  Phí mua chứng khoán cơ sở DNSE thu
      "brokerFirmSellingFeeRate": 0     //  Phí bán chứng khoán cơ sở DNSE thu
    }
  ]
}
```

Đối với giao dịch chứng khoán cơ sở, hệ thống sẽ trả về tối đa 2 gói vay mà người dùng có thể sử dụng để đặt lệnh cho mã chứng khoán truy vấn, bao gồm:

- Gói vay giao dịch tiền mặt:

    + Tỷ lệ ký quỹ tiền mặt 100% (`initialRate` = 1)
    + Dành cho giao dịch không sử dụng đòn bẩy tiền vay
- Gói vay ký quỹ (margin) cơ bản:

    + Dành cho giao dịch có sử dụng đòn bẩy tiền vay (`initialRate` ≠ 1)

**Danh sách gói vay phái sinh**

VD: Danh sách gói vay cho mã 41I1G1000

```json lines
{
  "symbolType": "VN30F1M",           // Mã giao dịch Hợp đồng tương lai
  "marketType": "DERIVATIVE",       // Loại thị trường 
  "loanPackages": [                 // Danh sách gói vay 
    {
      "id": 1306,                   // Mã gói vay
      "name": "Gói giao dịch 01",   // Tên gói vay 
      "initialRate": 0.1848,        // Tỷ lệ ký quỹ ban đầu
      "maintenanceRate": 0.1771,    // Tỷ lệ duy trì (call margin)
      "liquidRate": 0.1735,         // Tỷ lệ xử lý (force sell)
      "tradingFee": {               // Chính sách phí giao dịch (dành cho phái sinh)
        "id": 1304,                 // ID chính sách phí    
        "name": "Miễn phí",         // Tên phí
        "scope": "PRODUCT",         // Phạm vi áp dụng chính sách
        "channel": "ALL",           // Kênh giao dịch áp dụng
        "schemaType": "FIXED",      // Loại phí cố định
        "createdDate": "2023-02-02T04:22:56.199278Z",       // Thời điểm tạo chính sách
        "modifiedDate": "2023-02-02T04:22:56.199278Z",      // Thời điểm cập nhật chính sách
        "fixedTradingFee": 2000,        // Phí giao dịch 1 hợp đồng
        "fixedDailyCloseTradingFee": 2000      // Phí giao dịch 1 hợp đồng đóng luôn trong ngày 
      }
    }
  ]
}
```

Với sản phẩm phái sinh, thông thường tài khoản giao dịch của khách hàng chỉ được gắn một gói vay với một bộ tỷ lệ ký quỹ, duy trì và xử lý duy nhất áp dụng cho tất cả các mã phái sinh.

### Deal

Deals hay còn có thể hiểu là danh mục tài sản của khách hàng. Một Deal được hình thành bởi 1 mã chứng khoán và 1 gói vay:

- Với cùng một mã có thể có nhiều Deals độc lập nếu bạn mua cùng mã nhưng chọn gói vay khác nhau
- Việc cho vay, thu nợ, quản trị rủi ro được thực hiện trên từng Deal

Ví dụ:

- Lần 1: Mua 100cp HPG với gói vay “GD Tiền mặt", hệ thống sẽ tạo 1 Deal HPG Tiền mặt, tỷ lệ Ký quỹ 100%
- Lần 2: Mua 500cp HPG với gói vay margin “Tiền mặt 50%”, hệ thống sẽ tạo Deal mới HPG Tiền mặt 50% (khác với Deal bên trên), được hiểu là khách hàng ký quỹ 50% và sử dụng tiền vay 50% tính trên tổng số tiền khớp lệnh mua.
- Lần 3: Mua 200cp HPG với gói vay “Tiền mặt 100%”, do cùng gói vay với lần thứ 1, nên hệ thống gộp khối lượng mua thêm vào Deal HPG Tiền mặt 100%; tổng khối lượng sau mua là 300cp.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/deal.png)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/deal.png)
</div>

Khách hàng có thể tìm hiểu thêm về sản phẩm giao dịch ký quỹ theo DEAL [tại đây.](https://hdsd.dnse.com.vn/san-pham-dich-vu/sp-giao-dich-ky-quy-theo-deal/thong-tin-chung)
---
sidebar_position: 4
---


# Lệnh giao dịch
---

### Vòng đời lệnh

Vòng đời lệnh mô tả các trạng thái mà một lệnh có thể đi qua kể từ lúc bạn gửi yêu cầu đến khi kết thúc.

<div className="guideImg">

[![Locale Dropdown](https://cdn.dnse.com.vn/dnse-openapi/doc/img/sd3.png)](https://cdn.dnse.com.vn/dnse-openapi/doc/img/sd3.png)
</div>

### Trạng thái lệnh

| Trạng thái          | Giải nghĩa            | Chú thích                                                                                 |
|---------------------|-----------------------|-------------------------------------------------------------------------------------------|
| **Pending**         | Lệnh mới được tạo     | Lệnh vừa gửi lên hệ thống, đang được kiểm tra và xử lý nội bộ                             |
| **PendingNew**      | Lệnh chờ gửi lên Sở   | Lệnh hợp lệ và đang chờ gửi lên hệ thống Sở giao dịch                                     |
| **New**             | Lệnh chờ khớp         | Lệnh được Sở ghi nhận và đang chờ khớp theo điều kiện thị trường                          |
| **PartiallyFilled** | Lệnh đã khớp một phần | Một phần khối lượng đã khớp, phần còn lại tiếp tục chờ khớp                               |
| **Filled**          | Lệnh khớp toàn bộ     | Toàn bộ khối lượng lệnh đã được khớp thành công                                           |
| **PendingReplace**  | Lệnh chờ sửa          | Yêu cầu sửa lệnh được ghi nhận, đang chờ hệ thống/Sở xử lý thay đổi                       |
| **PendingCancel**   | Lệnh chờ hủy          | Yêu cầu hủy lệnh đang chờ hệ thống/Sở xử lý                                               |
| **Canceled**        | Lệnh hủy thành công   | Lệnh đã được hủy thành công và không còn hiệu lực giao dịch                               |
| **Rejected**        | Lệnh bị từ chối       | Lệnh không được chấp nhận do không đáp ứng điều kiện (gói vay, sức mua, hạn mức cho vay…) |
| **Expired**         | Lệnh hết hạn          | Lệnh hết hiệu lực do kết thúc phiên hoặc quá thời gian hiệu lực mà chưa được khớp         |
| **DoneForDay**      | Lệnh đã được giải tỏa | Lệnh kết thúc vòng đời trong ngày giao dịch                                               |

### Đặt lệnh

Dưới đây là các thông tin bắt buộc cần gửi đối với một yêu cầu (Request) đặt lệnh.

- **`marketType`**: Phân loại giao dịch
    - `STOCK`: giao dịch cơ sở
    - `DERIVATIVE`: giao dịch phái sinh
- **`orderCategory`**: Loại lệnh thường trong ngày (NORMAL)
- **`accountNo`:** Tiểu khoản giao dịch, được trả trong response Endpoint <a
  href="https://developers.dnse.com.vn/docs/dnse/get-accounts">Tài khoản giao dịch.</a>
- **`symbol`**: Mã chứng khoán giao dịch
- **`loanPackageId`**: Gói vay giao dịch, xem thêm thông tin về gói vay <a
  href="https://developers.dnse.com.vn/docs/guide/trading-api/dnse_margin#gói-vay-loan-packages">
  tại đây.</a>
- **`side`**: Chiều mua (NB) hoặc bán (NS)
- **`orderType`**: Loại lệnh tương ứng với sàn giao dịch
    - Sàn HOSE: ATO, ATC, LO, MTL
    - Sàn HNX: LO, MTL, MOK, MAK, ATC, PLO
    - Sàn Upcom: LO
- **`quantity`**: Khối lượng đặt

    - Khối lượng đặt không vượt quá khối lượng tối đa có thể mua (`qmaxBuy`)hoặc có thể bán (`qmaxSell`) trên tiểu khoản
      giao dịch, người dùng truy vấn thông tin đối với từng mã chứng khoán qua Endpoint <a
      href="https://developers.dnse.com.vn/docs/dnse/get-ppse">/Sức mua, sức bán.</a>
    - Với giao dịch cơ sở, khối lượng đặt là lô chẵn (100,200,...) hoặc lô lẻ (1,2,..99). Khối lượng lẻ lô (101,102,...)
      là không hợp lệ.
- **`price`**: Giá đặt
    - Nếu loại lệnh là LO, giá đặt phải > 0 và phải nằm trong khoảng giá trần sàn của mã chứng khoán tại phiên giao dịch
      đó.
    - Nếu loại lệnh khác LO, giá đặt truyền lên luôn = 0.

<details>
  <summary>VD Yêu cầu đặt lệnh</summary>

```json lines
{
  "method": "POST",
  "path": "/accounts/orders",
  "query": {
    "marketType": "STOCK",
    "orderCategory": "NORMAL"
  },
  "headers": {
    "x-api-key": "lB58g6iWzyrNx2EhwwQXeYeoAnkzlaXkJWi",
    // APIkey được cấp khi đăng ký dịch vụ
    "x-signature": "fjsdhfryt6aaa6c91a8f88b472c9721fde161e0d89df8c",
    // Chữ ký số theo thuật toán HMAC SHA256
    "trading-token": "7ceef658-9f01-414e-8b3e-faa77bb9061e",
    // Token đặt lệnh         
    "date": "Fri, 16 Jan 2026 07:11:30 +0000"
    // Thời gian tạo yêu cầu (UTC)
  },
  "body": {
    "accountNo": "0003979888",
    // Số tiểu khoản giao dịch
    "symbol": "HPG",
    // Mã chứng khoán đặt lệnh
    "side": "NB",
    // Chiều lệnh giao dịch 
    "orderType": "LO",
    // Loại lệnh giao dịch
    "price": 25950,
    // Giá đặt
    "quantity": 100,
    // Khối lượng đặt
    "loanPackageId": 5757
    // Mã gói vay 
  }
}
```

</details>

Khi lệnh khớp mua, hệ thống hình thành các Deals (hay còn gọi là danh mục tài sản) theo cặp `symbol` - `loanPackage`.
Nếu mua cùng mã nhưng khác gói vay → tạo Deal tách biệt (rủi ro được quản trị riêng).

### Sửa lệnh

**Điều kiện chung:**

- Chỉ được sửa lệnh LO trong phiên giao dịch liên tục và áp dụng cho lệnh ở trạng thái Chờ khớp (New) hoặc Đã khớp một
  phần (PartiallyFilled)
- Giá sửa phải nằm trong biên độ trần sàn của mã chứng khoán vào phiên giao dịch đó.
- Nếu giá hoặc khối lượng sau khi sửa vượt quá sức mua /sức bán cho phép, yêu cầu sửa lệnh sẽ bị từ chối.

**Sửa lệnh cơ sở:**

- Khi sửa lệnh thành công, hệ thống hủy lệnh hiện tại và đặt lại một lệnh mới với thông tin đã chỉnh sửa.
- Cho phép sửa đồng thời giá và khối lượng.
- Thứ tự ưu tiên của lệnh sau khi sửa sẽ được xác định lại theo thời điểm ghi nhận sửa lệnh thành công.

**Sửa lệnh phái sinh:**

- Người dùng chỉ được phép sửa hoặc giá hoặc khối lượng trong một yêu cầu.
- Khối lượng sửa phải lớn hơn khối lượng đã khớp (nếu lệnh đã khớp một phần).
- Nếu khối lượng sửa lớn hơn khối lượng ban đầu, thứ tự ưu tiên của lệnh sẽ được thay đổi.

<details>
  <summary>VD Yêu cầu hủy lệnh</summary>

```json lines
{
  "method": "PUT",
  "path": "/accounts/{account_no}/orders/{order_id}",
  "query": {
    "marketType": "STOCK",
    "orderCategory": "NORMAL"
  },
  "headers": {
    "x-api-key": "lB58g6iWzyrNx2EhwwQXeYeoAnkzlaXkJWi",
    // APIkey được cấp khi đăng ký dịch vụ
    "x-signature": "fjsdhfryt6aaa6c91a8f88b472c9721fde161e0d89df8c",
    // Chữ ký số theo thuật toán HMAC SHA256
    "trading-token": "7ceef658-9f01-414e-8b3e-faa77bb9061e",
    // Token đặt lệnh         
    "date": "Fri, 16 Jan 2026 07:11:30 +0000"
    // Thời gian tạo yêu cầu (UTC)
  },
  "body": {
    "price": 25950,
    // Giá sửa
    "quantity": 100
    // Khối lượng sửa
  }
}
```

</details>
# Market Data WebSocket

Tài liệu này hướng dẫn cách thiết lập kết nối đến DNSE WebSocket để nhận dữ liệu thị trường theo thời gian thực.

----

### Thông tin kết nối chung

- Base URL: `wss://ws-openapi.dnse.com.vn`
- DNSE cung cấp sẵn bộ SDK đã phân tách theo từng loại dữ liệu để khách hàng có thể sẵn sử dụng. Chi tiết xem sample SDKs [tại đây.](https://github.com/dnse-tech/openapi-sdk)
- Định dạng dữ liệu trong SDKs:
  - `msgpack`: Tốc độ xử lý nhanh, tiết kiệm băng thông
  - `json`: Phổ biến và dễ đọc trong quá trình phát triển
- Cơ chế kết nối:
  - Tất cả mã chứng khoán phải ở định dạng chữ in hoa. VD: ACB, HPG, 41I1G2000.
  - Một kết nối WebSocket có hiệu lực tối đa 8 giờ, WebSocket Server sẽ chủ động ngắt kết nối sau thời gian này.
  - Cơ chế để các clients duy trì kết nối ổn định tới WebSocket server DNSE:
    - WebSocket Server sẽ định kỳ gửi 1 PING message sau mỗi 3 phút.
    - Mỗi PING message được gửi từ WebSocket đều yêu cầu nhận PONG message phản hồi từ các client trong thời gian tối đa là 1 phút kể từ lúc Server gửi PING. Nếu quá thời hạn 1 phút này, Server sẽ chủ động ngắt kết nối với Client không đáp ứng.
    - Client được phép gửi PONG message ngay cả khi không nhận được PING từ Server, để chủ động duy trì kết nối. Cách này giúp client giữ kết nối trong các trường hợp PING message bị miss do network issue hoặc các gián đoạn tạm thời khác.

<details>
  <summary>Ví dụ</summary>

- **Case 1: Good interaction**
  - T+0 min   Server → PING
  - T+1     Client → PONG
  - T+3 min   Server → PING
  - T+4     Client → PONG

  Client phản hồi PONG cho mỗi PING từ Server.

  ✅ Connection remains active

- **Case 2: Bad interaction**
  - T+0 min   Server → PING
  - No PONG back from client
  - T+1 min   Server disconnects

  Server đóng kết nối do không nhận được PONG trong khoảng thời gian kết nối định kỳ.

  ❌  Dead Connection

- **Case 3: Client-initiated keepalive**
  - Within every 3 minutes: Client → PING

  Client có thể chủ động gửi PONG message để duy trì kết nối, đặc biệt trong các tình huống:
  - Một số thư viện WS thực hiện auto-handle ping/pong hoặc ẩn các ping frames đối với các app/clients
  - Mobile networks / NATs chủ động ngắt kết nối đối với các idle TCP connections
  - Miss PING frame từ server

  Do đó, việc cho phép clients định kỳ gửi PONG lên để Server xác nhận client vẫn đang hoạt động.

  ✅ Connection keep alive

</details>

### Tổng quan các kênh dữ liệu

| Kênh dữ liệu (Function) | Mô tả (Description) | Phân loại (Type) | Tần suất gửi dữ liệu (Frequency) |
|------------------------|------|------|----------------------|
| [Security Definition](#security-definition) | Thông tin mã chứng khoán (giá trần/sàn, trạng thái), dùng để lấy thông tin biên độ giá đầu ngày | Batch (BOD) | Gửi 1 lần trước giờ giao dịch (≈ 08:00) |
| [Trade](#trade) | Dữ liệu khớp lệnh theo thời gian thực | Real-time | Cập nhật khi có thay đổi dữ liệu trong phiên liên tục |
| [Trade Extra](#trade) | Dữ liệu khớp lệnh nâng cao (chiều mua/bán, giá trung bình) | Real-time | Cập nhật khi có thay đổi dữ liệu trong phiên liên tục |
| [Quote](#quote) | Độ sâu thị trường (giá chào mua/bán) | Real-time | Cập nhật khi có thay đổi dữ liệu trong phiên giao dịch |
| [OHLC](#ohlc) | Dữ liệu nến đang hình thành (Open, High, Low, Close, Volume) | Real-time | Cập nhật khi có giá khớp trong phiên liên tục |
| [OHLC Closed](#ohlc-closed) | Dữ liệu nến đã đóng (Open, High, Low, Close, Volume) | Periodic | Cập nhật khi có dữ liệu đóng nến |
| [Expected Price](#expected-price) | Giá và khối lượng dự kiến khớp lệnh trong phiên ATO/ATC | Real-time | Cập nhật khi có thay đổi dữ liệu trong phiên định kỳ (ATO/ATC) |
| [Market Index](#market-index) | Thông tin chỉ số thị trường (VNINDEX, HNX…) | Periodic | Cập nhật theo chu kỳ 5 giây + tổng hợp cuối ngày |
| [Foreign Investor](#foreign-investor) | Dữ liệu giao dịch của nhà đầu tư nước ngoài theo từng mã | Real-time | Cập nhật khi có thay đổi dữ liệu |

---
### Phân loại dữ liệu (Data Classification)

Để tối ưu hóa việc phát triển ứng dụng, khách hàng cần nắm rõ đặc tính và cơ chế truyền tải của từng kênh dữ liệu:

* **Real-time (Dữ liệu thời gian thực):** Dữ liệu được hệ thống chủ động đẩy xuống (Push) ngay khi có sự kiện phát sinh. Cơ chế này đảm bảo độ trễ thấp nhất cho phía Client.
* **Periodic (Dữ liệu định kỳ):** Dữ liệu chỉ xuất hiện hoặc được cập nhật vào các khoảng thời gian cố định hoặc theo từng giai đoạn (Phase) của phiên giao dịch.
* **Batch Data (Dữ liệu lô):** Dữ liệu Snapshot được xử lý theo đợt lớn.
  * **BOD (Beginning of Day):** Dữ liệu khởi tạo trước giờ giao dịch (VD: Danh mục mã, Giá trần/sàn).
  * **EOD (End of Day):** Dữ liệu tổng hợp sau khi kết thúc ngày giao dịch (VD: Giá đóng cửa chính thức).

---

## Các loại dữ liệu thị trường

### Thông tin mã chứng khoán (Security Definition) {#security-definition}

Cung cấp thông tin về giá trần sàn tham chiếu và trạng thái của mã chứng khoán trong ngày giao dịch. Dữ liệu được hệ thống gửi một lần duy nhất vào 8h sáng đầu ngày giao dịch.

#### Input

- **symbols**: Mã hoặc danh sách mã chứng khoán. Nếu không truyền, hệ thống sẽ trả toàn bộ danh sách mã chứng khoán trên phạm vi thị trường.
- **boardId**: Mã bảng giao dịch (VD: G1 – lô chẵn). Nếu không truyền, hệ thống sẽ lấy tất cả các bảng.

  | boardId         | Mô tả                        |
      |-----------------|------------------------------|
  | G1              | Lô chẵn                      |
  | G3              | Board phiên sau giờ (PLO)    |
  | G4              | Lô lẻ                        |
  | T1              | Thỏa thuận lô chẵn 9h-14h45  |
  | T3              | Thỏa thuận lô chẵn 14h45-15h |
  | T4              | Thỏa thuận lô lẻ 9h-14h45    |
  | T6              | Thỏa thuận lô lẻ 14h45-15h   |

#### Payload

```json lines
{
  "marketId":"DVX",                          //string  // Mã thị trường niêm yết mã chứng khoán
  "boardId":"G1",                            //string  // Mã bảng giao dịch
  "isin":"VN41I1G20009",                     //string  // Mã định danh quốc tế
  "symbol":"41I1G2000",                      //string  // Mã chứng khoán
  "productGrpId":"FIO",                      //string  // Nhóm sản phẩm theo thị trường
  "securityGroupId":"FU",                    //string  // Nhóm chứng khoán
  "basicPrice":2066.6,                       //float   // Giá tham chiếu ngày giao dịch
  "ceilingPrice":2211.2,                     //float   // Giá trần ngày giao dịch
  "floorPrice":1922.0,                       //float   // Giá sàn ngày giao dịch
  "openInterestQuantity":24473,              //integer // Khối lượng hợp đồng phái sinh mở qua đêm
  "securityStatus":"NO_HALT",                //string  // Trạng thái giao dịch của mã chứng khoán
  "symbolAdminStatusCode":"NRM",             //string  // Trạng thái quản lý hành chính mã chứng khoán
  "symbolTradingMethodStatusCode":"NRM",     //string  // Trạng thái cơ chế giao dịch mã chứng khoán
  "symbolTradingSanctionStatusCode":"NRM"    //string  // Tình trạng giao dịch của mã chứng khoán
}
```

### Dữ liệu khớp lệnh (Trade & Trade Extra) {#trade}

DNSE cung cấp dữ liệu khớp lệnh của một mã chứng khoán qua 2 Function khác nhau: Trade và Trade Extra. Trade Extra có thêm một số thông tin mà DNSE tự tổng hợp thêm (mua bán chủ động, giá khớp trung bình), nếu người dùng không có nhu cầu lấy các thông tin này thì có thể dùng function Trade đơn thuần để tối ưu hơn về tốc độ nhận dữ liệu.

#### Input

- **symbols**: Mã hoặc danh sách mã chứng khoán. Nếu không truyền, hệ thống sẽ trả toàn bộ danh sách mã chứng khoán trên phạm vi thị trường.
- **boardId**: Mã bảng giao dịch (VD: G1 – lô chẵn). Nếu không truyền, hệ thống sẽ lấy tất cả các bảng.

#### Payload

```json lines
{
  "marketId"          : "DVX",            //string  // Mã thị trường niêm yết mã chứng khoán
  "boardId"           : "G1",             //string  // Mã bảng giao dịch
  "isin"              : "VN41I1G20009",   //string  // Mã định danh quốc tế
  "symbol"            : "41I1G2000",      //string  // Mã chứng khoán
  "price"             : 1999.8,           //float   // Giá khớp gần nhất
  "quantity"          : 3.0,              //float   // Khối lượng khớp gần nhất
  "totalVolumeTraded" : 84164,            //integer // Tổng khối lượng khớp trong ngày
  "grossTradeAmount"  : 16817.93009,      //float   // Tổng giá trị giao dịch trong ngày
  "highestPrice"      : 2009.6,           //float   // Giá khớp cao nhất trong ngày
  "lowestPrice"       : 1988.8,           //float   // Giá khớp thấp nhất trong ngày
  "openPrice"         : 2005.6,           //float   // Giá mở cửa
  "tradingSessionId"  : "40"              //string  // Mã phiên giao dịch hiện tại
}
```

**VD Payload nhận được Function Trade Extra**

```json lines
{
  "marketId":"DVX",                  //string  // Mã thị trường niêm yết mã chứng khoán
  "boardId":"G1",                    //string  // Mã bảng giao dịch
  "isin":"VN41I1G20009",             //string  // Mã định danh quốc tế
  "symbol":"41I1G2000",              //string  // Mã chứng khoán
  "price":1994.0,                    //float   // Giá khớp gần nhất
  "quantity":1.0,                    //float   // Khối lượng khớp gần nhất
  "side":"UNSPECIFIED",              //string  // Chiều mua, bán chủ động
  "avgPrice":1997.654,               //float   // Giá khớp trung bình
  "totalVolumeTraded":104264,        //integer // Tổng khối lượng khớp trong ngày
  "grossTradeAmount":20828.33542,    //float   // Tổng giá trị giao dịch trong ngày
  "highestPrice":2009.6,             //float   // Giá khớp cao nhất trong ngày
  "lowestPrice":1988.8,              //float   // Giá khớp thấp nhất trong ngày
  "openPrice":2005.6,                //float   // Giá mở cửa
  "tradingSessionId":"40"            //string  // Mã phiên giao dịch hiện tại
}
```

### Độ sâu thị trường (Quote) {#quote}

Cung cấp thông tin giá chào mua và chào bán tốt nhất của mã chứng khoán tại bảng giao dịch cụ thể, cập nhật theo thời gian thực trong phiên giao dịch.
- Sàn HOSE hỗ trợ 3 mức giá.
- Sàn HNX, UPCOM hỗ trợ 10 mức giá.

#### Input

- **symbols**: Mã hoặc danh sách mã chứng khoán. Nếu không truyền, hệ thống sẽ trả toàn bộ danh sách mã chứng khoán trên phạm vi thị trường.
- **boardId**: Mã bảng giao dịch (VD: G1 – lô chẵn). Nếu không truyền, hệ thống sẽ lấy tất cả các bảng.

#### Payload

```json lines
{
  "marketId":"STO",              //string  // Mã thị trường niêm yết mã chứng khoán
  "boardId":"G1",                //string  // Mã bảng giao dịch
  "isin":"VN000000HPG4",          //string  // Mã định danh quốc tế
  "symbol":"HPG",                 //string  // Mã chứng khoán
  "bid":[
    {
      "price":28.3,               //float   // Giá chào mua cao nhất
      "quantity":13330.0          //float   // Tổng khối lượng chào mua tại mức giá này
    },
    {
      "price":28.25,            //float   // Mức giá chào mua tiếp theo
      "quantity":40830.0        //float   // Tổng khối lượng chào mua tại mức giá này
    },
    {
      "price":28.2,             //float   // Mức giá chào mua thấp hơn
      "quantity":50490.0        //float   // Tổng khối lượng chào mua tại mức giá này
    }
  ],
  "offer":[
    {
      "price":28.35,            //float   // Giá chào bán thấp nhất
      "quantity":12660.0        //float   // Tổng khối lượng chào bán tại mức giá tương ứng
    },
    {
      "price":28.4,             //float   // Mức giá chào bán tiếp theo
      "quantity":27530.0        //float   // Tổng khối lượng chào bán tại mức giá tương ứng
    },
    {
      "price":28.45,            //float   // Mức giá chào bán cao hơn
      "quantity":26710.0        //float   // Tổng khối lượng chào bán tại mức giá tương ứng
    }
  ],
  "totalOfferQtty":922230,      //integer // Tổng khối lượng chào bán
  "totalBidQtty":643750         //integer // Tổng khối lượng chào mua
}
```

### OHLC {#ohlc}

OHLC cung cấp thông tin nến (open, high, low, close, volume) theo khung thời gian thực dưới dạng dữ liệu nến đang hình thành và được cập nhật liên tục theo các giao dịch phát sinh. Áp dụng cho Cổ phiếu (stock), Phái sinh (derivative) và Chỉ số thị trường (index) với nhiều khung thời gian (resolution).

#### Input

- **symbol**: Mã hoặc danh sách mã chứng khoán hay chỉ số thị trường
  - Lưu ý: Đối với phái sinh, truyền lên `symbolType` (VD: VN30F1M) thay vì `symbol` (VD: 41I1G4000).
- **resolution**: Khung thời gian của nến (VD: 1, 3, 5, 15, 30, 1H, 1D, 1W)

#### Payload

*Cổ phiếu*

```json lines
{
  "time":1757992500,            //integer   // Thời gian bắt đầu nến
  "open":30.4,                  //float     // Giá mở cửa
  "high":30.4,                  //float     // Giá cao nhất trong nến
  "low":30.25,                  //float     // Giá thấp nhất trong nến
  "close":30.3,                 //float     // Giá đóng cửa
  "volume":1398200,             //integer   // Khối lượng giao dịch
  "symbol":"HPG",               //string    // Mã chứng khoán
  "resolution":"15",            //string    // Khung thời gian nến
  "lastUpdated":1757993014,    //integer   // Thời gian cập nhật lần cuối
  "type":"STOCK"                //string    // Loại nhóm thị trường
}
```

*Phái sinh*

```json lines
{
  "time":1757991840,            //integer   // Thời gian bắt đầu nến
  "open":1881.2,                //float     // Giá mở cửa
  "high":1881.2,                //float     // Giá cao nhất trong nến
  "low":1881.0,                 //float     // Giá thấp nhất trong nến
  "close":1881.2,               //float     // Giá đóng cửa
  "volume":"12",                //integer   // Khối lượng giao dịch
  "symbol":"VN30F1M",           //string    // Mã chứng khoán
  "resolution":"1",             //string    // Khung thời gian nến
  "lastUpdated":1757991844,    //integer   // Thời gian cập nhật lần cuối
  "type":"DERIVATIVE"           //string    // Loại nhóm thị trường
}
```

*Chỉ số index*

```json lines
{
  "time":1757988000,            //integer   // Thời gian bắt đầu nến
  "open":1696.87,               //float     // Giá mở cửa
  "high":1696.87,               //float     // Giá cao nhất trong nến
  "low":1686.02,                //float     // Giá thấp nhất trong nến
  "close":1686.31,              //float     // Giá đóng cửa
  "volume":435873728,           //integer   // Khối lượng giao dịch
  "symbol":"VNINDEX",           //string    // Mã chứng khoán
  "resolution":"1D",            //string    // Khung thời gian nến
  "lastUpdated":1757993070,    //integer   // Thời gian cập nhật lần cuối
  "type":"INDEX"                //string    // Loại nhóm thị trường
}
```

### OHLC đóng nến (OHLC Closed) {#ohlc-closed}

Cung cấp dữ liệu nến đã đóng theo từng khung thời gian (resolution). Dữ liệu chỉ gửi khi kết thúc mỗi khung thời gian và không thay đổi sau đó.

#### Input

- **symbol**: Mã hoặc danh sách mã chứng khoán hay chỉ số thị trường
  - Lưu ý: Đối với phái sinh, truyền lên `symbolType` (VD: VN30F1M) thay vì `symbol` (VD: 41I1G4000).
- **resolution**: Khung thời gian của nến (VD: 1, 3, 5, 15, 30, 1H, 1D, 1W)

#### Payload

```json lines
{
  "time": 1757992500,           //integer   // Thời gian bắt đầu nến
  "open": 30.4,                 //float     // Giá mở cửa
  "high": 30.4,                 //float     // Giá cao nhất trong nến
  "low": 30.25,                 //float     // Giá thấp nhất trong nến
  "close": 30.3,                //float     // Giá đóng cửa
  "volume": 1398200,            //integer   // Khối lượng giao dịch
  "symbol": "HPG",              //string    // Mã chứng khoán
  "resolution": "15",           //string    // Khung thời gian nến
  "lastUpdated": 1757993014,    //integer   // Thời gian cập nhật lần cuối
  "type": "STOCK"               //string    // Loại nhóm thị trường
}
```

### Giá khớp dự kiến (Expected Price) {#expected-price}

Cung cấp thông tin giá đóng cửa, giá khớp dự kiến và khối lượng khớp dự kiến của mã chứng khoán trong các phiên giao dịch khớp lệnh định kỳ ATO và ATC.

#### Input

- **symbols**: Mã hoặc danh sách mã chứng khoán. Nếu không truyền, hệ thống sẽ trả toàn bộ danh sách mã chứng khoán trên phạm vi thị trường.
- **boardId**: Mã bảng giao dịch (VD: G1 – lô chẵn). Nếu không truyền, hệ thống sẽ lấy tất cả các bảng.

#### Payload

```json lines
{
  "marketId":"DVX",                  //string    // Mã thị trường niêm yết mã chứng khoán
  "boardId":"G1",                    //string    // Mã bảng giao dịch
  "symbol":"41I1G1000",              //string    // Mã chứng khoán
  "isin":"VN41I1G10000",             //string    // Mã định danh quốc tế
  "closePrice":28.45,                //float     // Giá đóng cửa
  "expectedTradePrice":28.45,        //float     // Giá dự khớp tại thời điểm xác định
  "expectedTradeQuantity":133780     //integer   // Khối lượng dự khớp tại thời điểm xác định
}
```

### Chỉ số thị trường (Market Index) {#market-index}

Cung cấp thông tin chỉ số thị trường bao gồm giá trị chỉ số, mức thay đổi, độ rộng thị trường (số mã tăng/giảm/đi ngang) và thanh khoản. Dữ liệu được cập nhật liên tục trong phiên giao dịch.

#### Input

- **marketIndex**: Tên chỉ số thị trường

  | Giá trị | Mô tả |
      |--------|------|
  | HNX30 | Chỉ số Top 30 cổ phiếu sàn HNX |
  | VN30 | Chỉ số Top 30 cổ phiếu sàn HOSE |
  | HNX | Chỉ số sàn HNX |
  | VNXALLSHARE | Chỉ số các cổ phiếu chọn lọc sàn HOSE |
  | UPCOM | Chỉ số sàn UPCOM |
  | VNDIVIDEND | Chỉ số nhóm cổ phiếu có tỷ suất cổ tức tăng trưởng |
  | VNINDEX | Chỉ số sàn HOSE |
  | VN50GROWTH | Chỉ số nhóm 50 cổ phiếu tăng trưởng sàn HOSE |
  | VN100 | Chỉ số Top 100 cổ phiếu sàn HOSE |
  | VNMITECH | Chỉ số nhóm cổ phiếu công nghệ |


#### Payload

```json lines
{
  "indexName":"VNINDEX",                           //string  // Tên chỉ số thị trường
  "changedRatio":0.41,                             //float   // Tỷ lệ thay đổi (%)
  "changedValue":6.84,                             //float   // Giá trị thay đổi so với tham chiếu
  "fluctuationSteadinessIssueCount":67,            //integer // Số lượng mã có giá không đổi
  "fluctuationDownIssueCount":158,                 //integer // Số lượng mã có giá giảm
  "fluctuationUpIssueCount":144,                   //integer // Số lượng mã có giá tăng
  "fluctuationLowerLimitIssueCount":null,          //integer // Số lượng mã giảm sàn
  "fluctuationUpperLimitIssueCount":7,             //integer // Số lượng mã tăng trần
  "fluctuationDownIssueVolume":220246500,          //integer // Tổng khối lượng giao dịch các mã có giá giảm
  "fluctuationUpIssueVolume":446927155,            //integer // Tổng khối lượng giao dịch các mã có giá tăng 
  "fluctuationSteadinessIssueVolume":39390038,     //integer // Tổng khối lượng giao dịch các mã có giá không đổi
  "currencyCode":"VND",                            //string  // Đơn vị tiền tệ
  "indexTypeCode":"001",                           //string  // Mã loại chỉ số
  "lowestValueIndexes":1662.05,                    //float   // Giá thấp nhất trong phiên
  "highestValueIndexes":1677.83,                   //float   // Giá cao nhất trong phiên
  "priorValueIndexes":1662.54,                     //float   // Giá trị tham chiếu
  "valueIndexes":1669.38,                          //float   // Giá trị hiện tại của chỉ số
  "contauctAccTrdVal":15609.88011093,              //float   // Tổng giá trị giao dịch theo phương thức khớp lệnh
  "contauctAccTrdVol":606182599,                   //integer // Tổng khối lượng giao dịch theo phương thức khớp lệnh
  "blkTrdAccTrdVal":3040.58723198,                 //float   // Tổng giá trị giao dịch theo phương thức thỏa thuận
  "blkTrdAccTrdVol":100381155,                     //integer // Tổng khối lượng giao dịch theo phương thức thỏa thuận
  "grossTradeAmount":18650.46734291,               //float   // Tổng giá trị giao dịch trong ngày
  "totalVolumeTraded":706563754,                   //integer // Tổng khối lượng giao dịch trong ngày
  "marketIndexClass":1,                            //integer // Phân loại chỉ số
  "marketId":"STO",                                //string  // Mã thị trường
  "tradingSessionId":"40",                         //string  // Mã phiên giao dịch hiện tại
  "transactTime":"2026-03-31 07:05:05"             //string  // Thời điểm cập nhật
}
```

### Giao dịch nhà đầu tư nước ngoài (Foreign Investor) {#foreign-investor}

Cung cấp dữ liệu giao dịch của nhà đầu tư nước ngoài theo từng mã chứng khoán, bao gồm khối lượng và giá trị mua/bán, tổng lũy kế trong ngày và room còn lại. Dữ liệu được cập nhật trong phiên giao dịch khi có thay đổi.

#### Input

- **symbols**: Mã hoặc danh sách mã chứng khoán. Nếu không truyền, hệ thống sẽ trả toàn bộ danh sách mã chứng khoán trên phạm vi thị trường.
- **boardId**: Mã bảng giao dịch (VD: G1 – lô chẵn). Nếu không truyền, hệ thống sẽ lấy tất cả các bảng.

#### Payload

```json lines
{
  "marketId":"STO",                            //string  // Mã thị trường
  "boardId":"G1",                              //string  // Mã bảng giao dịch
  "tradingSessionId":"40",                     //string  // Mã phiên giao dịch hiện tại
  "symbol":"FPT",                              //string  // Mã chứng khoán
  "transactTime":"035200011",                  //string  // Thời điểm cập nhật
  "foreignInvestorTypeCode":"10",              //string  // Loại nhà đầu tư nước ngoài
  "sellVolume":1449400,                        //integer // Khối lượng bán trong ngày theo bảng giao dịch
  "sellTradedAmount":109774810000,             //float   // Giá trị bán trong ngày theo bảng giao dịch
  "buyVolume":608300,                          //integer // Khối lượng mua trong ngày theo bảng giao dịch
  "buyTradedAmount":46040960000,               //float   // Giá trị mua trong ngày theo bảng giao dịch
  "totalSellVolume":1449716,                   //integer // Tổng khối lượng bán trong ngày
  "totalSellTradedAmount":109798718600,        //float   // Tổng giá trị bán trong ngày
  "totalBuyVolume":608370,                     //integer // Tổng khối lượng mua trong ngày
  "totalBuyTradedAmount":46046280000,          //float   // Tổng giá trị mua trong ngày
  "foreignerOrderLimitQuantity":341884580,     //integer // Tổng room sở hữu tối đa của NĐT nước ngoài
  "foreignerBuyPossibleQuantity":351900000     //integer // Room còn lại có thể mua
}
```
---
sidebar_position: 1
---

# Enums Dữ liệu thị trường

### boardId

*Định danh bảng giao dịch*

| Enums (BoardID) | Kiểu dữ liệu | Mô tả                        |
|-----------------|--------------|------------------------------|
| UNSPECIFIED     | string       | Không xác định               |
| AL              | string       | Tất cả bảng                  |
| G1              | string       | Lô chẵn                      |
| G3              | string       | Board phiên sau giờ (PLO)    |
| G4              | string       | Lô lẻ                        |
| T1              | string       | Thỏa thuận lô chẵn 9h-14h45  |
| T3              | string       | Thỏa thuận lô chẵn 14h45-15h |
| T4              | string       | Thỏa thuận lô lẻ 9h-14h45    |
| T6              | string       | Thỏa thuận lô lẻ 14h45-15h   |

---

### indexTypeCode

*Loại chỉ số thị trường*

| Enums (IndexTypeCode) | Kiểu dữ liệu | Mô tả                                                           |
|-----------------------|--------------|-----------------------------------------------------------------|
| 001                   | string       | VNINDEX (Chỉ số sàn HOSE)                                       |
| 002                   | string       | HNX (Chỉ số sàn HNX)                                            |
| 100                   | string       | HNX30 (Top 30 cổ phiếu sàn HNX)                                 |
| 101                   | string       | VN30 (Top 30 cổ phiếu sàn HOSE)                                 |
| 104                   | string       | VN100 (Top 100 cổ phiếu sàn HOSE)                               |
| 151                   | string       | VNXALLSHARE (Chỉ số các cổ phiếu chọn lọc sàn HOSE)             |
| 301                   | string       | UPCOM (Chỉ số sàn UPCOM)                                        |
| 504                   | string       | VNMITECH (Chỉ số nhóm cổ phiếu công nghệ)                       |
| 505                   | string       | VN50GROWTH (Chỉ số nhóm 50 cổ phiếu tăng trưởng sàn HOSE)       |
| 506                   | string       | VNDIVIDEND (Chỉ số nhóm cổ phiếu có tỷ suất cổ tức tăng trưởng) |

---

### marketId

*Mã thị trường*

| Enums (MarketID) | Kiểu dữ liệu | Mô tả                           |
|------------------|--------------|---------------------------------|
| UNSPECIFIED      | string       | Không xác định                  |
| DVX              | string       | Phái sinh sàn HNX               |
| HCX              | string       | Trái phiếu doanh nghiệp sàn HNX |
| STO              | string       | Cổ phiếu sàn HOSE               |
| STX              | string       | Cổ phiếu sàn HNX                |
| UPX              | string       | Cổ phiếu sàn Upcom              |

---

### marketIndex (IndexName)

*Tên chỉ số thị trường*

| Enums (MarketIndex) | Kiểu dữ liệu | Mô tả                                              |
|---------------------|--------------|----------------------------------------------------|
| VNINDEX             | string       | Chỉ số sàn HOSE                                    |
| HNX                 | string       | Chỉ số sàn HNX                                     |
| HNX30               | string       | Chỉ số Top 30 cổ phiếu sàn HNX                     |
| VN30                | string       | Chỉ số Top 30 cổ phiếu sàn HOSE                    |
| VN100               | string       | Chỉ số Top 100 cổ phiếu sàn HOSE                   |
| VNXALLSHARE         | string       | Chỉ số các cổ phiếu chọn lọc sàn HOSE              |
| UPCOM               | string       | Chỉ số sàn UPCOM                                   |
| VNMITECH            | string       | Chỉ số nhóm cổ phiếu công nghệ                     |
| VN50GROWTH          | string       | Chỉ số nhóm 50 cổ phiếu tăng trưởng sàn HOSE       |
| VNDIVIDEND          | string       | Chỉ số nhóm cổ phiếu có tỷ suất cổ tức tăng trưởng |

---

### productGrpId

*Nhóm sản phẩm theo thị trường*

| Enums (ProductGrpID) | Kiểu dữ liệu | Mô tả                         |
|----------------------|--------------|-------------------------------|
| UNSPECIFIED          | string       | Không xác định                |
| FBX                  | string       | Hợp đồng tương lai Trái phiếu |
| FIO                  | string       | Hợp đồng tương lai Chỉ số     |
| HCX                  | string       | Trái phiếu Doanh nghiệp HNX   |
| STO                  | string       | Cổ phiếu sàn HOSE             |
| STX                  | string       | Cổ phiếu sàn HNX              |
| UPX                  | string       | Cổ phiếu sàn Upcom            |

---

### resolution

*Khung thời gian nến*

| Enums (Resolution) | Kiểu dữ liệu | Mô tả   |
|--------------------|--------------|---------|
| 1                  | string       | 1 phút  |
| 3                  | string       | 3 phút  |
| 5                  | string       | 5 phút  |
| 15                 | string       | 15 phút |
| 30                 | string       | 30 phút |
| 1H                 | string       | 1 giờ   |
| 1D                 | string       | 1 ngày  |
| 1W                 | string       | 1 tuần  |

---

### securityGroupId

*Định danh nhóm chứng khoán*

| Enums (SecurityGroupID) | Kiểu dữ liệu | Mô tả                   |
|-------------------------|--------------|-------------------------|
| UNSPECIFIED             | string       | Không xác định          |
| BS                      | string       | Trái phiếu doanh nghiệp |
| EF                      | string       | Quỹ ETF                 |
| EW                      | string       | Chứng quyền             |
| FU                      | string       | Hợp đồng tương lai      |
| SR                      | string       | Quyền mua               |
| ST                      | string       | Cổ phiếu                |

---

### securityStatus

*Trạng thái của mã chứng khoán*

| Enums (SecurityStatus) | Kiểu dữ liệu | Mô tả                 |
|------------------------|--------------|-----------------------|
| HALT                   | string       | Ngừng giao dịch       |
| NO_HALT                | string       | Không ngừng giao dịch |

---

### side

*Chiều xác định mua/bán chủ động*

| Enums (Side) | Kiểu dữ liệu | Mô tả          |
|--------------|--------------|----------------|
| UNSPECIFIED  | string       | Không xác định |
| BUY          | string       | Mua chủ động   |
| SELL         | string       | Bán chủ động   |

---

### symbolAdminStatusCode

*Trạng thái quản lý hành chính mã chứng khoán*

| Enums (SymbolAdminStatusCode) | Kiểu dữ liệu | Mô tả                          |
|-------------------------------|--------------|--------------------------------|
| UNSPECIFIED                   | string       | Không xác định                 |
| CR                            | string       | Kiểm soát và hạn chế giao dịch |
| CTR                           | string       | Kiểm soát                      |
| NRM                           | string       | Bình thường                    |
| RES                           | string       | Hạn chế giao dịch              |
| WFR                           | string       | Cảnh báo do vi phạm BCTC       |
| WID                           | string       | Cảnh báo do vi phạm CBTT       |
| WOV                           | string       | Cảnh báo vi phạm khác          |

---

### symbolTradingMethodStatusCode

*Trạng thái cơ chế giao dịch mã chứng khoán*

| Enums (SymbolTradingMethodStatusCode) | Kiểu dữ liệu | Mô tả                         |
|---------------------------------------|--------------|-------------------------------|
| UNSPECIFIED                           | string       | Không xác định                |
| NRM                                   | string       | Bình thường                   |
| NWE                                   | string       | Niêm yết mới biên độ đặc biệt |
| NWN                                   | string       | Niêm yết mới biên độ thường   |
| SLS                                   | string       | Giao dịch đặc biệt sau halt   |
| SNE                                   | string       | Giao dịch đặc biệt            |

---

### symbolTradingSanctionStatusCode

*Tình trạng giao dịch của mã chứng khoán*

| Enums (SymbolTradingSanctionStatusCode) | Kiểu dữ liệu | Mô tả                      |
|-----------------------------------------|--------------|----------------------------|
| UNSPECIFIED                             | string       | Không xác định             |
| NRM                                     | string       | Bình thường                |
| SUS                                     | string       | Tạm ngừng                  |
| DTL                                     | string       | Hủy niêm yết chuyển sàn    |
| TFR                                     | string       | Ngưng giao dịch do hạn chế |

---

### tradingSessionId

*Mã phiên giao dịch (theo từng mã)*

| Enums (TradingSessionID) | Kiểu dữ liệu | Mô tả          |
|--------------------------|--------------|----------------|
| UNSPECIFIED              | string       | Không xác định |
| 10                       | string       | ATO            |
| 30                       | string       | ATC            |
| 40                       | string       | Phiên liên tục |
| 80                       | string       | PCA mã halt    |
| 99                       | string       | Đóng bảng      |

---

### type

*Loại nhóm thị trường*

| Enums (Type) | Kiểu dữ liệu | Mô tả     |
|--------------|--------------|-----------|
| STOCK        | string       | Cổ phiếu  |
| DERIVATIVE   | string       | Phái sinh |
| INDEX        | string       | Chỉ số    |
---
sidebar_position: 2
---


# Rate Limits

DNSE OpenAPI áp dụng rate limit theo từng APIKey và từng Endpoint.

Rate limit được định nghĩa bởi:

- Rate: tổng số request trong 1 giờ
- Quota: tổng số request trong 24 giờ (1 ngày)

### Normal Rate Limits

## Rate Limits

| Tên API                         | Endpoint                                                                                                                                       | Rate / giờ | Quota / ngày |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------|--------------|
| Thông tin tiền                  | <a href="https://developers.dnse.com.vn/docs/dnse/get-account-balances">/Get Account Balance</a>                     | 10,000     | 100,000      |
| Tài khoản giao dịch             | <a href="https://developers.dnse.com.vn/docs/dnse/get-accounts">/Get Accounts</a>                                    | 100        | 1,000        |
| Danh sách gói vay               | <a href="https://developers.dnse.com.vn/docs/dnse/get-loan-packages">/Get Loan Packages</a>                          | 1000       | 10,000       |
| Sức mua, sức bán                | <a href="https://developers.dnse.com.vn/docs/dnse/get-ppse">/Get PPSE</a>                                            | 10,000     | 100,000      |
| Sổ lệnh                         | <a href="https://developers.dnse.com.vn/docs/dnse/get-orders">/Get Orders</a>                                        | 10,000     | 100,000      |
| Lịch sử lệnh                    | <a href="https://developers.dnse.com.vn/docs/dnse/get-orders-history">/Get Order History</a>                         | 10,000     | 100,000      |
| Chi tiết lệnh theo ID           | <a href="https://developers.dnse.com.vn/docs/dnse/get-order-detail">/Get Order Detail</a>                            | 10,000     | 100,000      |
| Vị thế nắm giữ                  | <a href="https://developers.dnse.com.vn/docs/dnse/get-accounts-account-no-positions">/Get Positions</a>              | 10,000     | 100,000      |
| Chi tiết vị thế theo ID         | <a href="https://developers.dnse.com.vn/docs/dnse/get-accounts-positions-position-id">/Get Position Detail by ID</a> | 10,000     | 100,000      |
| Gửi Email OTP                   | <a href="https://developers.dnse.com.vn/docs/dnse/send-email-otp">/Send Email OTP</a>                                | 100        | 1,000        |
| Xác thực OTP                    | <a href="https://developers.dnse.com.vn/docs/dnse/2-fa-verification">/Create Trading Token</a>                       | 100        | 1,000        |
| Đặt lệnh                        | <a href="https://developers.dnse.com.vn/docs/dnse/place-order">/Place Order</a>                                      | 50,000     | 100,000      |
| Sửa lệnh                        | <a href="https://developers.dnse.com.vn/docs/dnse/replace-order">/Replace Order</a>                                  | 50,000     | 100,000      |
| Hủy lệnh                        | <a href="https://developers.dnse.com.vn/docs/dnse/cancel-order">/Cancel Order</a>                                    | 50,000     | 100,000      |
| Đóng vị thế                     | <a href="https://developers.dnse.com.vn/docs/dnse/post-accounts-positions-position-id-close">/Close Position</a>     | 50,000     | 100,000      |
| Thông tin giao dịch chứng khoán | <a href="https://developers.dnse.com.vn/docs/dnse/get-secdef">/Get Security Definition</a>                           | 1,000      | 10,000       |
| Chi tiết mã chứng khoán         | <a href="https://developers.dnse.com.vn/docs/dnse/get-instruments">/Get Instruments</a>                              | 1,000      | 10,000       |
| Lịch sử OHLC                    | <a href="https://developers.dnse.com.vn/docs/dnse/get-ohlc-history">/Get OHLC</a>                                    | 1,000      | 10,000       |
| Lịch sử khớp lệnh               | <a href="https://developers.dnse.com.vn/docs/dnse/get-price-symbol-trades">/Get Trades</a>                           | 1,000      | 10,000       |
| Dữ liệu khớp gần nhất           | <a href="https://developers.dnse.com.vn/docs/dnse/get-price-symbol-trades-latest">/Get Latest Trades</a>             | 1,000      | 10,000       |

### Notes

DNSE có thể cung cấp thông tin về giới hạn sử dụng API thông qua các header trong response:

| Header                | Ý nghĩa                                  |
|-----------------------|------------------------------------------|
| X-RateLimit-Limit     | Số lượng request tối đa được phép        |
| X-RateLimit-Remaining | Số request còn lại trong chu kỳ hiện tại |
| X-RateLimit-Reset     | Thời điểm giới hạn được làm mới          |

Khi vượt quá giới hạn, hệ thống sẽ trả về **HTTP 429 (Too Many Requests)**

```json lines
429
Too Many Requests
{
  "error": "Rate Limit Exceeded"
}
```

### Khuyến nghị

- Phân bổ tần suất gọi API hợp lý trong từng khoảng thời gian
- Hạn chế gọi lặp lại các dữ liệu ít thay đổi bằng cách cache
- Ưu tiên sử dụng các API hỗ trợ xử lý nhiều dữ liệu trong một lần gọi (nếu có)
- Theo dõi số lượng request còn lại để chủ động điều chỉnh hành vi gọi API

***
---

sidebar_position: 1

---



# Trading SDKs



---

DNSE cung cấp và hỗ trợ [sample SDKs](https://github.com/dnse-tech/openapi-sdk) với đa dạng ngôn ngữ. Người dùng có thể tải xuống và ứng dụng ngay vào các scripts hoặc luồng giao dịch của mình.



- SDK Python: https://github.com/dnse-tech/openapi-sdk/tree/main/python

- SDK Javascript: https://github.com/dnse-tech/openapi-sdk/tree/main/javascript



Trang này cung cấp các ví dụ SDKs minh hoạ cách thiết lập và thực hiện các yêu cầu (Request) cơ bản với OpenAPI, bao gồm xác thực, truy vấn thông tin tài khoản và thực hiện giao dịch.



---

### Thông tin tài khoản



#### Tài khoản giao dịch

Lấy danh sách tất cả các tiểu khoản giao dịch (sub-account) thuộc quyền quản lý của tài khoản tương ứng với API Key.



<details>

  <summary>SDK get_accounts</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.get_accounts(dry_run=False)

print(status, body)

```

</details>



#### Thông tin tiền



Truy vấn thông tin tài sản cơ sở và phái sinh trên tiểu khoản giao dịch.

<details>

  <summary>SDK get_balances</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)



status, body = client.get_balances(

    account_no="0003979888",        // Số tiểu khoản giao dịch

    dry_run=False

)

print(status, body)

```

</details>



#### Danh sách gói vay



Lấy mã gói vay để đặt lệnh giao dịch tùy theo từng mã chứng khoán. Dựa vào response trả về, người dùng có thể chọn gói tiền mặt hoặc gói vay margin theo nhu cầu.



<details>

  <summary>SDK get_loan_packages</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)



status, body = client.get_loan_packages(

    account_no="0003979888",        // Số tiểu khoản giao dịch

    market_type="STOCK",     // STOCK (gói vay cơ sở) hoặc DERIVATIVE (gói vay phái sinh)

    symbol="HPG",       // Mã chứng khoán

    dry_run=False,

)

print(status, body)

```

</details>



#### Sức mua, sức bán



Truy vấn thông tin sức mua và sức bán của tài khoản theo mã chứng khoán và gói vay để kiểm tra khả năng đặt lệnh trước khi giao dịch.



<details>

  <summary>SDK get_ppse</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)



status, body = client.get_ppse(

    account_no="0003979888",

    market_type="STOCK",     // STOCK (gói vay cơ sở) hoặc DERIVATIVE (gói vay phái sinh)

    symbol="HPG",

    price=26000,

    loan_package_id=1775,

    dry_run=False,

)



print(status, body)

```

</details>



#### Sổ lệnh



Truy vấn sổ lệnh giao dịch trong ngày theo từng thị trường cơ sở hoặc phái sinh, bao gồm trạng thái và thông tin xử lý của từng lệnh.



<details>

  <summary>SDK get_orders</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.get_orders(

    account_no="0003979888",

    market_type="STOCK",     // STOCK (gói vay cơ sở) hoặc DERIVATIVE (gói vay phái sinh)

    orderCategory="NORMAL",

    dry_run=False,

)

print(status, body)

```

</details>



#### Chi tiết lệnh theo ID



Truy vấn thông tin chi tiết của một lệnh giao dịch cụ thể theo `orderId`, bao gồm trạng thái, khối lượng, giá và các thông tin liên quan trong quá trình khớp lệnh.



<details>

  <summary>SDK get_order_detail</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.get_order_detail(

    account_no="0003979888",     // Số tiểu khoản giao dịch

    market_type="STOCK",     // STOCK (gói vay cơ sở) hoặc DERIVATIVE (gói vay phái sinh)

    order_id="123",         // ID lệnh

    dry_run=False,

)

print(status, body)

```

</details>



#### Vị thế nắm giữ



Truy vấn danh sách các vị thế đang nắm giữ trên tài khoản, bao gồm thông tin khối lượng, giá vốn, lãi/lỗ dự tính và các thông tin khác.



<details>

  <summary>SDK get_positions</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.get_positions(

    account_no="0003979888",

    market_type="STOCK",     // STOCK (vị thế cơ sở) hoặc DERIVATIVE (vị thế phái sinh)

    dry_run=False,

)

print(status, body)

```

</details>



#### Chi tiết vị thế theo ID



Truy vấn thông tin chi tiết của một vị thế cơ sở hoặc phái sinh đang mở theo `positionId`



<details>

  <summary>SDK get_position_by_id</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.get_position_by_id(

    position_id="189",

    market_type="STOCK",

    dry_run=False,    

)

print(status, body)

```

</details>



#### Lịch sử lệnh đã đặt



Truy vấn thông tin danh sách lệnh đã đặt trong một khoảng thời gian nhất định. Thời gian tra cứu tối đa trong vòng 1 năm kể từ ngày hiện tại.



<details>

  <summary>SDK get_order_history</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.get_order_history(

    account_no="0003979888",

    market_type="STOCK",     // STOCK (cơ sở) hoặc DERIVATIVE (phái sinh)

    from_date="2026-03-03",

    to_date="2026-02-01",

    dry_run=False,

)

print(status, body)

```

</details>



### Giao dịch



#### Lấy Email OTP (optional)



Gửi yêu cầu nhận mã OTP qua email, chỉ áp dụng cho các tài khoản đang sử dụng phương thức xác thực lớp thứ hai là Email OTP.



<details>

  <summary>SDK send_email_OTP</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.send_email_otp(dry_run=False)

print(status, body)

```

</details>



Trường hợp không sử dụng phương thức Email OTP, người dùng có thể sử dụng Smart OTP, hướng dẫn <a href="https://developers.dnse.com.vn/docs/guide/intro/authentication#phương-thức-otp">tại đây</a>



#### Xác thực OTP lấy Trading Token



Xác thực mã OTP theo phương thức đã đăng ký để lấy Trading Toke. Đây là thông tin bắt buộc để xác thực quyền giao dịch, có hiệu lực trong 8 tiếng.



<details>

  <summary>SDK create_trading_token</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.create_trading_token(

    otp_type="email_otp",       // Phương thức xác thực đã đăng ký (email_otp hoặc smart_otp)

    passcode="976981",      // Mã OTP tương ứng phương thức

    dry_run=False,

)

print(status, body)

```

</details>



#### Đặt lệnh



Gửi yêu cầu đặt lệnh giao dịch cơ sở hoặc phái sinh trên tài khoản.



<details>

  <summary>SDK post_order</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

payload = {

    "accountNo": "0003979888",      // Số tiểu khoản giao dịch

    "symbol": "HPG",               // Mã chứng khoán đặt lệnh

    "side": "NB",                  // NB (mua) hoặc NS (bán)

    "orderType": "LO",             // Loại lệnh theo từng sàn 

    "price": 25950,                // Giá đặt 

    "quantity": 100,               // Khối lượng đặt

    "loanPackageId": 5757

}

status, body = client.post_order(

    market_type="STOCK",           // STOCK (gói vay cơ sở) hoặc DERIVATIVE (gói vay phái sinh)

    payload=payload,

    trading_token="2bccbdf1-32f0-4ea9-9234-b8977baebabc",   // Trading Token lấy từ response POST /create_trading_token

    order_category="NORMAL",

    dry_run=False,

)

print(status, body)

```

</details>



#### Hủy lệnh



Gửi yêu cầu hủy lệnh đã đặt theo `order_id`.



<details>

  <summary>SDK cancel_order</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.cancel_order(

    account_no="0003979888",     // Số tiểu khoản giao dịch

    market_type="STOCK",     // STOCK (gói vay cơ sở) hoặc DERIVATIVE (gói vay phái sinh)

    order_id="123",         // ID lệnh

    trading_token="2bccbdf1-32f0-4ea9-9234-b8977baebabc",

    order_category="NORMAL",

    dry_run=False,

)

print(status, body)

```

</details>



#### Sửa lệnh



Gửi yêu cầu sửa lệnh đã đặt theo `order_id`.



- Với lệnh cơ sở, khi sửa lệnh thành công đồng nghĩa hủy lệnh cũ và đặt lại lệnh mới, nên người dùng có thể sửa đồng thời giá và khối lượng.

- Với lệnh phái sinh, người dùng chỉ có thể sửa hoặc giá hoặc khối lượng. Khối lượng sửa phải lớn hơn khối lượng đã khớp (nếu có).



<details>

  <summary>SDK put_order</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

payload = {

    "price": 12500,

    "quantity": 100,

}

status, body = client.replace_order(

    account_no="0003979888",     // Số tiểu khoản giao dịch

    market_type="STOCK",     // STOCK (gói vay cơ sở) hoặc DERIVATIVE (gói vay phái sinh)

    order_id="123",         // ID lệnh

    trading_token="2bccbdf1-32f0-4ea9-9234-b8977baebabc",

    order_category="NORMAL",

    dry_run=False,

)

print(status, body)

```

</details>



#### Đóng vị thế



Gửi yêu cầu đóng vị thế đang mở của phái sinh theo `position_id`.

Đóng vị thế là lệnh đặt ngược chiều với vị thế đang mở, loại lệnh LO với giá đặt là giá trần/sàn của mã tương ứng và khối lượng đặt bằng khối lượng mở của vị thế.



<details>

  <summary>SDK cancel_order</summary>



```python

from dnse import DNSEClient



client = DNSEClient(

    api_key="your_api_key",

    api_secret="your_api_secret",

    base_url="https://openapi.dnse.com.vn",

)

status, body = client.close_position(

    position_id="389",

    market_type="DERIVATIVE",

    payload=payload,

    trading_token="replace-with-trading-token",

    dry_run=False,

)

print(status, body)

```

</details>

---

sidebar_position: 2

---

# Market Data SDKs



---



DNSE cung cấp [Market Data SDKs](https://github.com/dnse-tech/openapi-sdk) với đa dạng ngôn ngữ và xây dựng sẵn các function phân tách theo từng loại dữ liệu thị trường để khách hàng có thể sẵn sàng sử dụng được ngay.



- SDK Python: https://github.com/dnse-tech/openapi-sdk/tree/main/python/websocket-marketdata



---



### Thiết lập kết nối WebSocket

Thiết lập kết nối tới Websocket server của DNSE để nhận dữ liệu thị trường, khách hàng cần khai báo thông tin API Key và API Secret trong SDKs.



<details>

  <summary>Connect to WebSocket</summary>



```python

import asyncio

from trading_websocket import TradingClient



async def main():

    encoding = "msgpack"  # hoặc "json"

    client = TradingClient(

        api_key="your_api_key",

        api_secret="your_api_secret",

        base_url="wss://ws-openapi.dnse.com.vn",

        encoding=encoding,

    )



    await client.connect()

    print("Connected")



asyncio.run(main())

```

</details>



#### Thông tin mã chứng khoán (Security Definition)

Cung cấp thông tin về giá trần sàn tham chiếu và trạng thái của mã chứng khoán trong ngày giao dịch. Dữ liệu được hệ thống gửi một lần duy nhất vào 8h sáng đầu ngày giao dịch.



<details>

  <summary>SDK Security Definition</summary>



```python

from trading_websocket.models import SecurityDefinition



def handle_security_definition(sec_def: SecurityDefinition):    



await client.subscribe_sec_def(

    symbols=["ACB", "41I1G2000"],   // Mã chứng khoán nhận thông tin

    on_sec_def=handle_security_definition, 

    encoding=encoding

)

```

</details>



#### Dữ liệu khớp lệnh (Trade)



Phân phối Realtime dữ liệu khớp lệnh (tick) của các mã chứng khoán đã đăng ký.



<details>

  <summary>SDK Trade</summary>



```python

from trading_websocket.models import Trade



def handle_trade(trade: Trade):    



await client.subscribe_trades(

    symbols=["ACB", "41I1G2000"],   // Mã chứng khoán nhận thông tin

    on_trade=handle_trade, 

    encoding=encoding

)

```



</details>



#### Dữ liệu khớp lệnh mở rộng (Trade Extra)



Phân phối Realtime dữ liệu khớp lệnh (tick) và bổ sung thêm một số thông tin do DNSE tự tổng hợp (mua bán chủ động, giá khớp trung bình). Trong trường hợp người dùng không sử dụng đến các thông tin này thì nên dùng function Trade đơn thuần để tối ưu hơn về tốc độ nhận dữ liệu.



<details>

  <summary>SDK Trade Extra</summary>



```python

from trading_websocket.models import TradeExtra



def handle_trade_extra(trade: TradeExtra):



await client.subscribe_trade_extra(

    symbols=["ACB", "41I1G2000"],   // Mã chứng khoán nhận thông tin

    on_trade_extra=handle_trade_extra,

    encoding=encoding,

)

```

</details>



#### Độ sâu thị trường (Quote)



Phân phối Realtime thông tin về các mức giá chào mua và chào bán tốt nhất của mã chứng khoán (bid-ask).

Dữ liệu phản ánh trạng thái cung – cầu tại thời điểm hiện tại.



<details>

  <summary>SDK quote</summary>



```python

from trading_websocket.models import Quote



def handle_quote(quote: Quote):



await client.subscribe_quotes(

    symbols=["ACB", "41I1G2000"],   // Mã chứng khoán nhận thông tin

    on_quote=handle_quote,

    encoding=encoding,

)

```

</details>



#### OHLC



Phân phối thông tin nến theo khung thời gian thực (open, high, low, close, volume) cho Cổ phiếu (stock), Phái sinh (derivative) và Chỉ số thị trường (index). Áp dụng cho nhiều khung thời gian (resolution).



<details>

  <summary>SDK OHLC</summary>



```python

from trading_websocket.models import OHLC



def handle_ohlc(ohlc: Ohlc):



# internal 1 3 5 15 30 1H 1D 1W

await client.subscribe_ohlc(

    symbols=["HPG", "41I1G2000"],

    resolution="1",

    on_bar=handle_bar,

    encoding=encoding,

)

```

</details>



#### Giá khớp dự kiến (Expected Price)



Phân phối thông tin giá đóng cửa (kết thúc phiên), giá khớp dự kiến và khối lượng khớp dự kiến của mã chứng khoán trong các phiên giao dịch khớp lệnh định kỳ ATO và ATC.



<details>

  <summary>SDK Expected Price</summary>



```python

from trading_websocket.models import ExpectedPrice



def handle_expected_price(expected_price: ExpectedPrice):



await client.subscribe_expected_price(

    symbols=["HPG", "41I1G2000"],

    on_expected_price=handle_expected_price,

    encoding=encoding

)

```

</details>



#### Chỉ số thị trường (Market Index)



Cung cấp thông tin chỉ số thị trường bao gồm giá trị chỉ số, mức thay đổi, độ rộng thị trường (số mã tăng/giảm/đi ngang) và thanh khoản. Dữ liệu được cập nhật liên tục trong phiên giao dịch.



<details>

  <summary>SDK Market Index</summary>



```python

from trading_websocket.models import MarketIndex



def handle_market_index(data: MarketIndex):



await client.subscribe_market_index(market_index='HNX', on_market_index=handle_market_index, encoding=encoding)

```

</details>



#### Giao dịch nhà đầu tư nước ngoài (Foreign Investor)



Cung cấp dữ liệu giao dịch của nhà đầu tư nước ngoài theo từng mã chứng khoán, bao gồm khối lượng và giá trị mua/bán, tổng lũy kế trong ngày và room còn lại. Dữ liệu được cập nhật trong phiên giao dịch khi có thay đổi.



<details>

  <summary>SDK Foreign Investor</summary>



```python

from trading_websocket.models import ForeignInvestor



def handle_foreign_trading(data: ForeignInvestor):



await client.subscribe_foreign_trading(["SHS", "FPT"], board_id="G1", on_trade=handle_foreign_trading, encoding=encoding)

```

</details>


## Thông tin tiền

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getAccountBalances"></span>

### `GET /accounts/{accountNo}/balances`

<h3 id="getaccountbalances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|accountNo|path|string|true|Số tiểu khoản|

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/{accountNo}/balances \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/{accountNo}/balances HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/{accountNo}/balances", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/balances',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/{accountNo}/balances', headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/balances");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "stock": {
    "totalCash": 3720308,
    "availableCash": 3720022,
    "depositInterest": 286,
    "totalDebt": 592355,
    "depositFeeAmount": 405,
    "withdrawableCash": 3719617,
    "cashDividendReceiving": 0
  },
  "derivative": {
    "pendingDepositWithdraw": 826996062,
    "remainSecure": 122363429600,
    "usedSecure": 102098277,
    "pendingSecure": 826996062,
    "holdTaxAndFee": 0,
    "totalLoanDebt": 0
  }
}
```

<h3 id="getaccountbalances-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» stock|object|false|none|none|
|»» totalCash|integer(int32)|false|none|Tổng tiền (Tiền mặt + Lãi tiền gửi + Tiền bán chờ về + Tiền cổ tức chờ về - Tiền mua trong ngày)|
|»» availableCash|integer(int32)|false|none|Tiền mặt hiện có|
|»» depositInterest|integer(int32)|false|none|Lãi tiền gửi không kỳ hạn|
|»» totalDebt|integer(int32)|false|none|Tổng nợ (Nợ margin tạm thu + Nợ margin còn lại)|
|»» depositFeeAmount|integer(int32)|false|none|Phí lưu ký|
|»» withdrawableCash|integer(int32)|false|none|Tiền có thể rút|
|»» cashDividendReceiving|integer(int32)|false|none|Tiền cổ tức chờ về|
|» derivative|object|false|none|none|
|»» pendingDepositWithdraw|integer(int32)|false|none|Tiền nộp/rút cọc chờ xử lý|
|»» remainSecure|integer(int64)|false|none|Cọc còn lại|
|»» usedSecure|integer(int32)|false|none|Cọc đã sử dụng|
|»» pendingSecure|integer(int32)|false|none|Cọc chờ duyệt|
|»» holdTaxAndFee|integer(int32)|false|none|Thuế và phí tạm giữ|
|»» totalLoanDebt|integer(int32)|false|none|Khoản ứng chưa hoàn|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

## Tài khoản giao dịch

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getAccounts"></span>

### `GET /accounts`

<h3 id="getaccounts-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts', headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "name": "Phạm Thị Thùy",
  "custodyCode": "064CSUN032",
  "investorId": "1000005917",
  "accounts": [
    {
      "id": "0001179019",
      "dealAccount": true,
      "derivativeAccount": true,
      "derivative": {
        "status": "ACTIVE"
      }
    }
  ]
}
```

<h3 id="getaccounts-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» name|string|false|none|Họ tên khách hàng|
|» custodyCode|string|false|none|Số tài khoản lưu ký tại VSD|
|» investorId|string|false|none|Mã định danh khách hàng tại DNSE|
|» accounts|[object]|false|none|none|
|»» id|string|false|none|Số tiểu khoản|
|»» dealAccount|boolean|false|none|Tiểu khoản theo DEAL hoặc không|
|»» derivativeAccount|boolean|false|none|none|
|»» derivative|object|false|none|Trạng thái tài khoản phái sinh<br>ACTIVE: Đang hoạt động<br>INACTIVE: Ngừng hoạt động|
|»»» status|string|false|none|Tiểu khoản được phép giao dịch phái sinh hoặc không|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Danh sách gói vay

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getLoanPackages"></span>

### `GET /accounts/{accountNo}/loan-packages`

<h3 id="getloanpackages-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|symbol|query|string|true|Mã chứng khoán|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|accountNo|path|string|true|Số tiểu khoản|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Gói vay giao dịch cơ sở
- DERIVATIVE: Gói vay giao dịch phái sinh

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/{accountNo}/loan-packages?marketType=DERIVATIVE&symbol=41I1G4000 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/{accountNo}/loan-packages?marketType=DERIVATIVE&symbol=41I1G4000 HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/{accountNo}/loan-packages", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/loan-packages?marketType=DERIVATIVE&symbol=41I1G4000',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/{accountNo}/loan-packages', params={
  'marketType': 'DERIVATIVE',  'symbol': '41I1G4000'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/loan-packages?marketType=DERIVATIVE&symbol=41I1G4000");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "symbolType": "VN30F1M",
  "marketType": "DERIVATIVE",
  "loanPackages": [
    {
      "id": 2279,
      "name": "Gói giao dịch 02",
      "initialRate": 0.1848,
      "maintenanceRate": 0.1735,
      "liquidRate": 0.1731,
      "tradingFee": {
        "id": 2404,
        "name": "2000/HĐ",
        "scope": "PRODUCT",
        "channel": "ALL",
        "schemaType": "FIXED",
        "createdDate": "2022-12-13T08:22:12.530837Z",
        "modifiedDate": "2022-12-13T08:22:12.530837Z",
        "fixedTradingFee": 2000,
        "fixedDailyCloseTradingFee": 2000,
        "progressTradingFee": [
          {
            "fromQuantity": 1,
            "toQuantity": 2000,
            "fee": 1500
          }
        ],
        "progressDailyCloseTradingFee": [
          {
            "fromQuantity": 2001,
            "toQuantity": 3000,
            "fee": 2196
          }
        ]
      }
    }
  ]
}
```

<h3 id="getloanpackages-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» symbolType|string|false|none|Phân loại mã hợp đồng phái sinh theo thời gian đáo hạn (áp dụng cho DERIVATIVE)<br>- VN30F1M: HĐTL chỉ số VN30 1 tháng<br>- VN30F2M: HĐTL chỉ số VN30 2 tháng<br>- VN30F1Q: HĐTL chỉ số VN30 1 quý<br>- VN30F2Q: HĐTL chỉ số VN30 2 quý|
|» marketType|string|false|none|Loại thị trường<br>- STOCK: Gói vay giao dịch cơ sở<br>- DERIVATIVE: Gói vay giao dịch phái sinh|
|» loanPackages|[object]|false|none|Danh sách gói vay|
|»» id|integer(int32)|false|none|Id gói vay|
|»» name|string|false|none|Tên gói vay|
|»» initialRate|number(double)|false|none|Tỷ lệ ban đầu|
|»» maintenanceRate|number(double)|false|none|Tỷ lệ duy trì (call margin)|
|»» liquidRate|number(double)|false|none|Tỷ lệ xử lý (force sell)|
|»» tradingFee|object|false|none|Thông tin biểu phí phái sinh (áp dụng cho DERIVATIVE)|
|»»» id|integer(int32)|false|none|Id chính sách phí phái sinh|
|»»» name|string|false|none|Tên chính sách phí|
|»»» scope|string|false|none|Phạm vi áp dụng|
|»»» channel|string|false|none|Kênh áp dụng|
|»»» schemaType|string|false|none|Loại biểu phí<br>FIXED: Phí cố định<br>PROGRESSIVE: Phí lũy tiến|
|»»» createdDate|string(date-time)|false|none|Thời điểm áp dụng|
|»»» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|
|»»» fixedTradingFee|integer(int32)|false|none|Phí cố định trên 1 hợp đồng|
|»»» fixedDailyCloseTradingFee|integer(int32)|false|none|Phí đóng vị thế trong ngày|
|»»» progressTradingFee|[object]|false|none|Phí giao dịch lũy tiến|
|»»»» fromQuantity|number(double)|false|none|Khối lượng bắt đầu|
|»»»» toQuantity|number(double)|false|none|Khối lượng kết thúc|
|»»»» fee|number(double)|false|none|Mức phí|
|»»» progressDailyCloseTradingFee|[object]|false|none|Phí đóng vị thế trong ngày lũy tiến|
|»»»» fromQuantity|number(double)|false|none|Khối lượng bắt đầu|
|»»»» toQuantity|number(double)|false|none|Khối lượng kết thúc|
|»»»» fee|number(double)|false|none|Mức phí|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Sức mua, sức bán

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getPpse"></span>

### `GET /accounts/{accountNo}/ppse`

<h3 id="getppse-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|symbol|query|string|true|Mã chứng khoán|
|loanPackageId|query|string|true|Id gói vay|
|price|query|string|true|Giá đặt lệnh|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|accountNo|path|integer|true|Số tiểu khoản|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Gói vay giao dịch cơ sở
- DERIVATIVE: Gói vay giao dịch phái sinh

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/{accountNo}/ppse?marketType=STOCK&symbol=ACB&loanPackageId=5757&price=23000 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/{accountNo}/ppse?marketType=STOCK&symbol=ACB&loanPackageId=5757&price=23000 HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/{accountNo}/ppse", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/ppse?marketType=STOCK&symbol=ACB&loanPackageId=5757&price=23000',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/{accountNo}/ppse', params={
  'marketType': 'STOCK',  'symbol': 'ACB',  'loanPackageId': '5757',  'price': '23000'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/ppse?marketType=STOCK&symbol=ACB&loanPackageId=5757&price=23000");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "qmaxBuy": 1209,
  "qmaxSell": 700,
  "price": 23000
}
```

<h3 id="getppse-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» qmaxBuy|integer(int32)|false|none|Khối lượng mua tối đa|
|» qmaxSell|integer(int32)|false|none|Khối lượng bán tối đa|
|» price|number(double)|false|none|Giá đặt|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Sổ lệnh

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getOrders"></span>

### `GET /accounts/{accountNo}/orders`

<h3 id="getorders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|orderCategory|query|string|true|Phân loại lệnh thường, lệnh điều kiện (mặc định NORMAL)|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|accountNo|path|string|true|Số tiểu khoản|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Sổ lệnh cơ sở
- DERIVATIVE: Sổ lệnh phái sinh

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/{accountNo}/orders?marketType=STOCK&orderCategory=NORMAL \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/{accountNo}/orders?marketType=STOCK&orderCategory=NORMAL HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/{accountNo}/orders", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/orders?marketType=STOCK&orderCategory=NORMAL',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/{accountNo}/orders', params={
  'marketType': 'STOCK',  'orderCategory': 'NORMAL'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/orders?marketType=STOCK&orderCategory=NORMAL");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "orders": [
    {
      "id": 141,
      "side": "NB",
      "accountNo": "0001179019",
      "symbol": "BCM",
      "price": 51200,
      "priceSecure": 51200,
      "averagePrice": 0,
      "quantity": 300,
      "fillQuantity": 0,
      "canceledQuantity": 0,
      "leaveQuantity": 300,
      "orderType": "LO",
      "orderCategory": "NORMAL",
      "orderStatus": "New",
      "loanPackageId": 7937,
      "marketType": "STOCK",
      "transDate": "2026-03-16",
      "createdDate": "2026-03-24T03:15:22.226297778Z",
      "modifiedDate": "2026-03-24T03:15:22.358568266Z"
    }
  ]
}
```

<h3 id="getorders-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» orders|[object]|false|none|Danh sách lệnh giao dịch|
|»» id|integer(int32)|false|none|Id lệnh giao dịch|
|»» side|string|false|none|Chiều giao dịch<br>NB: Mua<br>NS: Bán|
|»» accountNo|string|false|none|Số tiểu khoản|
|»» symbol|string|false|none|Mã chứng khoán|
|»» price|number(double)|false|none|Giá đặt|
|»» priceSecure|number(double)|false|none|Giá dùng để kiểm tra sức mua/đặt lệnh|
|»» averagePrice|number(double)|false|none|Giá khớp trung bình|
|»» quantity|integer(int32)|false|none|Khối lượng đặt|
|»» fillQuantity|integer(int32)|false|none|Khối lượng đã khớp|
|»» canceledQuantity|integer(int32)|false|none|Khối lượng đã hủy|
|»» leaveQuantity|integer(int32)|false|none|Khối lượng còn lại|
|»» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|»» orderCategory|string|false|none|Phân loại lệnh thường, lệnh điều kiện (mặc định NORMAL)|
|»» orderStatus|string|false|none|Trạng thái lệnh<br>- Pending/PendingNew: Chờ gửi<br>- New: Chờ khớp<br>- PendingReplace: Chờ sửa<br>- PendingCancel: Chờ hủy<br>- PartiallyFilled: Khớp một phần<br>- Filled: Khớp toàn bộ<br>- Canceled: Đã hủy<br>- Rejected: Bị từ chối<br>- Expired: Hết hạn trong phiên<br>- DoneForDay: Lệnh được giải tỏa do không khớp trong phiên|
|»» loanPackageId|integer(int32)|false|none|Gói vay áp dụng cho mã chứng khoán|
|»» marketType|string|false|none|Loại thị trường<br>STOCK: Lệnh cơ sở<br>DERIVATIVE: Lệnh phái sinh|
|»» transDate|string|false|none|Ngày giao dịch|
|»» createdDate|string(date-time)|false|none|Thời điểm tạo|
|»» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Chi tiết trạng thái lệnh

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getExecutions"></span>

### `GET /accounts/{accountNo}/executions/{orderId}`

<h3 id="getexecutions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|orderCategory|query|string|true|Phân loại lệnh thường, lệnh điều kiện (mặc định NORMAL)|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|accountNo|path|integer|true|Số tiểu khoản|
|orderId|path|integer|true|Id lệnh giao dịch|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Lệnh cơ sở
- DERIVATIVE: Sổ lệnh phái sinh (hiện tại chỉ hỗ trợ phái sinh) 

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/{accountNo}/executions/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/{accountNo}/executions/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/{accountNo}/executions/{orderId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/executions/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/{accountNo}/executions/{orderId}', params={
  'marketType': 'DERIVATIVE',  'orderCategory': 'NORMAL'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/executions/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "id": 966,
  "side": "NS",
  "accountNo": "0001179019",
  "symbol": "41I1G4000",
  "price": 1706.1,
  "quantity": 5,
  "orderType": "LO",
  "loanPackageId": 2278,
  "orderCategory": "NORMAL",
  "orderStatus": "Filled",
  "fillQuantity": 5,
  "lastQuantity": 2,
  "lastPrice": 1706.1,
  "averagePrice": 1750.96,
  "transDate": "2026-03-16",
  "taxRate": 0,
  "exchangeFeeRate": 0,
  "feeRate": 0,
  "leaveQuantity": 0,
  "canceledQuantity": 0,
  "error": "",
  "marketType": "DERIVATIVE",
  "priceSecure": 1706.1,
  "createdDate": "2026-03-23T03:10:06.556826794Z",
  "modifiedDate": "2026-03-23T04:07:45.683977124Z",
  "metadata": "{\"orderSession\":\"OPEN\",\"dealId\":\"1.77410795472387E14\",\"releaseSecureOnFilled\":\"false\",\"originMaker\":\"1000005917-close_deal_177410795472387\",\"dtaAccountNo\":\"D000113702\",\"isForeigner\":false,\"probType\":\"CUSTOMER\",\"eventNo\":5}",
  "reports": []
}
```

<h3 id="getexecutions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer(int32)|false|none|ID lệnh|
|» side|string|false|none|Chiều giao dịch<br>- NB: Mua<br>- NS: Bán|
|» accountNo|string|false|none|Số tiểu khoản|
|» symbol|string|false|none|Mã hợp đồng phái sinh|
|» price|number(double)|false|none|Giá đặt lệnh|
|» quantity|integer(int32)|false|none|Khối lượng đặt lệnh|
|» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|» loanPackageId|integer(int32)|false|none|Mã gói vay|
|» orderCategory|string|false|none|Phân loại lệnh (mặc định NORMAL)|
|» orderStatus|string|false|none|Trạng thái lệnh<br>- Pending/PendingNew: Chờ gửi<br>- New: Chờ khớp<br>- PartiallyFilled: Khớp một phần<br>- Filled: Khớp toàn bộ<br>- Rejected: Bị từ chối<br>- Expired: Hết hạn trong phiên<br>- DoneForDay: Lệnh được giải tỏa do không khớp trong phiên|
|» fillQuantity|integer(int32)|false|none|Khối lượng đã khớp|
|» lastQuantity|integer(int32)|false|none|Khối lượng khớp gần nhất|
|» lastPrice|number(double)|false|none|Giá khớp gần nhất|
|» averagePrice|number(double)|false|none|Giá khớp trung bình|
|» transDate|string|false|none|Ngày giao dịch|
|» taxRate|integer(int32)|false|none|Tỷ lệ thuế|
|» exchangeFeeRate|integer(int32)|false|none|Tỷ lệ phí trả Sở giao dịch|
|» feeRate|integer(int32)|false|none|Tổng tỷ lệ phí của lệnh|
|» leaveQuantity|integer(int32)|false|none|Khối lượng còn lại chưa khớp|
|» canceledQuantity|integer(int32)|false|none|Khối lượng đã hủy|
|» error|string|false|none|Mã lỗi nếu lệnh bị từ chối|
|» marketType|string|false|none|Loại thị trường<br>- STOCK: Lệnh cơ sở<br>- DERIVATIVE: LLệnh phái sinh (hiện tại chỉ hỗ trợ phái sinh)|
|» priceSecure|number(double)|false|none|Giá dùng để kiểm tra sức mua/đặt lệnh|
|» createdDate|string(date-time)|false|none|Thời điểm tạo lệnh|
|» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật lệnh|
|» metadata|string|false|none|Thông tin bổ sung của lệnh|
|» reports|[object]|false|none|Danh sách trạng thái lệnh cơ sở theo từng lần cập nhật|
|»» id|integer(int32)|false|none|ID lệnh|
|»» side|string|false|none|Chiều giao dịch<br>- NB: Mua<br>- NS: Bán|
|»» accountNo|string|false|none|Số tiểu khoản|
|»» symbol|string|false|none|Mã hợp đồng phái sinh|
|»» price|number(double)|false|none|Giá đặt lệnh|
|»» quantity|integer(int32)|false|none|Khối lượng đặt lệnh|
|»» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|»» orderStatus|string|false|none|Trạng thái lệnh<br>- Pending/PendingNew: Chờ gửi<br>- New: Chờ khớp<br>- PartiallyFilled: Khớp một phần<br>- Filled: Khớp toàn bộ<br>- Rejected: Bị từ chối<br>- Expired: Hết hạn trong phiên<br>- DoneForDay: Lệnh được giải tỏa do không khớp trong phiên|
|»» fillQuantity|integer(int32)|false|none|Khối lượng đã khớp|
|»» lastQuantity|integer(int32)|false|none|Khối lượng khớp gần nhất|
|»» lastPrice|number(double)|false|none|Giá khớp gần nhất|
|»» averagePrice|number(double)|false|none|Giá khớp trung bình|
|»» transDate|string|false|none|Ngày giao dịch|
|»» createdDate|string(date-time)|false|none|Thời điểm tạo lệnh|
|»» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật lệnh|
|»» taxRate|integer(int32)|false|none|Tỷ lệ thuế|
|»» exchangeFeeRate|integer(int32)|false|none|Tỷ lệ phí trả Sở giao dịch|
|»» feeRate|integer(int32)|false|none|Tổng tỷ lệ phí của lệnh|
|»» leaveQuantity|integer(int32)|false|none|Khối lượng còn lại chưa khớp|
|»» canceledQuantity|integer(int32)|false|none|Khối lượng đã hủy|
|»» error|string|false|none|Mã lỗi nếu có|
|»» priceSecure|number(double)|false|none|Giá dùng để kiểm tra sức mua/đặt lệnh|
|»» metadata|string|false|none|Thông tin bổ sung của lệnh|
|»» loanPackageId|integer(int32)|false|none|Mã gói vay|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Lịch sử lệnh

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getOrdersHistory"></span>

### `GET /accounts/{accountNo}/orders/history`

<h3 id="getordershistory-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|from|query|string|true|Ngày bắt đầu (yyyy-mm-dd) |
|to|query|string|true|Ngày kết thúc (yyyy-mm-dd) |
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|accountNo|path|string|true|Số tiểu khoản|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Gói vay giao dịch cơ sở
- DERIVATIVE: Gói vay giao dịch phái sinh

**from**: Ngày bắt đầu (yyyy-mm-dd) 
- Thời gian tra cứu tối đa trong 1 năm tính từ ngày hiện tại

**to**: Ngày kết thúc (yyyy-mm-dd) 
- Lớn hơn hoặc bằng ngày bắt đầu và không vượt quá ngày hiện tại

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/{accountNo}/orders/history?marketType=STOCK&from=2026-02-15&to=2026-03-18 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/{accountNo}/orders/history?marketType=STOCK&from=2026-02-15&to=2026-03-18 HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/{accountNo}/orders/history", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/orders/history?marketType=STOCK&from=2026-02-15&to=2026-03-18',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/{accountNo}/orders/history', params={
  'marketType': 'STOCK',  'from': '2026-02-15',  'to': '2026-03-18'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/orders/history?marketType=STOCK&from=2026-02-15&to=2026-03-18");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "accountNo": "0001179019",
  "fillQuantity": 0,
  "total": 8,
  "start": 0,
  "end": 8,
  "marketType": "STOCK",
  "data": [
    {
      "id": "20260312_241",
      "symbol": "HPG",
      "side": "NB",
      "orderType": "LO",
      "orderStatus": "Expired",
      "price": 27200,
      "quantity": 200,
      "fillQuantity": 0,
      "leaveQuantity": 0,
      "canceledQuantity": 200,
      "averagePrice": 0,
      "loanPackageId": 5765,
      "transDate": "2026-03-12",
      "createdDate": "2026-03-17T06:44:18.813804Z",
      "modifiedDate": "2026-03-18T15:28:24.44026Z"
    }
  ]
}
```

<h3 id="getordershistory-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» accountNo|string|false|none|Số tiểu khoản|
|» fillQuantity|integer(int32)|false|none|Tổng khối lượng đã khớp|
|» total|integer(int32)|false|none|Tổng số bản ghi|
|» start|integer(int32)|false|none|Vị trí bắt đầu của tập bản ghi được trả về|
|» end|integer(int32)|false|none|Vị trí kết thúc của tập bản ghi được trả về|
|» marketType|string|false|none|Loại thị trường<br>- STOCK: Gói vay giao dịch cơ sở<br>- DERIVATIVE: Gói vay giao dịch phái sinh|
|» data|[object]|false|none|Danh sách lệnh giao dịch|
|»» id|string|false|none|ID lệnh trên hệ thống|
|»» symbol|string|false|none|Mã chứng khoán|
|»» side|string|false|none|Chiều giao dịch<br>NB: Mua<br>NS: Bán|
|»» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|»» orderStatus|string|false|none|Trạng thái lệnh<br>- Pending/PendingNew: Chờ gửi<br>- New: Chờ khớp<br>- PartiallyFilled: Khớp một phần<br>- Filled: Khớp toàn bộ<br>- Rejected: Bị từ chối<br>- Expired: Hết hạn trong phiên<br>- DoneForDay: Lệnh được giải tỏa do không khớp trong phiên|
|»» price|integer(int32)|false|none|Giá đặt|
|»» quantity|integer(int32)|false|none|Khối lượng đặt|
|»» fillQuantity|integer(int32)|false|none|Khối lượng đã khớp|
|»» leaveQuantity|integer(int32)|false|none|Khối lượng còn lại|
|»» canceledQuantity|integer(int32)|false|none|Khối lượng đã huỷ|
|»» averagePrice|integer(int32)|false|none|Giá khớp trung bình|
|»» loanPackageId|integer(int32)|false|none|ID gói vay|
|»» transDate|string|false|none|Ngày giao dịch|
|»» createdDate|string(date-time)|false|none|Thời điểm tạo|
|»» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Vị thế nắm giữ

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getPositions"></span>

### `GET /accounts/{accountNo}/positions`

<h3 id="getpositions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|pageSize|query|string|true|Kích thước trang dữ liệu (page size)|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|accountNo|path|string|true|Số tiểu khoản|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Danh sách vị thế cơ sở
- DERIVATIVE: Danh sách vị thế phái sinh

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/{accountNo}/positions?marketType=DERIVATIVE&pageSize=20 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/{accountNo}/positions?marketType=DERIVATIVE&pageSize=20 HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/{accountNo}/positions", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/positions?marketType=DERIVATIVE&pageSize=20',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/{accountNo}/positions', params={
  'marketType': 'DERIVATIVE',  'pageSize': '20'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/positions?marketType=DERIVATIVE&pageSize=20");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "positions": [
    {
      "id": 177410795472387,
      "symbol": "41I1G4000",
      "accountNo": "0001179019",
      "status": "OPEN",
      "loanPackageId": 2278,
      "side": "NB",
      "accumulateQuantity": 6,
      "tradeQuantity": 1,
      "closedQuantity": 5,
      "openQuantity": 1,
      "overNightQuantity": 0,
      "costPrice": 1834.5,
      "marketPrice": 1706.1,
      "breakEvenPrice": 1834.95691,
      "createdDate": "2026-03-23T03:08:32.773651Z",
      "modifiedDate": "2026-03-23T04:07:45.692156Z"
    }
  ],
  "pageIndex": 0,
  "pageSize": 20,
  "pageNumber": 1,
  "total": 1
}
```

<h3 id="getpositions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» positions|[object]|false|none|none|
|»» id|integer(int64)|false|none|ID vị thế|
|»» symbol|string|false|none|Mã chứng khoán|
|»» marketType|string|false|none|Loại thị trường<br>STOCK: Gói vay giao dịch cơ sở<br>DERIVATIVE: Gói vay giao dịch phái sinh|
|»» accountNo|string|false|none|Số tiểu khoản|
|»» status|string|false|none|Trạng thái của vị thế<br>OPEN: Đang mở<br>PENDING_CLOSE: Chờ đóng<br>CLOSED: Đã đóng<br>ODD_LOT: Lô lẻ (cơ sở)|
|»» loanPackageId|integer(int32)|false|none|Gói vay cơ sở hoặc phái sinh|
|»» side|string|false|none|Loại vị thế<br>NB: Mua<br>NS: Bán|
|»» accumulateQuantity|integer(int32)|false|none|Khối lượng cộng dồn|
|»» tradeQuantity|integer(int32)|false|none|Khối lượng được giao dịch|
|»» closedQuantity|integer(int32)|false|none|Khối lượng đã đóng|
|»» openQuantity|integer(int32)|false|none|Khối lượng mở|
|»» overNightQuantity|integer(int32)|false|none|Khối lượng mở qua đêm (dành cho phái sinh)|
|»» costPrice|number(float)|false|none|Giá vốn trung bình của khối lượng mở|
|»» marketPrice|number(double)|false|none|Giá thị trường|
|»» breakEvenPrice|number(double)|false|none|Giá hòa vốn|
|»» createdDate|string(date-time)|false|none|Thời điểm mở|
|»» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|
|» pageIndex|integer(int32)|false|none|Kích thước trang dữ liệu (dành cho phái sinh)|
|» pageSize|integer(int32)|false|none|Số bản ghi trên 1 trang (dành cho phái sinh)|
|» pageNumber|integer(int32)|false|none|Số trang (chỉ dành cho phái sinh)|
|» total|integer(int32)|false|none|Tổng số vị thế (chỉ dành cho phái sinh)|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Chi tiết vị thế theo ID

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getPositionById"></span>

### `GET /accounts/positions/{positionId}`

<h3 id="getpositionbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|positionId|path|integer|true|Id vị thế |

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Danh sách Deal cơ sở
- DERIVATIVE: Danh sách Deal phái sinh

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/positions/{positionId}?marketType=DERIVATIVE \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/positions/{positionId}?marketType=DERIVATIVE HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/positions/{positionId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/positions/{positionId}?marketType=DERIVATIVE',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/positions/{positionId}', params={
  'marketType': 'DERIVATIVE'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/positions/{positionId}?marketType=DERIVATIVE");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "data": {
    "id": 177410795472387,
    "symbol": "41I1G4000",
    "marketType": "DERIVATIVE",
    "accountNo": "0001179019",
    "status": "OPEN",
    "loanPackageId": 2278,
    "side": "NB",
    "accumulateQuantity": 6,
    "tradeQuantity": 1,
    "closedQuantity": 5,
    "openQuantity": 1,
    "overNightQuantity": 0,
    "costPrice": 1834.5,
    "averageCostPrice": 1834.5,
    "averageClosePrice": 1750.96,
    "marketPrice": 1706.1,
    "breakEvenPrice": 1834.95691,
    "createdDate": "2026-03-23T03:08:32.773651Z",
    "modifiedDate": "2026-03-23T04:07:45.692156Z"
  }
}
```

<h3 id="getpositionbyid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|false|none|none|
|»» id|integer(int64)|false|none|ID vị thế|
|»» symbol|string|false|none|Mã chứng khoán|
|»» marketType|string|false|none|Loại thị trường<br>- STOCK: Vị thế cơ sở<br>- DERIVATIVE: Vị thế phái sinh|
|»» accountNo|string|false|none|Số tiểu khoản|
|»» status|string|false|none|Trạng thái của vị thế<br>- OPEN: Đang mở<br>- PENDING_CLOSE: Chờ đóng<br>- CLOSED: Đã đóng<br>- ODD_LOT: Lô lẻ (cơ sở)|
|»» loanPackageId|integer(int32)|false|none|Gói vay cơ sở hoặc phái sinh|
|»» side|string|false|none|Loại vị thế<br>- NB: Mua<br>- NS: Bán|
|»» accumulateQuantity|integer(int32)|false|none|Khối lượng cộng dồn|
|»» tradeQuantity|integer(int32)|false|none|Khối lượng được giao dịch|
|»» closedQuantity|integer(int32)|false|none|Khối lượng đã đóng|
|»» openQuantity|integer(int32)|false|none|Khối lượng mở|
|»» overNightQuantity|integer(int32)|false|none|Khối lượng mở qua đêm (dành cho phái sinh)|
|»» costPrice|number(float)|false|none|Giá vốn trung bình của khối lượng mở|
|»» averageCostPrice|number(float)|false|none|Giá vốn trung bình|
|»» averageClosePrice|number(double)|false|none|Giá đóng trung bình|
|»» marketPrice|number(double)|false|none|Giá thị trường|
|»» breakEvenPrice|number(double)|false|none|Giá hòa vốn|
|»» createdDate|string(date-time)|false|none|Thời điểm mở|
|»» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

<h1 id="dnse-openapi-v2-trading">trading</h1>
## Gửi Email OTP

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="sendEmailOtp"></span>

### `POST /registration/send-email-otp`

<h3 id="sendemailotp-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|

> Code samples

```shell
# You can also use wget
curl -X POST https://openapi.dnse.com.vn/registration/send-email-otp \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
POST https://openapi.dnse.com.vn/registration/send-email-otp HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://openapi.dnse.com.vn/registration/send-email-otp", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/registration/send-email-otp',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.post('https://openapi.dnse.com.vn/registration/send-email-otp', headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/registration/send-email-otp");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 400 Response

```json
{
  "code": "OA-003",
  "message": "Thông tin nhập không hợp lệ",
  "status": 400
}
```

<h3 id="sendemailotp-responseschema">Response Schema</h3>

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Xác thực OTP

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="2FAVerification"></span>

### `POST /registration/trading-token`

<h3 id="2faverification-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|body|body|object|false|none|
|» otpType|body|string|false|Phương thức xác thực OTP|
|» passcode|body|string|false|Mã OTP tương ứng với phương thức xác thực|

#### Detailed descriptions

**» otpType**: Phương thức xác thực OTP
- email_otp: Áp dụng cho tài khoản đăng ký phương thức xác thực lớp thứ 2 là Email OTP
- smart_otp: Áp dụng cho tài khoản đăng ký phương thức xác thực lớp thứ 2 là Smart OTP

> Code samples

```shell
# You can also use wget
curl -X POST https://openapi.dnse.com.vn/registration/trading-token \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
POST https://openapi.dnse.com.vn/registration/trading-token HTTP/1.1
Host: openapi.dnse.com.vn
Content-Type: application/json
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://openapi.dnse.com.vn/registration/trading-token", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript
const inputBody = '{
  "otpType": "email_otp",
  "passcode": "519752"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/registration/trading-token',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.post('https://openapi.dnse.com.vn/registration/trading-token', headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/registration/trading-token");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Body parameter

```json
{
  "otpType": "email_otp",
  "passcode": "519752"
}
```

> Example responses

> 200 Response

```json
{
  "tradingToken": "9ab81e9c-8a81-45aa-8190-b69a1c179d52"
}
```

<h3 id="2faverification-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tradingToken|string|false|none|Token đặt lệnh|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Đặt lệnh

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="placeOrder"></span>

### `POST /accounts/orders`

<h3 id="placeorder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|orderCategory|query|string|true|Phân loại lệnh thường, lệnh điều kiện (mặc định NORMAL)|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|trading-token|header|string|true|Token đặt lệnh|
|body|body|object|false|none|
|» accountNo|body|string|false|Số tiểu khoản|
|» loanPackageId|body|integer(int32)|false|Id gói vay|
|» orderType|body|string|false|Loại lệnh|
|» price|body|number(double)|false|Giá đặt lệnh|
|» quantity|body|integer(int32)|false|Khối lượng đặt lệnh|
|» side|body|string|false|Loại lệnh|
|» symbol|body|string|false|Mã chứng khoán|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Đặt lệnh cơ sở
- DERIVATIVE: Đặt lệnh phái sinh

**» orderType**: Loại lệnh
- LO: Lệnh giới hạn
- MOK/MAK/MTL: Lệnh thị trường
- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa
- PLO: Lệnh khớp lệnh sau giờ

**» side**: Loại lệnh
- NB: Mua
- NS: Bán

> Code samples

```shell
# You can also use wget
curl -X POST https://openapi.dnse.com.vn/accounts/orders?marketType=DERIVATIVE&orderCategory=NORMAL \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Signature: your_signature' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'trading-token: 7ceef658-9f01-414e-8b3e-faa77bb9061e'

```

```http
POST https://openapi.dnse.com.vn/accounts/orders?marketType=DERIVATIVE&orderCategory=NORMAL HTTP/1.1
Host: openapi.dnse.com.vn
Content-Type: application/json
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Signature: your_signature
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
trading-token: 7ceef658-9f01-414e-8b3e-faa77bb9061e

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Signature": []string{"your_signature"},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "trading-token": []string{"7ceef658-9f01-414e-8b3e-faa77bb9061e"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://openapi.dnse.com.vn/accounts/orders", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript
const inputBody = '{
  "accountNo": "0001179019",
  "loanPackageId": 2278,
  "orderType": "LO",
  "price": 35000,
  "quantity": 300,
  "side": "NB",
  "symbol": "TCB"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Signature':'your_signature',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'trading-token':'7ceef658-9f01-414e-8b3e-faa77bb9061e'
};

fetch('https://openapi.dnse.com.vn/accounts/orders?marketType=DERIVATIVE&orderCategory=NORMAL',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Signature': 'your_signature',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'trading-token': '7ceef658-9f01-414e-8b3e-faa77bb9061e'
}

r = requests.post('https://openapi.dnse.com.vn/accounts/orders', params={
  'marketType': 'DERIVATIVE',  'orderCategory': 'NORMAL'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/orders?marketType=DERIVATIVE&orderCategory=NORMAL");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Body parameter

```json
{
  "accountNo": "0001179019",
  "loanPackageId": 2278,
  "orderType": "LO",
  "price": 35000,
  "quantity": 300,
  "side": "NB",
  "symbol": "TCB"
}
```

> Example responses

> 200 Response

```json
{
  "id": 1626,
  "symbol": "41I1G4000",
  "side": "NS",
  "orderType": "LO",
  "orderStatus": "Pending",
  "price": 1861.5,
  "averagePrice": 0,
  "quantity": 3,
  "fillQuantity": 0,
  "canceledQuantity": 0,
  "leaveQuantity": 3,
  "accountNo": "0001179019",
  "marketType": "DERIVATIVE",
  "orderCategory": "NORMAL",
  "transDate": "2026-03-16",
  "createdDate": "2026-03-24T04:09:50.761146893Z",
  "modifiedDate": "2026-03-24T04:09:50.761151529Z"
}
```

<h3 id="placeorder-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer(int32)|false|none|Id lệnh giao dịch|
|» symbol|string|false|none|Mã chứng khoán|
|» side|string|false|none|Chiều đặt lệnh<br>NB: Mua<br>NS: Bán|
|» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|» orderStatus|string|false|none|Trạng thái lệnh<br>- PendingNew: Chờ gửi<br>- New: Chờ khớp<br>- PendingReplace: Chờ sửa<br>- PartiallyFilled: Khớp một phần<br>- Filled: Khớp toàn bộ<br>- Canceled: Đã hủy<br>- Rejected: Bị từ chối<br>- Expired: Hết hạn trong phiên<br>- DoneForDay: Giải tỏa trong phiên|
|» price|number(double)|false|none|Giá đặt|
|» averagePrice|integer(int32)|false|none|Giá khớp trung bình|
|» quantity|integer(int32)|false|none|Khối lượng đặt|
|» fillQuantity|integer(int32)|false|none|Khối lượng khớp|
|» canceledQuantity|integer(int32)|false|none|Khối lượng đã hủy|
|» leaveQuantity|integer(int32)|false|none|Khối lượng còn lại|
|» accountNo|string|false|none|Số tiểu khoản|
|» marketType|string|false|none|Loại thị trường<br>- STOCK: Lệnh cơ sở<br>- DERIVATIVE: Lệnh phái sinh|
|» orderCategory|string|false|none|Phân loại lệnh thường (mặc định NORMAL)|
|» transDate|string|false|none|Ngày giao dịch|
|» createdDate|string(date-time)|false|none|Thời điểm tạo|
|» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Sửa lệnh

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="replaceOrder"></span>

### `PUT /accounts/{accountNo}/orders/{orderId}`

<h3 id="replaceorder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|orderCategory|query|string|true|Phân loại lệnh thường, lệnh điều kiện (mặc định NORMAL)|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|trading-token|header|string|true|Token đặt lệnh|
|body|body|object|false|none|
|» price|body|number(double)|false|Giá mới cho lệnh LO|
|» quantity|body|integer(int32)|false|Khối lượng mới|
|accountNo|path|string|true|Số tiểu khoản|
|orderId|path|integer|true|Id lệnh giao dịch|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Gói vay giao dịch cơ sở
- DERIVATIVE: Gói vay giao dịch phái sinh

**» price**: Giá mới cho lệnh LO
- Đối với lệnh cơ sở, có thể sửa cả giá và khối lượng
- Đối với lệnh phái sinh, chỉ được sửa hoặc giá hoặc khối lượng

**» quantity**: Khối lượng mới
- Đối với lệnh phái sinh, khối lượng mới phải lớn hơn khối lượng đã khớp (nếu có) của lệnh đã đặt

> Code samples

```shell
# You can also use wget
curl -X PUT https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Signature: your_signature' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'trading-token: 7ceef658-9f01-414e-8b3e-faa77bb9061e'

```

```http
PUT https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL HTTP/1.1
Host: openapi.dnse.com.vn
Content-Type: application/json
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Signature: your_signature
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
trading-token: 7ceef658-9f01-414e-8b3e-faa77bb9061e

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Signature": []string{"your_signature"},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "trading-token": []string{"7ceef658-9f01-414e-8b3e-faa77bb9061e"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript
const inputBody = '{
  "price": 1851,
  "quantity": 3
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Signature':'your_signature',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'trading-token':'7ceef658-9f01-414e-8b3e-faa77bb9061e'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Signature': 'your_signature',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'trading-token': '7ceef658-9f01-414e-8b3e-faa77bb9061e'
}

r = requests.put('https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}', params={
  'marketType': 'DERIVATIVE',  'orderCategory': 'NORMAL'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Body parameter

```json
{
  "price": 1851,
  "quantity": 3
}
```

> Example responses

> 200 Response

```json
{
  "id": 1626,
  "accountNo": "0001179019",
  "side": "NS",
  "loanPackageId": 2278,
  "symbol": "41I1G4000",
  "orderType": "LO",
  "orderCategory": "NORMAL",
  "price": 1851,
  "quantity": 3,
  "fillQuantity": 0,
  "canceledQuantity": 0,
  "marketType": "DERIVATIVE",
  "transDate": "2026-03-16",
  "createdDate": "2026-03-24T04:09:50.761146893Z",
  "modifiedDate": "2026-03-24T04:14:21.004856492Z"
}
```

<h3 id="replaceorder-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer(int32)|false|none|Id lệnh giao dịch|
|» accountNo|string|false|none|Số tiểu khoản|
|» side|string|false|none|Chiều đặt lệnh<br>- NB: Mua<br>- NS: Bán|
|» loanPackageId|integer(int32)|false|none|Mã gói vay|
|» symbol|string|false|none|Mã chứng khoán|
|» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|» orderCategory|string|false|none|Phân loại lệnh thường (mặc định NORMAL)|
|» price|number(double)|false|none|Giá đặt|
|» quantity|integer(int32)|false|none|Khối lượng đặt|
|» fillQuantity|integer(int32)|false|none|Khối lượng khớp|
|» canceledQuantity|integer(int32)|false|none|Khối lượng đã hủy|
|» marketType|string|false|none|Loại thị trường<br>- STOCK: Lệnh cơ sở<br>- DERIVATIVE: Lệnh phái sinh|
|» transDate|string|false|none|Ngày giao dịch|
|» createdDate|string(date-time)|false|none|Thời điểm tạo|
|» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Hủy lệnh

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="cancelOrder"></span>

### `DELETE /accounts/{accountNo}/orders/{orderId}`

<h3 id="cancelorder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|orderCategory|query|string|true|Phân loại lệnh thường, lệnh điều kiện (mặc định NORMAL)|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|trading-token|header|string|true|Token đặt lệnh|
|accountNo|path|string|true|Số tiểu khoản|
|orderId|path|integer|true|Id lệnh giao dịch|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Đặt lệnh cơ sở
- DERIVATIVE: Đặt lệnh phái sinh

> Code samples

```shell
# You can also use wget
curl -X DELETE https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Signature: your_signature' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'trading-token: 7ceef658-9f01-414e-8b3e-faa77bb9061e'

```

```http
DELETE https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Signature: your_signature
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
trading-token: 7ceef658-9f01-414e-8b3e-faa77bb9061e

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Signature": []string{"your_signature"},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "trading-token": []string{"7ceef658-9f01-414e-8b3e-faa77bb9061e"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Signature':'your_signature',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'trading-token':'7ceef658-9f01-414e-8b3e-faa77bb9061e'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Signature': 'your_signature',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'trading-token': '7ceef658-9f01-414e-8b3e-faa77bb9061e'
}

r = requests.delete('https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}', params={
  'marketType': 'DERIVATIVE',  'orderCategory': 'NORMAL'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "id": 1626,
  "symbol": "41I1G4000",
  "side": "NS",
  "orderType": "LO",
  "orderStatus": "PendingCancel",
  "loanPackageId": "2278",
  "price": 1851,
  "averagePrice": 0,
  "quantity": 3,
  "fillQuantity": 0,
  "canceledQuantity": 0,
  "leaveQuantity": 3,
  "accountNo": "0001179019",
  "orderCategory": "NORMAL",
  "marketType": "DERIVATIVE",
  "transDate": "2026-03-16",
  "createdDate": "2026-03-24T04:09:50.761146893Z",
  "modifiedDate": "2026-03-24T04:16:12.469115348Z"
}
```

<h3 id="cancelorder-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer(int32)|false|none|Id lệnh giao dịch|
|» symbol|string|false|none|Mã chứng khoán|
|» side|string|false|none|Chiều đặt lệnh<br>- NB: Mua<br>- NS: Bán|
|» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|» orderStatus|string|false|none|Trạng thái lệnh<br>- PendingNew: Chờ gửi<br>- New: Chờ khớp<br>- PendingReplace: Chờ sửa<br>- PartiallyFilled: Khớp một phần<br>- Filled: Khớp toàn bộ<br>- Canceled: Đã hủy<br>- Rejected: Bị từ chối<br>- Expired: Hết hạn trong phiên<br>- DoneForDay: Giải tỏa trong phiên|
|» loanPackageId|string|false|none|Mã gói vay|
|» price|number(double)|false|none|Giá đặt|
|» averagePrice|number(float)|false|none|Giá khớp trung bình|
|» quantity|integer(int32)|false|none|Khối lượng đặt|
|» fillQuantity|integer(int32)|false|none|Khối lượng khớp|
|» canceledQuantity|integer(int32)|false|none|Khối lượng đã hủy|
|» leaveQuantity|integer(int32)|false|none|Khối lượng còn lại|
|» accountNo|string|false|none|Số tiểu khoản|
|» orderCategory|string|false|none|Phân loại lệnh thường (mặc định NORMAL)|
|» marketType|string|false|none|Loại thị trường<br>- STOCK: Lệnh cơ sở<br>- DERIVATIVE: Lệnh phái sinh|
|» transDate|string|false|none|Ngày giao dịch|
|» createdDate|string(date-time)|false|none|Thời điểm tạo|
|» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Chi tiết lệnh theo ID

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getOrderDetail"></span>

### `GET /accounts/{accountNo}/orders/{orderId}`

<h3 id="getorderdetail-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|orderCategory|query|string|true|Phân loại lệnh thường, lệnh điều kiện (mặc định NORMAL)|
|X-API-Key|header|string|false|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|false|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|false|Chữ ký xác thực yêu cầu|
|accountNo|path|string|true|Số tiểu khoản|
|orderId|path|integer|true|Id lệnh giao dịch|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Sổ lệnh cơ sở
- DERIVATIVE: Sổ lệnh phái sinh

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}', params={
  'marketType': 'DERIVATIVE',  'orderCategory': 'NORMAL'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/{accountNo}/orders/{orderId}?marketType=DERIVATIVE&orderCategory=NORMAL");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "id": 966,
  "side": "NS",
  "accountNo": "0001179019",
  "symbol": "41I1G4000",
  "price": 1706.1,
  "quantity": 5,
  "orderType": "LO",
  "loanPackageId": 2278,
  "orderCategory": "NORMAL",
  "orderStatus": "Filled",
  "fillQuantity": 5,
  "lastQuantity": 2,
  "lastPrice": 1706.1,
  "averagePrice": 1750.96,
  "transDate": "2026-03-16",
  "taxRate": 0,
  "exchangeFeeRate": 0,
  "feeRate": 0,
  "leaveQuantity": 0,
  "canceledQuantity": 0,
  "error": "",
  "marketType": "DERIVATIVE",
  "priceSecure": 1706.1,
  "createdDate": "2026-03-23T03:10:06.556826794Z",
  "modifiedDate": "2026-03-23T04:07:45.683977124Z",
  "metadata": "{\"orderSession\":\"OPEN\",\"dealId\":\"1.77410795472387E14\",\"releaseSecureOnFilled\":\"false\",\"originMaker\":\"1000005917-close_deal_177410795472387\",\"dtaAccountNo\":\"D000113702\",\"isForeigner\":false,\"probType\":\"CUSTOMER\",\"eventNo\":5}",
  "reports": []
}
```

<h3 id="getorderdetail-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer(int32)|false|none|ID lệnh|
|» side|string|false|none|Chiều giao dịch<br>- NB: Mua<br>- NS: Bán|
|» accountNo|string|false|none|Số tiểu khoản|
|» symbol|string|false|none|Mã hợp đồng phái sinh|
|» price|number(double)|false|none|Giá đặt lệnh|
|» quantity|integer(int32)|false|none|Khối lượng đặt lệnh|
|» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|» loanPackageId|integer(int32)|false|none|Mã gói vay|
|» orderCategory|string|false|none|Phân loại lệnh (mặc định NORMAL)|
|» orderStatus|string|false|none|Trạng thái lệnh<br>- Pending/PendingNew: Chờ gửi<br>- New: Chờ khớp<br>- PartiallyFilled: Khớp một phần<br>- Filled: Khớp toàn bộ<br>- Rejected: Bị từ chối<br>- Expired: Hết hạn trong phiên<br>- DoneForDay: Lệnh được giải tỏa do không khớp trong phiên|
|» fillQuantity|integer(int32)|false|none|Khối lượng đã khớp|
|» lastQuantity|integer(int32)|false|none|Khối lượng khớp gần nhất|
|» lastPrice|number(double)|false|none|Giá khớp gần nhất|
|» averagePrice|number(double)|false|none|Giá khớp trung bình|
|» transDate|string|false|none|Ngày giao dịch|
|» taxRate|integer(int32)|false|none|Tỷ lệ thuế|
|» exchangeFeeRate|integer(int32)|false|none|Tỷ lệ phí trả Sở giao dịch|
|» feeRate|integer(int32)|false|none|Tổng tỷ lệ phí của lệnh|
|» leaveQuantity|integer(int32)|false|none|Khối lượng còn lại chưa khớp|
|» canceledQuantity|integer(int32)|false|none|Khối lượng đã hủy|
|» error|string|false|none|Mã lỗi nếu lệnh bị từ chối|
|» marketType|string|false|none|Loại thị trường<br>- STOCK: Sổ lệnh cơ sở<br>- DERIVATIVE: Sổ lệnh phái sinh|
|» priceSecure|number(double)|false|none|Giá dùng để kiểm tra sức mua/đặt lệnh|
|» createdDate|string(date-time)|false|none|Thời điểm tạo lệnh|
|» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật lệnh|
|» metadata|string|false|none|Thông tin bổ sung của lệnh|
|» reports|[any]|false|none|Danh sách trạng thái lệnh cơ sở theo từng lần cập nhật|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Đóng vị thế

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="closePosition"></span>

### `POST /accounts/positions/{positionId}/close`

<h3 id="closeposition-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marketType|query|string|true|Loại thị trường |
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|trading-token|header|string|true|Token đặt lệnh|
|positionId|path|string|true|Id vị thế|

#### Detailed descriptions

**marketType**: Loại thị trường 
- STOCK: Danh sách Deal cơ sở
- DERIVATIVE: Danh sách Deal phái sinh
Hiện tại chỉ hỗ trợ phái sinh

> Code samples

```shell
# You can also use wget
curl -X POST https://openapi.dnse.com.vn/accounts/positions/{positionId}/close?marketType=DERIVATIVE \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Signature: your_signature' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'trading-token: 7ceef658-9f01-414e-8b3e-faa77bb9061e'

```

```http
POST https://openapi.dnse.com.vn/accounts/positions/{positionId}/close?marketType=DERIVATIVE HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Signature: your_signature
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
trading-token: 7ceef658-9f01-414e-8b3e-faa77bb9061e

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Signature": []string{"your_signature"},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "trading-token": []string{"7ceef658-9f01-414e-8b3e-faa77bb9061e"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://openapi.dnse.com.vn/accounts/positions/{positionId}/close", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Signature':'your_signature',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'trading-token':'7ceef658-9f01-414e-8b3e-faa77bb9061e'
};

fetch('https://openapi.dnse.com.vn/accounts/positions/{positionId}/close?marketType=DERIVATIVE',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Signature': 'your_signature',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'trading-token': '7ceef658-9f01-414e-8b3e-faa77bb9061e'
}

r = requests.post('https://openapi.dnse.com.vn/accounts/positions/{positionId}/close', params={
  'marketType': 'DERIVATIVE'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/accounts/positions/{positionId}/close?marketType=DERIVATIVE");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "id": 1636,
  "side": "NS",
  "accountNo": "0001179019",
  "symbol": "41I1G4000",
  "price": 1618.2,
  "quantity": 1,
  "orderType": "LO",
  "fillQuantity": 0,
  "leaveQuantity": 0,
  "canceledQuantity": 0,
  "loanPackageId": 2278,
  "createdDate": "2026-03-24T04:20:55.63",
  "modifiedDate": "2026-03-24T04:20:55.63"
}
```

<h3 id="closeposition-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer(int32)|false|none|Id lệnh giao dịch|
|» side|string|false|none|Chiều đặt lệnh<br>- NB: Mua<br>- NS: Bán|
|» accountNo|string|false|none|Số tiểu khoản|
|» symbol|string|false|none|Mã chứng khoán|
|» price|number(double)|false|none|Giá đặt|
|» quantity|integer(int32)|false|none|Khối lượng đặt|
|» orderType|string|false|none|Loại lệnh<br>- LO: Lệnh giới hạn<br>- MOK/MAK/MTL: Lệnh thị trường<br>- ATO/ATC: Lệnh phiên định kỳ mở cửa/đóng cửa<br>- PLO: Lệnh khớp lệnh sau giờ|
|» fillQuantity|integer(int32)|false|none|Khối lượng khớp|
|» leaveQuantity|integer(int32)|false|none|Khối lượng còn lại|
|» canceledQuantity|integer(int32)|false|none|Khối lượng đã hủy|
|» loanPackageId|integer(int32)|false|none|Mã gói vay|
|» createdDate|string(date-time)|false|none|Thời điểm tạo|
|» modifiedDate|string(date-time)|false|none|Thời điểm cập nhật|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

<h1 id="dnse-openapi-v2-market-data">market-data</h1>
## Thông tin giao dịch chứng khoán

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getSymbolSecdef"></span>

### `GET /price/{symbol}/secdef`

<h3 id="getsymbolsecdef-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boardId|query|string|false|Mã bảng giao dịch|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|symbol|path|string|true|Mã chứng khoán|

#### Detailed descriptions

**boardId**: Mã bảng giao dịch
- G1: Lô chẵn
- G4: Lô lẻ
- T1: Thỏa thuận trong giờ (9h - 14h45)
- T3: Thỏa thuận sau giờ (14h45 - 15h)
- T4: Thỏa thuận lô lẻ trong giờ (9h - 14h45)
- T6: Thỏa thuận lô lẻ sau giờ  (14h45 - 15h)

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/price/{symbol}/secdef \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/price/{symbol}/secdef HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/price/{symbol}/secdef", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/price/{symbol}/secdef',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/price/{symbol}/secdef', headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/price/{symbol}/secdef");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
[
  {
    "marketId": "STO",
    "boardId": "G1",
    "isin": "VN000000HPG4",
    "symbol": "HPG",
    "productGrpId": "STO",
    "securityGroupId": "ST",
    "basicPrice": 26.8,
    "ceilingPrice": 28.65,
    "floorPrice": 24.95,
    "securityStatus": "UNSPECIFIED",
    "symbolAdminStatusCode": "NRM",
    "symbolTradingMethodStatusCode": "NRM",
    "symbolTradingSanctionStatusCode": "NRM"
  }
]
```

<h3 id="getsymbolsecdef-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» marketId|string|false|none|Mã thị trường niêm yết mã chứng khoán<br>- DVX: Phái sinh sàn HNX<br>- HCX: Trái phiếu doanh nghiệp HNX<br>- STO: Cổ phiếu sàn HOSE<br>- STX: Cổ phiếu sàn HNX<br>- UPX: Cổ phiếu sàn Upcom|
|» boardId|string|false|none|Mã bảng giao dịch<br>- G1: Lô chẵn<br>- G4: Lô lẻ<br>- T1: Thỏa thuận trong giờ (9h - 14h45)<br>- T3: Thỏa thuận sau giờ (14h45 - 15h)<br>- T4: Thỏa thuận lô lẻ trong giờ (9h - 14h45)<br>- T6: Thỏa thuận lô lẻ sau giờ (14h45 - 15h)|
|» isin|string|false|none|Mã định danh quốc tế|
|» symbol|string|false|none|Mã chứng khoán|
|» productGrpId|string|false|none|Nhóm sản phẩm theo thị trường<br>-FBX: Hợp đồng tương lai Trái phiếu<br>-FIO: Hợp đồng tương lai Chỉ số<br>-HCX: Trái phiếu Doanh nghiệp HNX<br>-STO: Cổ phiếu sàn HOSE<br>-STX: Cổ phiếu sàn HNX<br>-UPX: Cổ phiếu sàn Upcom|
|» securityGroupId|string|false|none|Nhóm chứng khoán<br>- BS: Trái phiếu doanh nghiệp<br>- EF: Quỹ ETF<br>- EW: Chứng quyền<br>- FU: Hợp đồng tương lai<br>- ST: Cổ phiếu|
|» basicPrice|number(double)|false|none|Giá tham chiếu ngày giao dịch|
|» ceilingPrice|number(double)|false|none|Giá trần ngày giao dịch|
|» floorPrice|number(double)|false|none|Giá sàn ngày giao dịch|
|» securityStatus|string|false|none|Trạng thái giao dịch của mã chứng khoán<br>- HALT: Ngừng giao dịch<br>- NO_HALT: Không ngừng giao dịch|
|» symbolAdminStatusCode|string|false|none|Trạng thái quản lý hành chính mã chứng khoán<br>- CR: Kiểm soát và hạn chế giao dịch<br>- CTR: Kiểm soát<br>- NRM: Bình thường<br>- RES: Hạn chế giao dịch<br>- WFR: Cảnh báo vi phạm BCTC<br>- WID: Cảnh báo vi phạm CBTT<br>- WOV: Cảnh báo vi phạm khác|
|» symbolTradingMethodStatusCode|string|false|none|Trạng thái cơ chế giao dịch mã chứng khoán<br>- NRM: Bình thường<br>- NWE: Niêm yết mới (biên độ đặc biệt)<br>- NWN: Niêm yết mới (biên độ thường)<br>- SLS: Giao dịch đặc biệt sau tạm ngưng<br>- SNE: Giao dịch đặc biệt không có giao dịch dài hạn|
|» symbolTradingSanctionStatusCode|string|false|none|Tình trạng giao dịch của mã chứng khoán<br>- NRM: Bình thường<br>- SUS: Tạm ngừng giao dịch<br>- DTL: Hủy niêm yết để chuyển sàn<br>- TFR: Ngưng giao dịch do hạn chế|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Giá đóng cửa

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getPriceSymbolClose"></span>

### `GET /price/{symbol}/close`

<h3 id="getpricesymbolclose-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boardId|query|string|false|Mã bảng giao dịch|
|X-API-Key|header|string|false|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|false|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|false|Chữ ký xác thực yêu cầu|
|symbol|path|string|true|Mã chứng khoán|

#### Detailed descriptions

**boardId**: Mã bảng giao dịch
- G1: Lô chẵn
- G4: Lô lẻ
- T1: Thỏa thuận trong giờ (9h - 14h45)
- T3: Thỏa thuận sau giờ (14h45 - 15h)
- T4: Thỏa thuận lô lẻ trong giờ (9h - 14h45)
- T6: Thỏa thuận lô lẻ sau giờ  (14h45 - 15h)

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/price/{symbol}/close \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/price/{symbol}/close HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/price/{symbol}/close", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/price/{symbol}/close',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/price/{symbol}/close', headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/price/{symbol}/close");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "prices": [
    {
      "marketId": "STO",
      "boardId": "G1",
      "isin": "VN000000HPG4",
      "symbol": "HPG",
      "closePrice": 26.8,
      "time": "2026-04-08 02:14:59"
    }
  ]
}
```

<h3 id="getpricesymbolclose-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» prices|[object]|false|none|none|
|»» marketId|string|false|none|Mã thị trường niêm yết mã chứng khoán<br>- DVX: Phái sinh sàn HNX<br>- HCX: Trái phiếu doanh nghiệp HNX<br>- STO: Cổ phiếu sàn HOSE<br>- STX: Cổ phiếu sàn HNX<br>- UPX: Cổ phiếu sàn Upcom|
|»» boardId|string|false|none|Mã bảng giao dịch<br>- G1: Lô chẵn<br>- G4: Lô lẻ<br>- T1: Thỏa thuận trong giờ (9h - 14h45)<br>- T3: Thỏa thuận sau giờ (14h45 - 15h)<br>- T4: Thỏa thuận lô lẻ trong giờ (9h - 14h45)<br>- T6: Thỏa thuận lô lẻ sau giờ (14h45 - 15h)|
|»» isin|string|false|none|Mã định danh quốc tế|
|»» symbol|string|false|none|Mã chứng khoán|
|»» closePrice|number(double)|false|none|Giá đóng cửa gần nhất|
|»» time|string|false|none|Thời gian ghi nhận|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Chi tiết mã chứng khoán

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getInstruments"></span>

### `GET /instruments`

<h3 id="getinstruments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|query|string|true|Danh sách mã chứng khoán|
|marketId|query|string|false|Mã thị trường niêm yết|
|securityGroupId|query|string|false|Nhóm chứng khoán|
|indexName|query|string|false|Chỉ số thị trường |
|limit|query|integer|false|Số bản ghi trên mỗi trang|
|page|query|integer|false|Phân trang hiện tại|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|

#### Detailed descriptions

**marketId**: Mã thị trường niêm yết
- STO: Cổ phiếu sàn HOSE
- STX: Cổ phiếu sàn HNX
- UPX: Cổ phiếu sàn UPCOM
- DVX: Phái sinh
- HCX: Trái phiếu doanh nghiệp

**securityGroupId**: Nhóm chứng khoán
- ST: Cổ phiếu
- EF: Quỹ ETF
- EW: Chứng quyền
- FU: Hợp đồng tương lai
- BS: Trái phiếu

**indexName**: Chỉ số thị trường 
- VN30: Top 30 cổ phiếu sàn HOSE
- VN100: Top 100 cổ phiếu sàn HOSE
- HNX30: Top 30 cổ phiếu sàn HNX

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/instruments?symbol=SSI%2CSHS%2CACB%2CHUT%2CDSE \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/instruments?symbol=SSI%2CSHS%2CACB%2CHUT%2CDSE HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/instruments", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/instruments?symbol=SSI%2CSHS%2CACB%2CHUT%2CDSE',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/instruments', params={
  'symbol': 'SSI,SHS,ACB,HUT,DSE'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/instruments?symbol=SSI%2CSHS%2CACB%2CHUT%2CDSE");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "symbol": "ACB",
      "marketId": "STO",
      "securityGroupId": "ST",
      "symbolType": "",
      "listedDate": "2020-12-09",
      "shortName": "Ngân hàng Á Châu",
      "name": "Ngân hàng TMCP Á Châu",
      "indexName": [
        "VN100",
        "VN30"
      ]
    }
  ],
  "total": 5,
  "page": 1,
  "pageSize": 100
}
```

<h3 id="getinstruments-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[object]|false|none|Danh sách thông tin mã chứng khoán|
|»» symbol|string|false|none|Mã chứng khoán|
|»» marketId|string|false|none|Mã thị trường niêm yết<br>- STO: Cổ phiếu sàn HOSE<br>- STX: Cổ phiếu sàn HNX<br>- UPX: Cổ phiếu sàn UPCOM<br>- DVX: Phái sinh<br>- HCX: Trái phiếu doanh nghiệp|
|»» securityGroupId|string|false|none|Nhóm chứng khoán<br>- ST: Cổ phiếu<br>- EF: Quỹ ETF<br>- EW: Chứng quyền<br>- FU: Hợp đồng tương lai<br>- BS: Trái phiếu|
|»» symbolType|string|false|none|Phân loại mã hợp đồng phái sinh theo thời gian đáo hạn (áp dụng cho DERIVATIVE)<br>- VN30F1M: HĐTL chỉ số VN30 1 tháng<br>- VN30F2M: HĐTL chỉ số VN30 2 tháng<br>- VN30F1Q: HĐTL chỉ số VN30 1 quý<br>- VN30F2Q: HĐTL chỉ số VN30 2 quý|
|»» listedDate|string|false|none|Ngày niêm yết|
|»» shortName|string|false|none|Tên viết tắt của tổ chức phát hành|
|»» name|string|false|none|Tên đầy đủ của tổ chức phát hành|
|»» indexName|[string]|false|none|Danh sách chỉ số mà mã chứng khoán thuộc về (nếu có)|
|» total|integer(int32)|false|none|Tổng số bản ghi|
|» page|integer(int32)|false|none|Trang hiện tại (bắt đầu từ 1)|
|» pageSize|integer(int32)|false|none|Số bản ghi trên mỗi trang|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Lịch sử OHLC

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getOhlcHistory"></span>

### `GET /price/ohlc`

<h3 id="getohlchistory-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|query|string|true|Mã chứng khoán |
|type|query|string|true|Loại thị trường|
|resolution|query|string|true|Khung thời gian nến|
|from|query|string|true|Thời gian bắt đầu|
|to|query|string|true|Thời gian kết thúc|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|

#### Detailed descriptions

**type**: Loại thị trường
- STOCK: Cổ phiếu
- DERIVATIVE: Phái sinh
- INDEX: Chỉ số thị trường

**resolution**: Khung thời gian nến
- 1,3,5,15,30,1h,1D,1W

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/price/ohlc?symbol=ACB&type=STOCK&resolution=15&from=1773657310&to=1773830110 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/price/ohlc?symbol=ACB&type=STOCK&resolution=15&from=1773657310&to=1773830110 HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/price/ohlc", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/price/ohlc?symbol=ACB&type=STOCK&resolution=15&from=1773657310&to=1773830110',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/price/ohlc', params={
  'symbol': 'ACB',  'type': 'STOCK',  'resolution': '15',  'from': '1773657310',  'to': '1773830110'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/price/ohlc?symbol=ACB&type=STOCK&resolution=15&from=1773657310&to=1773830110");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "t": [
    1773715500
  ],
  "o": [
    23.8
  ],
  "h": [
    23.8
  ],
  "l": [
    23.7
  ],
  "c": [
    23.75
  ],
  "v": [
    2530900
  ],
  "nextTime": 0
}
```

<h3 id="getohlchistory-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» t|[integer]|false|none|Danh sách thời gian nến|
|» o|[number]|false|none|Danh sách giá mở cửa của nến theo thời gian tương ứng|
|» h|[number]|false|none|Danh sách giá cao nhất trong nến theo thời gian tương ứng|
|» l|[number]|false|none|Danh sách giá thấp nhất trong nến theo thời gian tương ứng|
|» c|[number]|false|none|Danh sách giá đóng cửa của nến theo thời gian tương ứng|
|» v|[integer]|false|none|Danh sách khối lượng giao dịch theo thời gian tương ứng|
|» nextTime|integer(int32)|false|none|Timestamp của cây nến tiếp theo (nếu có), 0 nếu không còn|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Lịch sử khớp lệnh

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getHistoryTrades"></span>

### `GET /price/{symbol}/trades`

<h3 id="gethistorytrades-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boardId|query|string|true|Mã bảng giao dịch|
|from|query|string|true|Thời gian bắt đầu (timestamp)|
|to|query|string|true|Thời gian kết thúc (timestamp)|
|limit|query|number|false|none|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|symbol|path|string|true|Mã chứng khoán|

#### Detailed descriptions

**boardId**: Mã bảng giao dịch
- G1: Lô chẵn
- G4: Lô lẻ
- T1: Thỏa thuận trong giờ (9h - 14h45)
- T3: Thỏa thuận sau giờ (14h45 - 15h)
- T4: Thỏa thuận lô lẻ trong giờ (9h - 14h45)
- T6: Thỏa thuận lô lẻ sau giờ  (14h45 - 15h)

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/price/{symbol}/trades?boardId=G1&from=1773282637&to=1773289837 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/price/{symbol}/trades?boardId=G1&from=1773282637&to=1773289837 HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/price/{symbol}/trades", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/price/{symbol}/trades?boardId=G1&from=1773282637&to=1773289837',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/price/{symbol}/trades', params={
  'boardId': 'G1',  'from': '1773282637',  'to': '1773289837'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/price/{symbol}/trades?boardId=G1&from=1773282637&to=1773289837");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "trades": [
    {
      "marketId": "STO",
      "boardId": "G1",
      "isin": "VN000000ACB8",
      "symbol": "ACB",
      "matchPrice": 22.85,
      "matchQtty": 10,
      "side": "UNSPECIFIED",
      "avgPrice": 22.958,
      "totalVolumeTraded": 764430,
      "grossTradeAmount": 175.49849,
      "highestPrice": 23.25,
      "lowestPrice": 22.75,
      "openPrice": 23,
      "time": "2026-03-12 04:29:57"
    }
  ],
  "nextPageToken": "NDYwMTQ1XzIwMjYtMDMtMTJUMDQ6MjU6MDUuNTZa"
}
```

<h3 id="gethistorytrades-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» trades|[object]|false|none|Danh sách giao dịch|
|»» marketId|string|false|none|Mã thị trường|
|»» boardId|string|false|none|Mã bảng giao dịch|
|»» isin|string|false|none|Mã định danh quốc tế|
|»» symbol|string|false|none|Mã chứng khoán|
|»» matchPrice|number(double)|false|none|Giá khớp gần nhất|
|»» matchQtty|integer(int32)|false|none|Khối lượng khớp gần nhất|
|»» side|string|false|none|Chiều giao dịch|
|»» avgPrice|number(double)|false|none|Giá khớp trung bình|
|»» totalVolumeTraded|integer(int32)|false|none|Tổng khối lượng giao dịch trong ngày|
|»» grossTradeAmount|number(double)|false|none|Tổng giá trị giao dịch trong ngày|
|»» highestPrice|number(float)|false|none|Giá cao nhất trong ngày|
|»» lowestPrice|number(float)|false|none|Giá thấp nhất trong ngày|
|»» openPrice|integer(int32)|false|none|Giá mở cửa|
|»» time|string|false|none|Thời gian ghi nhận|
|» nextPageToken|string|false|none|Token dùng để lấy trang tiếp theo|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
## Dữ liệu khớp gần nhất

### Base URLs:
- **https://openapi.dnse.com.vn**

<span id="getLatestTrades"></span>

### `GET /price/{symbol}/trades/latest`

<h3 id="getlatesttrades-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boardId|query|string|true|Mã bảng giao dịch|
|X-API-Key|header|string|true|API Key được cấp khi đăng ký dịch vụ|
|X-Aux-Date|header|string|true|Thời gian thực hiện yêu cầu|
|X-Signature|header|string|true|Chữ ký xác thực yêu cầu|
|symbol|path|string|true|Mã chứng khoán |

#### Detailed descriptions

**boardId**: Mã bảng giao dịch
- G1: Lô chẵn
- G4: Lô lẻ
- T1: Thỏa thuận trong giờ (9h - 14h45)
- T3: Thỏa thuận sau giờ (14h45 - 15h)
- T4: Thỏa thuận lô lẻ trong giờ (9h - 14h45)
- T6: Thỏa thuận lô lẻ sau giờ  (14h45 - 15h)

> Code samples

```shell
# You can also use wget
curl -X GET https://openapi.dnse.com.vn/price/{symbol}/trades/latest?boardId=G1 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==' \
  -H 'X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000' \
  -H 'X-Signature: your_signature'

```

```http
GET https://openapi.dnse.com.vn/price/{symbol}/trades/latest?boardId=G1 HTTP/1.1
Host: openapi.dnse.com.vn
Accept: application/json
X-API-Key: eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==
X-Aux-Date: Mon, 19 Jan 2026 07:45:23 +0000
X-Signature: your_signature

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ=="},
        "X-Aux-Date": []string{"Mon, 19 Jan 2026 07:45:23 +0000"},
        "X-Signature": []string{"your_signature"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://openapi.dnse.com.vn/price/{symbol}/trades/latest", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date':'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature':'your_signature'
};

fetch('https://openapi.dnse.com.vn/price/{symbol}/trades/latest?boardId=G1',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'eyJvcmciOiJkbnNlIiwiaWQiOiI5YmMzYmViN2JjY2U0MmE0Yjk1NDE0MTA2YTMzODIxNyIsImgiOiJtdXJtdXIxMjgifQ==',
  'X-Aux-Date': 'Mon, 19 Jan 2026 07:45:23 +0000',
  'X-Signature': 'your_signature'
}

r = requests.get('https://openapi.dnse.com.vn/price/{symbol}/trades/latest', params={
  'boardId': 'G1'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("https://openapi.dnse.com.vn/price/{symbol}/trades/latest?boardId=G1");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

> Example responses

> 200 Response

```json
{
  "trades": [
    {
      "marketId": "STO",
      "boardId": "G1",
      "isin": "VN000000ACB8",
      "symbol": "ACB",
      "matchPrice": 23.35,
      "matchQtty": 20,
      "side": "SELL",
      "avgPrice": 23.435,
      "totalVolumeTraded": 427980,
      "grossTradeAmount": 100.295515,
      "highestPrice": 23.55,
      "lowestPrice": 23.35,
      "openPrice": 23.5,
      "time": "2026-03-19 04:08:29"
    }
  ]
}
```

<h3 id="getlatesttrades-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» trades|[object]|false|none|none|
|»» marketId|string|false|none|Mã thị trường niêm yết mã chứng khoán<br>- DVX: Phái sinh sàn HNX<br>- HCX: Trái phiếu doanh nghiệp HNX<br>- STO: Cổ phiếu sàn HOSE<br>- STX: Cổ phiếu sàn HNX<br>- UPX: Cổ phiếu sàn Upcom|
|»» boardId|string|false|none|Mã bảng giao dịch<br>- G1: Lô chẵn<br>- G4: Lô lẻ<br>- T1: Thỏa thuận trong giờ (9h - 14h45)<br>- T3: Thỏa thuận sau giờ (14h45 - 15h)<br>- T4: Thỏa thuận lô lẻ trong giờ (9h - 14h45)<br>- T6: Thỏa thuận lô lẻ sau giờ (14h45 - 15h)|
|»» isin|string|false|none|Mã định danh quốc tế|
|»» symbol|string|false|none|Mã chứng khoán|
|»» matchPrice|number(double)|false|none|Giá khớp lệnh của giao dịch|
|»» matchQtty|integer(int32)|false|none|Khối lượng khớp của giao dịch|
|»» side|string|false|none|Phía giao dịch chủ động<br>- BUY: Bên mua chủ động<br>- SELL: Bên bán chủ động|
|»» avgPrice|number(double)|false|none|Giá khớp trung bình|
|»» totalVolumeTraded|integer(int32)|false|none|Tổng khối lượng đã giao dịch trong ngày|
|»» grossTradeAmount|number(double)|false|none|Tổng giá trị giao dịch trong nngày|
|»» highestPrice|number(double)|false|none|Giá khớp cao nhất trong ngày|
|»» lowestPrice|number(double)|false|none|Giá khớp thấp nhất trong ngày|
|»» openPrice|number(float)|false|none|Giá mở cửa|
|»» time|string|false|none|Thời gian khớp lệnh (theo định dạng yyyy-MM-dd HH:mm:ss)|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|string|false|none|none|
|» message|string|false|none|none|
|» status|integer|false|none|none|
