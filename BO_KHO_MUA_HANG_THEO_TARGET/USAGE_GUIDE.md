# USAGE GUIDE - Hướng Dẫn Sử Dụng Chi Tiết

Hướng dẫn sử dụng hệ thống mua hàng tự động từng bước.

---

## 🎯 Mục Lục

1. [Setup Ban Đầu](#setup-ban-đầu)
2. [Workflow Hoàn Chỉnh](#workflow-hoàn-chỉnh)
3. [Commands Chi Tiết](#commands-chi-tiết)
4. [Tips & Best Practices](#tips--best-practices)
5. [Troubleshooting](#troubleshooting)

---

## 🚀 Setup Ban Đầu

### Bước 1: Cài Đặt Python Dependencies

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
pip install -r tools/requirements.txt
```

**Kiểm tra cài đặt thành công:**
```bash
python -c "import google.auth; print('OK')"
```

### Bước 2: Cấu Hình Credentials

**Copy credentials:**
```bash
cp c:\Users\nguye\Desktop\AI\config\service-account-key.json config/
```

**Kiểm tra file:**
```bash
ls config/service-account-key.json
```

### Bước 3: Test Kết Nối Google Sheets

*(Coming soon - Python script test_connection.py)*

---

## 🔄 Workflow Hoàn Chỉnh

### Scenario 1: Tính Nhu Cầu + Tạo Phiếu Mua Hàng

#### Bước 1: Tính VTTH

```bash
/tinh-vtth 300
```

**Output:**
```
✅ Đã tính VTTH cho 300 khách - B2B-Gói đồng

| STT | Tên Sản Phẩm | Định mức | Nhu cầu (lọ) | Số lượng (Hộp) |
|-----|--------------|----------|--------------|----------------|
| 1   | Lammen 22x22 | 0.5      | 150          | 2              |
...

📊 Tổng: 25 loại VTTH
💾 Đã lưu vào: workspace/calculations/vtth_20250202_143052.json
```

#### Bước 2: Tính Hóa Chất

```bash
/tinh-hoa-chat 300
```

**Hệ thống sẽ hỏi:**
```
❓ Bạn có muốn thêm QC & CALIB riêng không?
Trả lời: CÓ / KHÔNG
```

**Trả lời:** `CÓ`

**Output:**
```
✅ Đã tính Hóa Chất cho 300 khách - B2B-Gói đồng

| STT | Tên HC | Test KH | QC | Cal | Tổng | Lọ | Hộp |
|-----|--------|---------|----|----|------|-----|-----|
| 1   | GLUCOSE| 300     | 2  | 4  | 306  | 4   | 1   |
...

📊 Tổng: 23 loại hóa chất (bao gồm QC/CALIB bổ sung)
💾 Đã lưu vào: workspace/calculations/hoa_chat_20250202_143052.json
```

#### Bước 3: Chuẩn Bị File Tồn Kho

**Format file Excel:**

| Tên sản phẩm | Tồn kho |
|--------------|---------|
| Lammen 22x22 | 0       |
| GLUCOSE GLU 440 | 1.2  |
| ALT          | 0.5     |

**Lưu file vào:** `workspace/inventory-files/ton-kho-thang-2.xlsx`

#### Bước 4: So Sánh Tồn Kho

```bash
/so-sanh-kho workspace/inventory-files/ton-kho-thang-2.xlsx
```

**Output:**
```
✅ Đã so sánh với tồn kho!

## 🔴 CẦN MUA (15 loại)
...

## ✅ ĐỦ KHO (10 loại)
...

📊 Tổng kết:
- Tổng loại: 25
- CẦN MUA: 15 loại
- ĐỦ KHO: 10 loại

❓ Bạn có muốn tạo Phiếu Mua Hàng không?
Trả lời: CÓ / KHÔNG
```

**Trả lời:** `CÓ`

#### Bước 5: Tạo Phiếu Tự Động

```
✅ Đã tạo Phiếu Mua Hàng thành công!

📋 Thông tin phiếu:
- Tên sheet: Phiếu_20250202_143052
- Link: https://docs.google.com/spreadsheets/d/1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800

📊 Tóm tắt:
- Số lượng mặt hàng: 15
- Tổng SL cần mua: 8 hộp
- Gói dịch vụ: B2B-Gói đồng
- Số khách hàng: 300

🔗 [Mở Phiếu](https://docs.google.com/spreadsheets/d/...)
```

#### Bước 6: Kiểm Tra Phiếu

1. Mở link Google Sheets
2. Kiểm tra sheet mới `Phiếu_20250202_143052`
3. Xác nhận:
   - Header đã điền đúng
   - Danh sách sản phẩm đầy đủ
   - Số lượng đúng (đơn vị lớn, đã ROUNDUP)
   - Format giữ nguyên từ template

---

## 📝 Commands Chi Tiết

### /kho - Menu Chính

**Sử dụng:**
```bash
/kho
```

**Khi nào dùng:**
- User mới, chưa quen workflow
- Muốn xem các lựa chọn có sẵn

**Output:**
```
Xin chào! 👋 Tôi có thể giúp gì?

1️⃣ Tính VTTH
2️⃣ Tính Hóa Chất
3️⃣ So sánh tồn kho & tạo phiếu

Chọn số (1, 2 hoặc 3):
```

---

### /tinh-vtth - Tính VTTH

**Syntax:**
```bash
/tinh-vtth <số_khách> [gói_dv]
```

**Ví dụ:**
```bash
# Gói đồng (mặc định)
/tinh-vtth 300

# Gói cơ bản
/tinh-vtth 150 B2B-Gói cơ bản

# Gói bạc
/tinh-vtth 500 B2B-Gói bạc
```

**Khi nào dùng:**
- Cần tính vật tư tiêu hao cho số khách mới
- Đầu workflow (bước 1)

**Output:**
- Bảng danh sách VTTH
- Số lượng cần (đơn vị nhỏ và lớn)
- File JSON lưu kết quả

---

### /tinh-hoa-chat - Tính Hóa Chất

**Syntax:**
```bash
/tinh-hoa-chat <số_khách> [gói_dv]
```

**Ví dụ:**
```bash
/tinh-hoa-chat 300
/tinh-hoa-chat 150 B2B-Gói cơ bản
```

**Khi nào dùng:**
- Cần tính hóa chất cho số khách mới
- Đầu workflow (bước 1)

**⭐ Đặc biệt:**
- LUÔN hỏi về QC/CALIB bổ sung
- Tự động tra cứu QC/CALIB từ sheet "Hoa Chat"
- Lọc từ sheet "Hoa Chat Chi Tiet" (QUAN TRỌNG!)

**Output:**
- Bảng danh sách hóa chất
- Số test khách + QC + Calib
- Có/không có QC/CALIB bổ sung
- File JSON lưu kết quả

---

### /so-sanh-kho - So Sánh Tồn Kho

**Syntax:**
```bash
/so-sanh-kho <file_path>
```

**Ví dụ:**
```bash
/so-sanh-kho workspace/inventory-files/ton-kho.xlsx
/so-sanh-kho ../data/inventory.csv
/so-sanh-kho D:/kho/ton-kho-thang-2.xlsx
```

**Yêu cầu:**
- Phải chạy `/tinh-vtth` hoặc `/tinh-hoa-chat` trước
- File phải là `.xlsx` hoặc `.csv`
- File phải có cột "Tên sản phẩm" và "Tồn kho"

**Khi nào dùng:**
- Sau khi đã tính VTTH hoặc HC
- Có file tồn kho mới nhất
- Muốn xác định số lượng cần mua

**Output:**
- 2 bảng: CẦN MUA và ĐỦ KHO
- Hiển thị cả đơn vị nhỏ và lớn
- Hỏi có muốn tạo phiếu không

---

### /tao-phieu - Tạo Phiếu Mua Hàng

**Syntax:**
```bash
/tao-phieu
```

**Yêu cầu:**
- Phải chạy `/so-sanh-kho` trước
- Có ít nhất 1 item CẦN MUA

**Khi nào dùng:**
- Sau khi so sánh tồn kho
- Có items CẦN MUA
- Muốn tạo phiếu chính thức

**Output:**
- Link Google Sheets
- Tên sheet mới
- Tổng số mặt hàng
- Tổng số lượng

**Phiếu được lưu ở:**
- Google Sheets: Sheet mới `Phiếu_YYYYMMDD_HHMMSS`
- Metadata: Sheet "Phiếu Mua Hàng"
- Chi tiết: Sheet "Chi Tiết Phiếu Mua Hàng"

---

## 💡 Tips & Best Practices

### 1. Quy Đổi Đơn Vị

**⭐ QUY TẮC VÀNG:**
```
SO SÁNH TỒN KHO: Đơn vị nhỏ
PHIẾU MUA HÀNG: Đơn vị lớn + ROUNDUP
```

**Ví dụ:**
```
Cần: 150 lọ
Tồn: 1.2 hộp = 120 lọ
→ Cần mua: 30 lọ = 1 hộp (ROUNDUP)
```

### 2. File Tồn Kho

**Best Practices:**
- Đặt tên rõ ràng: `ton-kho-2025-02-02.xlsx`
- Lưu trong `workspace/inventory-files/`
- Update định kỳ (hàng tuần)
- Giữ lịch sử files cũ

**Format Excel:**
```
| Tên sản phẩm       | Tồn kho | Ghi chú          |
|--------------------|---------|------------------|
| GLUCOSE GLU 440    | 1.2     | 1.2 hộp          |
| Lammen 22x22       | 0       | Hết kho          |
| ALT                | 0.5     | Sắp hết          |
```

### 3. Lưu Kết Quả

**Tự động lưu:**
- VTTH: `workspace/calculations/vtth_*.json`
- HC: `workspace/calculations/hoa_chat_*.json`
- Comparison: `workspace/calculations/comparison_*.json`

**Dọn dẹp:**
```bash
# Xóa file > 30 ngày
find workspace/calculations/ -name "*.json" -mtime +30 -delete
```

### 4. Kiểm Tra Phiếu

**Checklist sau khi tạo phiếu:**
- [ ] Ngày lập đúng?
- [ ] Người đề nghị: Phòng Xét Nghiệm?
- [ ] Nội dung: Đúng số khách và gói?
- [ ] Số lượng mặt hàng khớp với CẦN MUA?
- [ ] Đơn vị lớn (Hộp, Chai, Thùng)?
- [ ] Số lượng đã ROUNDUP?
- [ ] Format giữ nguyên từ template?

### 5. QC/CALIB Bổ Sung

**Khi nào chọn CÓ:**
- Đợt khách lớn (>200 khách)
- Lâu chưa mua QC/CALIB
- Sắp hết QC/CALIB

**Khi nào chọn KHÔNG:**
- Vừa mua QC/CALIB
- Đợt khách nhỏ (<100 khách)
- Đủ QC/CALIB trong kho

---

## 🐛 Troubleshooting

### Lỗi 1: Sheet "Hoa Chat Chi Tiet" not found

**Nguyên nhân:**
- Sai tên sheet
- Chưa share spreadsheet với service account

**Giải pháp:**
1. Kiểm tra spreadsheet ID đúng
2. Share với service account email
3. Kiểm tra tên sheet chính xác: "Hoa Chat Chi Tiet" (có dấu cách)

### Lỗi 2: Permission Denied

**Nguyên nhân:**
- Credentials không đúng
- Chưa share spreadsheet

**Giải pháp:**
1. Kiểm tra file `config/service-account-key.json`
2. Share spreadsheet với email trong credentials
3. Cấp quyền "Editor"

### Lỗi 3: Thiếu Hóa Chất

**Nguyên nhân:**
- Lọc sai sheet
- Điều kiện lọc sai

**Giải pháp:**
1. Kiểm tra đọc sheet "Hoa Chat Chi Tiet" (KHÔNG phải "Hoa Chat")
2. Kiểm tra điều kiện: Loại = "Chạy mẫu" + Gói có "x"
3. In ra số lượng rows để debug

### Lỗi 4: Tồn Kho Không Khớp

**Nguyên nhân:**
- Tên sản phẩm không khớp
- Format tên khác nhau

**Giải pháp:**
1. Chuẩn hóa tên: lowercase, strip whitespace
2. Kiểm tra spelling
3. Xem log matching để debug

### Lỗi 5: Copy Template Failed

**Nguyên nhân:**
- Template không tồn tại
- Permissions không đủ

**Giải pháp:**
1. Kiểm tra sheet "Phiếu mua hàng mẫu version 1" tồn tại
2. Kiểm tra permissions
3. Thử copy manual để test

---

## 📊 Scenarios Thực Tế

### Scenario 1: Đợt Khách Nhỏ (50 khách)

```bash
# Tính HC thôi (bỏ qua VTTH)
/tinh-hoa-chat 50

# Không cần QC/CALIB bổ sung
→ Trả lời: KHÔNG

# So sánh
/so-sanh-kho workspace/inventory-files/ton-kho.xlsx

# Tạo phiếu (nếu cần)
→ Trả lời: CÓ
```

### Scenario 2: Đợt Khách Lớn (500 khách)

```bash
# Tính cả VTTH và HC
/tinh-vtth 500
/tinh-hoa-chat 500

# CÓ QC/CALIB bổ sung
→ Trả lời: CÓ

# So sánh
/so-sanh-kho workspace/inventory-files/ton-kho.xlsx

# Tạo phiếu
→ Trả lời: CÓ
```

### Scenario 3: Kiểm Tra Trước Khi Mua

```bash
# Tính nhu cầu
/tinh-hoa-chat 300

# So sánh để xem
/so-sanh-kho workspace/inventory-files/ton-kho.xlsx

# KHÔNG tạo phiếu ngay
→ Trả lời: KHÔNG

# Review kết quả, quyết định sau
```

---

## 🎓 Video Tutorials

*(Coming soon)*

- Setup Google Sheets API
- Workflow đầu tiên
- Troubleshooting thường gặp

---

## 📞 Support

**Documentation:**
- `CLAUDE.md` - AI instructions
- `context/` - Detailed guides
- Agent files - Specific workflows

**Google Sheets:**
https://docs.google.com/spreadsheets/d/1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800

---

**🚀 Bây giờ bạn đã sẵn sàng sử dụng hệ thống!**
