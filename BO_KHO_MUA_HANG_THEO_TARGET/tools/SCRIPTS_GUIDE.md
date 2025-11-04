# Scripts Guide - Hướng Dẫn Sử Dụng Scripts

## 🎯 MỤC ĐÍCH

Tài liệu này liệt kê **TẤT CẢ** các scripts Python có sẵn trong project và cách sử dụng.

**⚠️ QUY TẮC QUAN TRỌNG:**
> **LUÔN SỬ DỤNG CÁC SCRIPTS CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!**
>
> Các scripts này đã được test và optimize. Không tự viết lại logic!

---

## 📁 CẤU TRÚC THỦ MUỤC

```
BO_KHO_MUA_HANG_THEO_TARGET/
├── tools/
│   └── scripts/
│       ├── google_sheets_api.py          # ⭐ API wrapper
│       ├── calculator.py                 # ⭐ Tính VTTH
│       ├── calculate_chemicals.py        # ⭐ Tính Hóa Chất
│       ├── inventory_comparator.py       # ⭐ So sánh kho (CANONICAL)
│       ├── create_purchase_order.py      # ⭐ Tạo phiếu (CANONICAL)
│       ├── inventory_comparison.py       # ❌ DEPRECATED - Không dùng
│       ├── purchase_order_creator.py     # ❌ DEPRECATED - Không dùng
│       └── debug_sheet.py                # 🔧 Dev tool
```

---

## ⭐ CANONICAL SCRIPTS (LUÔN DÙNG CÁC SCRIPTS NÀY)

### 1. `google_sheets_api.py` - Google Sheets API Wrapper

**Mục đích:** API layer để đọc/ghi Google Sheets

**Không chạy trực tiếp.** Được import bởi các scripts khác.

**Key Functions:**
```python
from tools.scripts.google_sheets_api import get_sheet_data, update_cells, copy_sheet

# Đọc data từ sheet
data = get_sheet_data(spreadsheet_id, sheet_name, range_name)

# Cập nhật cells
update_cells(spreadsheet_id, sheet_name, range_name, values)

# Copy sheet template
new_sheet_id = copy_sheet(spreadsheet_id, source_sheet_id, new_sheet_name)
```

---

### 2. `calculator.py` - Tính VTTH (Vật Tư Tiêu Hao)

**Mục đích:** Tính nhu cầu VTTH dựa trên số khách và gói dịch vụ

**Cách chạy:**
```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/calculator.py
```

**Interactive prompts:**
```
Nhập số lượng khách: 300
Chọn gói dịch vụ:
1. B2B-Goi dong
2. B2B-Goi co ban
3. B2B-Goi bac
Chọn (1-3): 1
```

**Output:**
- File: `workspace/calculations/vtth_YYYYMMDD_HHMMSS.json`
- Format:
```json
{
  "so_khach": 300,
  "goi_dv": "B2B-Goi dong",
  "timestamp": "20250104_143022",
  "items": [
    {
      "ten": "Lammen",
      "dinh_muc": 0.5,
      "so_luong_nho": 150,
      "don_vi_nho": "lo",
      "ty_le_quy_doi": 100,
      "so_luong_lon": 2,
      "don_vi_lon": "hop"
    }
  ]
}
```

**Logic:**
- Đọc sheet "VTTH" từ Google Sheets
- Map gói dịch vụ → column index
- Parse định mức (VD: "100 lo" → số lượng 100, đơn vị "lo")
- Tính: `nhu_cau_nho = so_khach × dinh_muc`
- Quy đổi lớn: `nhu_cau_lon = ROUNDUP(nhu_cau_nho ÷ ty_le_quy_doi)`

---

### 3. `calculate_chemicals.py` - Tính Hóa Chất

**Mục đích:** Tính nhu cầu Hóa Chất (bao gồm QC/CALIB)

**Cách chạy:**
```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/calculate_chemicals.py
```

**Interactive prompts:**
```
Nhập số lượng khách: 300
Chọn gói dịch vụ:
1. dong
2. co ban
3. bac
Chọn (1-3): 1
```

**Output:**
- File: `workspace/calculations/hoa_chat_YYYYMMDD_HHMMSS.json`
- Format tương tự calculator.py

