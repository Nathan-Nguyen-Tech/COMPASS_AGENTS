# Command: /tinh-hoa-chat

Tính toán nhu cầu Hóa Chất (bao gồm QC/CALIB) theo số lượng khách hàng và gói dịch vụ.

## Mô Tả

Command này sẽ:
1. Đọc sheet "Hoa Chat Chi Tiet" để lọc danh sách hóa chất
2. Lọc theo: Loại = "Chạy mẫu" + Gói có "x"
3. Đọc sheet "Hoa Chat" để tra cứu QC/CALIB
4. Tính: `Test = Test khách + Test QC + Test Calib`
5. Quy đổi sang đơn vị lớn (ROUNDUP)
6. **HỎI** về QC/CALIB bổ sung
7. Hiển thị bảng kết quả
8. Lưu vào workspace/calculations/

## Sử Dụng

```bash
/tinh-hoa-chat <số_khách> [gói_dv]
```

### Tham Số

- **số_khách** (bắt buộc): Số lượng khách hàng
- **gói_dv** (tùy chọn): Gói dịch vụ. Mặc định: "B2B-Gói đồng"
  - Options: "B2B-Gói đồng", "B2B-Gói cơ bản", "B2B-Gói bạc"

## Ví Dụ

```bash
# Tính hóa chất cho 300 khách, gói đồng (mặc định)
/tinh-hoa-chat 300

# Tính hóa chất cho 300 khách, gói đồng (rõ ràng)
/tinh-hoa-chat 300 B2B-Gói đồng

# Tính hóa chất cho 150 khách, gói cơ bản
/tinh-hoa-chat 150 B2B-Gói cơ bản
```

## ⭐ QUY TẮC QUAN TRỌNG

### 1. LUÔN đọc sheet "Hoa Chat Chi Tiet" để lọc
```python
# ✅ ĐÚNG
chi_tiet = get_sheet_data(spreadsheet_id, "Hoa Chat Chi Tiet")

# ❌ SAI - KHÔNG lọc từ "Hoa Chat"
# hoa_chat = get_sheet_data(spreadsheet_id, "Hoa Chat")  # SAI!
```

### 2. Điều kiện lọc
```python
for row in chi_tiet[1:]:
    loai_hc = row[5]      # Cột 5: Loại hóa chất
    goi = row[col_index]  # Cột 12/13/14: Gói

    # ⭐ ĐIỀU KIỆN
    if loai_hc == "Chạy mẫu" and goi == "x":
        filtered_items.append(row)
```

### 3. LUÔN hỏi về QC/CALIB bổ sung
```
❓ Bạn có muốn thêm QC & CALIB riêng không?

Nếu CÓ, tôi sẽ thêm:
✅ ERBA PATH: 2 lọ (QC sinh hóa)
✅ ERBA NORM (Level-2): 2 lọ (QC sinh hóa)
✅ XL MULTICAL 4*3ml: 2 lọ (Calib chung)
✅ HDL/LDL Cal: 1 lọ (nếu có HDL/LDL)

Trả lời: CÓ / KHÔNG
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

### ⭐ Bước 2: Đọc Sheet "Hoa Chat Chi Tiet" (SHEET CHÍNH)
```python
from tools.scripts.google_sheets_api import get_sheet_data

spreadsheet_id = "1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800"
chi_tiet = get_sheet_data(spreadsheet_id, "Hoa Chat Chi Tiet", include_grid_data=False)
```

### ⭐ Bước 3: Lọc Hóa Chất
```python
col_map = {
    "B2B-Gói đồng": 12,
    "B2B-Gói cơ bản": 13,
    "B2B-Gói bạc": 14
}

col_index = col_map[goi_dv]

filtered_items = []
for row in chi_tiet[1:]:  # Bỏ header
    loai_hc = row[5] if len(row) > 5 else ""
    goi = row[col_index] if len(row) > col_index else ""

    # ⭐ ĐIỀU KIỆN LỌC
    if loai_hc == "Chạy mẫu" and goi == "x":
        ten = row[3]
        lo_per_hop = float(row[9]) if row[9] else 1
        test_per_lo = float(row[10]) if row[10] else 0

        filtered_items.append({
            'ten': ten,
            'lo_per_hop': lo_per_hop,
            'test_per_lo': test_per_lo
        })
