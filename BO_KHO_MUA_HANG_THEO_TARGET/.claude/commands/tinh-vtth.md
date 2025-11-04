# Command: /tinh-vtth

Tính toán nhu cầu Vật Tư Tiêu Hao (VTTH) theo số lượng khách hàng và gói dịch vụ.

## 🛠️ SCRIPT AVAILABLE

**⚠️ CRITICAL: Đã có script Python sẵn để chạy command này!**

**LUÔN SỬ DỤNG SCRIPT CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!**

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/calculator.py
```

📖 **Chi tiết:** [tools/SCRIPTS_GUIDE.md](../tools/SCRIPTS_GUIDE.md#2-calculatorpy---tính-vtth-vật-tư-tiêu-hao)

## Mô Tả

Command này sẽ:
1. Đọc dữ liệu từ sheet "VTTH" trong Google Sheets
2. Lọc theo gói dịch vụ được chọn
3. Tính nhu cầu: `Nhu cầu = Số khách × Định mức`
4. Quy đổi sang đơn vị lớn: `Số hộp = ROUNDUP(Nhu cầu ÷ Tỷ lệ quy đổi)`
5. Hiển thị bảng kết quả
6. Lưu vào workspace/calculations/

## Sử Dụng

```bash
/tinh-vtth <số_khách> [gói_dv]
```

### Tham Số

- **số_khách** (bắt buộc): Số lượng khách hàng
- **gói_dv** (tùy chọn): Gói dịch vụ. Mặc định: "B2B-Gói đồng"
  - Options: "B2B-Gói đồng", "B2B-Gói cơ bản", "B2B-Gói bạc"

## Ví Dụ

```bash
# Tính VTTH cho 300 khách, gói đồng (mặc định)
/tinh-vtth 300

# Tính VTTH cho 300 khách, gói đồng (rõ ràng)
/tinh-vtth 300 B2B-Gói đồng

# Tính VTTH cho 150 khách, gói cơ bản
/tinh-vtth 150 B2B-Gói cơ bản

# Tính VTTH cho 500 khách, gói bạc
/tinh-vtth 500 B2B-Gói bạc
```

## Workflow

### Bước 1: Validate Input
```python
if not số_khách or số_khách <= 0:
    print("❌ Số khách hàng phải > 0")
    return

goi_dv = goi_dv or "B2B-Gói đồng"

valid_goi = ["B2B-Gói đồng", "B2B-Gói cơ bản", "B2B-Gói bạc"]
if goi_dv not in valid_goi:
    print(f"❌ Gói dịch vụ không hợp lệ. Chọn: {', '.join(valid_goi)}")
    return
```

### Bước 2: Đọc Dữ Liệu
```python
from tools.scripts.google_sheets_api import get_sheet_data

spreadsheet_id = "1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800"
data = get_sheet_data(spreadsheet_id, "VTTH", include_grid_data=False)
```

### Bước 3: Lọc Theo Gói
```python
# Map gói dịch vụ → column index
col_map = {
    "B2B-Gói đồng": 12,
    "B2B-Gói cơ bản": 13,
    "B2B-Gói bạc": 14
}

col_index = col_map[goi_dv]

filtered_items = []
for row in data[1:]:  # Bỏ header
    if len(row) > col_index and row[col_index] == "x":
        filtered_items.append(row)
```

### Bước 4: Tính Toán
```python
import math

results = []
for row in filtered_items:
    ten = row[1]
    dinh_muc = float(row[2]) if row[2] else 0
    dvt_nho = row[3]
    dvt_lon = row[4]
    ty_le_quy_doi = float(row[5]) if row[5] else 1

    # Tính nhu cầu đơn vị nhỏ
    nhu_cau_nho = số_khách * dinh_muc

    # Quy đổi sang đơn vị lớn (ROUNDUP)
    so_luong_lon = math.ceil(nhu_cau_nho / ty_le_quy_doi)

    results.append({
        'ten': ten,
        'dinh_muc': dinh_muc,
        'dvt_nho': dvt_nho,
        'dvt_lon': dvt_lon,
        'ty_le_quy_doi': ty_le_quy_doi,
        'so_luong_nho': nhu_cau_nho,
        'so_luong_lon': so_luong_lon
    })
```

### Bước 5: Hiển Thị Kết Quả
```markdown
✅ Đã tính VTTH cho 300 khách - B2B-Gói đồng

| STT | Tên Sản Phẩm | Định mức | Nhu cầu (lọ) | Số lượng (Hộp) | ĐVT |
|-----|--------------|----------|--------------|----------------|-----|
| 1   | Lammen 22x22 | 0.5      | 150          | 2              | Hộp |
| 2   | Ống nghiệm   | 1.5      | 450          | 5              | Hộp |
| 3   | Kim tiêm     | 1.0      | 300          | 3              | Hộp |
...

📊 Tổng: 25 loại VTTH
💾 Đã lưu vào: workspace/calculations/vtth_20250202_143052.json

---

Bước tiếp theo:
- Chạy /so-sanh-kho [file_path] để so sánh với tồn kho
- Hoặc chạy /tinh-hoa-chat để tính hóa chất
```

### Bước 6: Lưu Kết Quả
```python
import json
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"workspace/calculations/vtth_{timestamp}.json"

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump({
        'type': 'VTTH',
        'so_khach': số_khách,
        'goi_dv': goi_dv,
        'timestamp': timestamp,
        'results': results
    }, f, ensure_ascii=False, indent=2)
```

## Output Format

### Bảng Kết Quả
- **STT**: Số thứ tự
- **Tên Sản Phẩm**: Tên VTTH
- **Định mức**: Định mức sử dụng/khách
- **Nhu cầu (lọ)**: Tổng nhu cầu đơn vị nhỏ
- **Số lượng (Hộp)**: Số lượng cần mua (đơn vị lớn, đã ROUNDUP)
- **ĐVT**: Đơn vị tính lớn (Hộp, Chai, Thùng)

### Metadata
- Tổng số loại VTTH
- File path đã lưu

## Agent Used

Command này sử dụng **Calculator Agent** (`calculator.md`)

## Related Commands

- `/tinh-hoa-chat` - Tính hóa chất
- `/so-sanh-kho` - So sánh với tồn kho
- `/kho` - Menu chính

## Error Handling

| Lỗi | Thông Báo |
|-----|-----------|
| Số khách <= 0 | ❌ Số khách hàng phải > 0 |
| Gói không hợp lệ | ❌ Gói dịch vụ không hợp lệ |
| Sheet not found | ❌ Không tìm thấy sheet 'VTTH' |
| Empty data | ❌ Sheet 'VTTH' không có dữ liệu |
| Permission denied | ❌ Không có quyền truy cập Google Sheets |

## Notes

- Kết quả được lưu vào `workspace/calculations/` để có thể sử dụng cho `/so-sanh-kho`
- VTTH = Vật Tư Tiêu Hao (consumables)
- Luôn ROUNDUP khi quy đổi sang đơn vị lớn
- Gói đồng thường có ~25 loại VTTH