**Logic đặc biệt:**
- Đọc sheet "Hoa Chat Chi Tiet" (SHEET CHÍNH)
- Lọc: Loại = "Chạy mẫu" VÀ gói dịch vụ có dấu "x"
- Lookup QC/CALIB từ sheet "Hoa Chat" (SHEET PHỤ)
- Tính: `tong_test = test_khach + test_qc + test_calib`
- Một số items không cần QC/CALIB (dung dịch, thuốc nhuộm)

---

### 4. `inventory_comparator.py` - So Sánh Tồn Kho ⭐ CANONICAL

**Mục đích:** So sánh nhu cầu với tồn kho, xác định số lượng cần mua

**Cách chạy:**
```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/inventory_comparator.py
```

**Interactive prompts:**
```
Chọn file tính toán (VTTH hoặc Hóa Chất):
1. workspace/calculations/vtth_20250104_143022.json
2. workspace/calculations/hoa_chat_20250104_143530.json
Chọn: 1

Nhập đường dẫn file tồn kho (Excel hoặc CSV):
> ton_kho_hom_nay.xlsx
```

**Output:**
- File: `workspace/calculations/comparison_YYYYMMDD_HHMMSS.json`
- Format:
```json
{
  "so_khach": 300,
  "goi_dv": "B2B-Goi dong",
  "timestamp": "20250104_144500",
  "can_mua": [
    {
      "ten": "Lammen",
      "can_nho": 150,
      "ton_kho_nho": 0,
      "can_mua_nho": 150,
      "can_mua_lon": 2,
      "trang_thai": "HẾT KHO"
    }
  ],
  "du_kho": [...]
}
```

**Logic CRITICAL:**
```python
# ⭐ LUÔN SO SÁNH BẰNG ĐƠN VỊ NHỎ
ton_kho_nho = ton_kho_lon × ty_le_quy_doi  # 1.2 hộp × 100 = 120 lọ
can_mua_nho = max(0, can_nho - ton_kho_nho)  # 150 - 120 = 30 lọ

# ⭐ QUY ĐỔI SANG ĐƠN VỊ LỚN CHO PHIẾU (ROUNDUP)
can_mua_lon = math.ceil(can_mua_nho ÷ ty_le_quy_doi)  # ⌈30÷100⌉ = 1 hộp
```

**Features:**
- Auto-detect header row (thường là row 3)
- Normalize product names để matching
- Xác định trạng thái: ĐỦ KHO / CẦN MUA / HẾT KHO
- Hỗ trợ cả Excel (.xlsx) và CSV (.csv)

---

### 5. `create_purchase_order.py` - Tạo Phiếu Mua Hàng ⭐ CANONICAL

**Mục đích:** Tạo Phiếu Mua Hàng trong Google Sheets từ kết quả so sánh

**Cách chạy:**
```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/create_purchase_order.py
```

**Interactive prompts:**
```
Chọn file so sánh:
1. workspace/calculations/comparison_20250104_144500.json
Chọn: 1

Nhập tên người yêu cầu: Nguyen Van A
Nhập nội dung yêu cầu: Mua VTTH cho 300 khách gói đông
```

**Output:**
- Google Sheet mới: "Phiếu_YYYYMMDD_HHMMSS"
- Metadata file: `workspace/purchase_orders/phieu_YYYYMMDD_HHMMSS.json`

**Workflow:**
1. Copy sheet template "Phiếu mua hàng mẫu version 1"
2. Rename thành "Phiếu_YYYYMMDD_HHMMSS"
3. Update header (ngày, người yêu cầu, nội dung, số khách)
4. Populate items từ row 9 (dùng ĐƠN VỊ LỚN - đã ROUNDUP)
5. Lưu metadata vào sheet "Phiếu Mua Hàng"
6. Lưu chi tiết vào sheet "Chi Tiết Phiếu Mua Hàng"

**Sheet Structure:**
```
Row 1-2: Logo & Title
Row 3-8: Header info (Ngày, Người yêu cầu, Nội dung, Số khách)
Row 9+: Items table
  Column A: STT
  Column B: Tên sản phẩm
  Column C: Số lượng (ĐƠN VỊ LỚN)
  Column D: Đơn vị
  Column E: Ghi chú
```

---

## ❌ DEPRECATED SCRIPTS (KHÔNG SỬ DỤNG)