```

### ⭐ Bước 4: Đọc Sheet "Hoa Chat" (TRA CỨU QC/CALIB)
```python
qc_calib_info = get_sheet_data(spreadsheet_id, "Hoa Chat", include_grid_data=False)
```

### Bước 5: Tính Toán
```python
import math

results = []

for item in filtered_items:
    ten = item['ten']
    lo_per_hop = item['lo_per_hop']
    test_per_lo = item['test_per_lo']

    # Tra cứu QC/CALIB
    test_qc = 2
    test_calib = 4

    for qc_row in qc_calib_info[1:]:
        ten_qc = qc_row[1] if len(qc_row) > 1 else ""
        if ten_qc == ten:
            test_qc = int(float(qc_row[16])) if len(qc_row) > 16 and qc_row[16] else 2
            test_calib = int(float(qc_row[24])) if len(qc_row) > 24 and qc_row[24] else 4
            break

    # Đặc biệt: HC không có QC/CALIB
    keywords_no_qc = ["dung dịch", "wash", "tiểu", "diluit", "lyse", "clean", "dye"]
    if any(keyword in ten.lower() for keyword in keywords_no_qc):
        test_qc = 0
        test_calib = 0

    # Tính toán
    test_khach = số_khách
    tong_test = test_khach + test_qc + test_calib

    if test_per_lo > 0:
        so_lo = math.ceil(tong_test / test_per_lo)
        so_hop = math.ceil(so_lo / lo_per_hop)
    else:
        so_lo = 1
        so_hop = 1

    # Xác định đơn vị lớn
    if "20L" in ten or "20l" in ten.lower():
        dvt_lon = "Thùng"
    elif any(k in ten.lower() for k in ["dung dịch", "lyse", "clean"]):
        dvt_lon = "Chai"
    else:
        dvt_lon = "Hộp"

    results.append({
        'ten': ten,
        'dvt_nho': 'lọ',
        'dvt_lon': dvt_lon,
        'ty_le_quy_doi': lo_per_hop,
        'test_per_lo': test_per_lo,
        'test_khach': test_khach,
        'test_qc': test_qc,
        'test_calib': test_calib,
        'tong_test': tong_test,
        'so_luong_nho': so_lo,
        'so_luong_lon': so_hop
    })
```

### ⭐ Bước 6: Hỏi QC/CALIB Bổ Sung
```
❓ Bạn có muốn thêm QC & CALIB riêng không?

Nếu CÓ, tôi sẽ thêm:
✅ ERBA PATH: 2 lọ (QC sinh hóa)
✅ ERBA NORM (Level-2): 2 lọ (QC sinh hóa)
✅ XL MULTICAL 4*3ml: 2 lọ (Calib chung)
✅ HDL/LDL Cal: 1 lọ (nếu có HDL/LDL)

Trả lời: CÓ / KHÔNG
```

**Nếu user trả lời "CÓ":**
```python
qc_calib_bo_sung = [
    {'ten': 'ERBA PATH', 'so_luong_nho': 2, 'so_luong_lon': 2, 'dvt_nho': 'lọ', 'dvt_lon': 'lọ', 'ty_le_quy_doi': 1, 'loai': 'QC'},
    {'ten': 'ERBA NORM (Level-2)', 'so_luong_nho': 2, 'so_luong_lon': 2, 'dvt_nho': 'lọ', 'dvt_lon': 'lọ', 'ty_le_quy_doi': 1, 'loai': 'QC'},
    {'ten': 'XL MULTICAL 4*3ml', 'so_luong_nho': 2, 'so_luong_lon': 2, 'dvt_nho': 'lọ', 'dvt_lon': 'lọ', 'ty_le_quy_doi': 1, 'loai': 'CALIB'}
]

# Kiểm tra nếu có HDL/LDL
has_hdl_ldl = any('HDL' in item['ten'] or 'LDL' in item['ten'] for item in results)
if has_hdl_ldl:
    qc_calib_bo_sung.append({
        'ten': 'HDL/LDL Cal',
        'so_luong_nho': 1,
        'so_luong_lon': 1,
        'dvt_nho': 'lọ',
        'dvt_lon': 'lọ',
        'ty_le_quy_doi': 1,
        'loai': 'CALIB'
    })

