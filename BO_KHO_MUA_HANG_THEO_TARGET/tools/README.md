# Tools - Scripts & SOPs

Thư mục này chứa Python scripts, utilities, và Standard Operating Procedures.

## 📁 Cấu Trúc

### scripts/
Python scripts cho Google Sheets và tính toán
- `google_sheets_api.py` - Kết nối Google Sheets API
- `calculator.py` - Logic tính toán VTTH & HC
- `inventory_comparator.py` - So sánh tồn kho
- `purchase_order_creator.py` - Tạo phiếu mua hàng
- `utils.py` - Utilities (normalize, roundup, etc.)

### SOPs/
Standard Operating Procedures - Hướng dẫn chi tiết
- `setup-google-sheets-api.md` - Setup Google Sheets API
- `configure-credentials.md` - Cấu hình credentials
- `update_readmes.md` - SOP cập nhật README

## 🐍 Python Scripts

### Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

### Sử Dụng Scripts

#### 1. Test Google Sheets Connection
```bash
python tools/scripts/google_sheets_api.py
```

#### 2. Tính VTTH (CLI)
```python
from tools.scripts.calculator import calculate_vtth

results = calculate_vtth(
    spreadsheet_id="1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800",
    so_khach=300,
    goi_dv="B2B-Gói đồng"
)
```

#### 3. So Sánh Tồn Kho (CLI)
```python
from tools.scripts.inventory_comparator import compare_inventory

comparison = compare_inventory(
    calculated_items=results,
    ton_kho_file="workspace/inventory-files/ton-kho.xlsx"
)
```

#### 4. Tạo Phiếu (CLI)
```python
from tools.scripts.purchase_order_creator import create_purchase_order

phieu = create_purchase_order(
    spreadsheet_id="1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800",
    can_mua_list=comparison['can_mua'],
    so_khach=300,
    goi_dv="B2B-Gói đồng"
)
```

## 📚 SOPs

### Setup Ban Đầu
1. `setup-google-sheets-api.md` - Tạo Google Cloud Project, enable API
2. `configure-credentials.md` - Cấu hình service account credentials

### Sử Dụng Hàng Ngày
- Tham khảo `USAGE_GUIDE.md` ở thư mục gốc

## 🔧 Requirements

Xem file `requirements.txt` để biết các package cần thiết:
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- pandas
- openpyxl

---

*Tất cả scripts đều có docstrings chi tiết. Dùng `help(function_name)` để xem.*