### `inventory_comparison.py` - DEPRECATED
- **Lý do:** Version cũ, logic khác với inventory_comparator.py
- **Vấn đề:** Dùng fuzzy matching, JSON structure khác
- **Thay thế:** Dùng `inventory_comparator.py`

### `purchase_order_creator.py` - DEPRECATED
- **Lý do:** Version cũ, thiếu metadata tracking
- **Vấn đề:** Không lưu vào "Phiếu Mua Hàng" và "Chi Tiết Phiếu Mua Hàng"
- **Thay thế:** Dùng `create_purchase_order.py`

---

## 🔧 DEV TOOLS

### `debug_sheet.py` - Sheet Debugger
**Mục đích:** Debug Google Sheet structure (dev only)

**Cách chạy:**
```bash
python tools/scripts/debug_sheet.py
```

Hiển thị:
- Column names
- Data types
- Sample rows
- Sheet structure

---

## 📊 WORKFLOW HOÀN CHỈNH

### Workflow 1: Tính VTTH và Tạo Phiếu

```bash
# Bước 1: Tính VTTH
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/calculator.py
# → Output: workspace/calculations/vtth_20250104_143022.json

# Bước 2: So sánh tồn kho
python tools/scripts/inventory_comparator.py
# → Chọn file vtth_20250104_143022.json
# → Nhập file tồn kho: ton_kho.xlsx
# → Output: workspace/calculations/comparison_20250104_144500.json

# Bước 3: Tạo phiếu mua hàng
python tools/scripts/create_purchase_order.py
# → Chọn file comparison_20250104_144500.json
# → Nhập thông tin người yêu cầu
# → Output: Google Sheet "Phiếu_20250104_144500"
```

### Workflow 2: Tính Hóa Chất và Tạo Phiếu

```bash
# Bước 1: Tính Hóa Chất
python tools/scripts/calculate_chemicals.py
# → Output: workspace/calculations/hoa_chat_20250104_143530.json

# Bước 2-3: Tương tự như trên
```

---

## 🔐 CREDENTIALS

**File:** `BO_KHO_MUA_HANG_THEO_TARGET/credentials.json`

Cần file credentials để chạy scripts. Nếu thiếu:
1. Vào Google Cloud Console
2. Enable Google Sheets API
3. Tạo Service Account
4. Download credentials.json
5. Đặt vào thư mục project

---

## 🐛 TROUBLESHOOTING

### Lỗi: "ModuleNotFoundError: No module named 'google'"
```bash
pip install -r requirements.txt
```

### Lỗi: "File credentials.json not found"
- Kiểm tra file credentials.json có trong thư mục project
- Đảm bảo Service Account có quyền truy cập spreadsheet

### Lỗi: "Sheet not found"
- Kiểm tra tên sheet đúng chính xác
- Kiểm tra spreadsheet ID đúng

### Lỗi: "Invalid file format"
- Inventory file phải là .xlsx hoặc .csv
- Kiểm tra file có header row 3

---

## 📝 BEST PRACTICES

### 1. Luôn Kiểm Tra Scripts Trước
```bash
# ✅ ĐÚNG
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/calculator.py

# ❌ SAI - Tự viết code mới
# Không tự implement lại logic!
```

### 2. Dùng Output Từ Script Trước Làm Input Cho Script Sau
```bash
# Bước 1: calculator.py → vtth_20250104.json
# Bước 2: inventory_comparator.py → comparison_20250104.json (dùng vtth_20250104.json)
# Bước 3: create_purchase_order.py (dùng comparison_20250104.json)
```

### 3. Lưu Kết Quả Vào workspace/
- Calculations: `workspace/calculations/`
- Purchase orders: `workspace/purchase_orders/`
- Logs: `workspace/logs/`

### 4. Đặt Tên File Với Timestamp
```
vtth_20250104_143022.json
comparison_20250104_144500.json
phieu_20250104_145000.json
```

---

## 📚 REFERENCES

- [README.md](README.md) - Overview và installation
- [CLAUDE.md](../CLAUDE.md) - Main instructions
- [context/workflows/](../context/workflows/) - Workflow documentation
- [.claude/agents/](../.claude/agents/) - Agent definitions

---

**Cập nhật:** 2025-01-04
**Version:** 1.0.0