results.extend(qc_calib_bo_sung)
```

### Bước 7: Hiển Thị Kết Quả
```markdown
✅ Đã tính Hóa Chất cho 300 khách - B2B-Gói đồng

| STT | Tên Hóa Chất | Test KH | QC | Cal | Tổng | Lọ | Hộp | ĐVT |
|-----|--------------|---------|----|----|------|-----|-----|-----|
| 1   | GLUCOSE GLU 440 | 300 | 2 | 4 | 306 | 4 | 1 | Hộp |
| 2   | ALT | 300 | 2 | 4 | 306 | 4 | 1 | Hộp |
| 3   | AST | 300 | 2 | 4 | 306 | 4 | 1 | Hộp |
...
| 21  | ERBA PATH | - | - | - | - | 2 | 2 | lọ |
| 22  | ERBA NORM (Level-2) | - | - | - | - | 2 | 2 | lọ |
| 23  | XL MULTICAL 4*3ml | - | - | - | - | 2 | 2 | lọ |

📊 Tổng: 23 loại hóa chất (bao gồm QC/CALIB bổ sung)
💾 Đã lưu vào: workspace/calculations/hoa_chat_20250202_143052.json

---

Bước tiếp theo:
- Chạy /so-sanh-kho [file_path] để so sánh với tồn kho
```

### Bước 8: Lưu Kết Quả
```python
import json
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"workspace/calculations/hoa_chat_{timestamp}.json"

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump({
        'type': 'Hoa Chat',
        'so_khach': số_khách,
        'goi_dv': goi_dv,
        'timestamp': timestamp,
        'results': results
    }, f, ensure_ascii=False, indent=2)
```

## Output Format

### Bảng Kết Quả
- **STT**: Số thứ tự
- **Tên Hóa Chất**: Tên hóa chất
- **Test KH**: Số test cho khách hàng
- **QC**: Số test QC
- **Cal**: Số test Calibration
- **Tổng**: Tổng số test
- **Lọ**: Số lượng lọ cần
- **Hộp**: Số lượng hộp cần (đã ROUNDUP)
- **ĐVT**: Đơn vị tính lớn

### Metadata
- Tổng số loại hóa chất (bao gồm QC/CALIB bổ sung)
- File path đã lưu

## Agent Used

Command này sử dụng **Calculator Agent** (`calculator.md`)

## Related Commands

- `/tinh-vtth` - Tính VTTH
- `/so-sanh-kho` - So sánh với tồn kho
- `/kho` - Menu chính

## Error Handling

| Lỗi | Thông Báo |
|-----|-----------|
| Số khách <= 0 | ❌ Số khách hàng phải > 0 |
| Gói không hợp lệ | ❌ Gói dịch vụ không hợp lệ |
| Sheet "Hoa Chat Chi Tiet" not found | ❌ Không tìm thấy sheet 'Hoa Chat Chi Tiet' |
| Sheet "Hoa Chat" not found | ❌ Không tìm thấy sheet 'Hoa Chat' |
| Empty data | ❌ Sheet không có dữ liệu |
| Thiếu hóa chất | ⚠️ Số lượng HC ít hơn expected (Gói đồng: ~21 loại) |

## CHECKLIST

Trước khi trả kết quả, kiểm tra:
- [ ] Đã đọc sheet "Hoa Chat Chi Tiet"?
- [ ] Đã lọc theo "Loại = Chạy mẫu"?
- [ ] Đã lọc theo cột gói có "x"?
- [ ] Đã tra cứu QC/CALIB từ sheet "Hoa Chat"?
- [ ] Đã hỏi về QC/CALIB bổ sung?
- [ ] Số lượng hóa chất có đủ? (Gói đồng: ~21 loại)
- [ ] Đã lưu kết quả?

## Notes

- **CRITICAL**: LUÔN đọc "Hoa Chat Chi Tiet" để lọc, KHÔNG phải "Hoa Chat"
- Sheet "Hoa Chat" CHỈ dùng để tra cứu QC/CALIB
- LUÔN hỏi về QC/CALIB bổ sung
- Gói đồng thường có ~21 loại hóa chất (chưa bao gồm QC/CALIB bổ sung)
- Kết quả được lưu để sử dụng cho `/so-sanh-kho`
