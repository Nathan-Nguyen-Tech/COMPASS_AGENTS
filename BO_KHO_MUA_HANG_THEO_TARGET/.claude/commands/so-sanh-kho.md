# Command: /so-sanh-kho

So sánh kết quả đã tính (VTTH hoặc Hóa Chất) với file tồn kho để xác định số lượng cần mua.

## 🛠️ SCRIPT AVAILABLE

**⚠️ CRITICAL: Đã có script Python sẵn để chạy command này!**

**LUÔN SỬ DỤNG SCRIPT CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!**

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/inventory_comparator.py
```

📖 **Chi tiết:** [tools/SCRIPTS_GUIDE.md](../tools/SCRIPTS_GUIDE.md#4-inventory_comparatorpy---so-sánh-tồn-kho--canonical)

## Mô Tả

Command này sẽ:
1. Đọc file tồn kho (Excel .xlsx hoặc CSV .csv)
2. **So sánh bằng đơn vị nhỏ nhất** (lọ, miếng, ml)
3. Tính số lượng cần mua (cả đơn vị nhỏ và lớn)
4. Xác định trạng thái: ĐỦ KHO / CẦN MUA / HẾT KHO
5. Hiển thị 2 bảng: CẦN MUA và ĐỦ KHO
6. Hỏi có muốn tạo phiếu mua hàng không

## ⚠️ YÊU CẦU

Phải đã chạy `/tinh-vtth` hoặc `/tinh-hoa-chat` trước đó!

## Sử Dụng

```bash
/so-sanh-kho <file_path>
```

### Tham Số

- **file_path** (bắt buộc): Đường dẫn file tồn kho
  - Format: `.xlsx` hoặc `.csv`
  - Cột bắt buộc: "Tên sản phẩm", "Tồn kho"

## Ví Dụ

```bash
# File trong workspace
/so-sanh-kho workspace/inventory-files/ton-kho-thang-2.xlsx

# File ở nơi khác
/so-sanh-kho D:/data/ton-kho.csv

# File tương đối
/so-sanh-kho ../ton-kho.xlsx
```

## ⭐ QUY TẮC CỰC KỲ QUAN TRỌNG

### SO SÁNH BẰNG ĐƠN VỊ NHỎ!

```python
# ✅ ĐÚNG: So sánh bằng đơn vị nhỏ
ton_kho_nho = ton_kho_lon * ty_le_quy_doi  # 1.2 hộp × 100 = 120 lọ
can_nho = item['so_luong_nho']              # 150 lọ
can_mua_nho = max(0, can_nho - ton_kho_nho) # 150 - 120 = 30 lọ

# ✅ QUY ĐỔI SANG ĐƠN VỊ LỚN CHO PHIẾU (ROUNDUP)
can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi)  # ⌈30÷100⌉ = 1 hộp

# ❌ SAI - KHÔNG BAO GIỜ:
# can_mua_lon = can_lon - ton_kho_lon  # SAI HOÀN TOÀN!
```

**Tại sao?**
- Tồn kho có thể là số thập phân (1.2 hộp)
- Nếu so sánh bằng đơn vị lớn sẽ SAI!

## Workflow

### Bước 1: Kiểm Tra Điều Kiện
```python
# Kiểm tra đã có kết quả tính toán chưa
if not has_calculation_results():
    print("❌ Chưa có kết quả tính toán!")
    print("Vui lòng chạy /tinh-vtth hoặc /tinh-hoa-chat trước.")
    return

# Kiểm tra file tồn tại
import os
if not os.path.exists(file_path):
    print(f"❌ File không tồn tại: {file_path}")
    return
```

### Bước 2: Đọc File Tồn Kho
```python
import pandas as pd

# Đọc file
if file_path.endswith('.xlsx'):
    df = pd.read_excel(file_path)
elif file_path.endswith('.csv'):
    df = pd.read_csv(file_path)
else:
    print("❌ File phải là .xlsx hoặc .csv")
    return

# Kiểm tra cột
required_cols = ['Tên sản phẩm', 'Tồn kho']
for col in required_cols:
    if col not in df.columns:
        print(f"❌ Thiếu cột '{col}' trong file")
        return

# Chuẩn hóa tên
def normalize_name(name):
    return str(name).strip().lower()

df['ten_chuan'] = df['Tên sản phẩm'].apply(normalize_name)
```

### ⭐ Bước 3: So Sánh (BẰNG ĐƠN VỊ NHỎ!)
```python
import math

for item in calculated_items:
    ten_chuan = normalize_name(item['ten'])
    can_nho = item['so_luong_nho']
    ty_le_quy_doi = item['ty_le_quy_doi']

    # Tìm tồn kho
    ton_kho_row = df[df['ten_chuan'] == ten_chuan]

    if not ton_kho_row.empty:
        ton_kho_lon = float(ton_kho_row.iloc[0]['Tồn kho'])
        # ⭐ Chuyển sang đơn vị nhỏ
        ton_kho_nho = ton_kho_lon * ty_le_quy_doi
    else:
        ton_kho_nho = 0
        ton_kho_lon = 0

    # ⭐ SO SÁNH BẰNG ĐƠN VỊ NHỎ
    can_mua_nho = max(0, can_nho - ton_kho_nho)

    # ⭐ QUY ĐỔI SANG ĐƠN VỊ LỚN (ROUNDUP)
    can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi)

    # Xác định trạng thái
    if ton_kho_nho >= can_nho:
        trang_thai = "ĐỦ KHO"
    elif ton_kho_nho == 0:
        trang_thai = "HẾT KHO"
    else:
        trang_thai = "CẦN MUA"

    # Lưu kết quả
    item['ton_kho_nho'] = ton_kho_nho
    item['ton_kho_lon'] = ton_kho_lon
    item['can_mua_nho'] = can_mua_nho
    item['can_mua_lon'] = can_mua_lon  # ⭐ CHO PHIẾU MUA HÀNG
    item['trang_thai'] = trang_thai
```

### Bước 4: Hiển Thị Kết Quả
```markdown
✅ Đã so sánh với tồn kho!

## 🔴 CẦN MUA (15 loại)

| STT | Tên SP | Cần (lọ) | Tồn (lọ) | Mua (lọ) | Mua (Hộp) | Trạng Thái |
|-----|--------|----------|----------|----------|-----------|------------|
| 1   | Lammen | 200      | 0        | 200      | 4         | HẾT KHO    |
| 2   | GLUCOSE| 150      | 120      | 30       | 1         | CẦN MUA    |
| 3   | ALT    | 200      | 50       | 150      | 2         | CẦN MUA    |
...

## ✅ ĐỦ KHO (10 loại)

| STT | Tên SP | Cần (lọ) | Tồn (lọ) | Trạng Thái |
|-----|--------|----------|----------|------------|
| 1   | AST    | 100      | 250      | ĐỦ KHO     |
| 2   | UREA   | 150      | 200      | ĐỦ KHO     |
...

📊 Tổng kết:
- Tổng loại: 25
- CẦN MUA: 15 loại (HẾT KHO + CẦN MUA)
- ĐỦ KHO: 10 loại

⚠️ LƯU Ý: Phiếu mua hàng sẽ dùng đơn vị lớn (Hộp) và ROUNDUP.
```

### ⭐ Bước 5: Hỏi Tạo Phiếu
```
❓ Bạn có muốn tạo Phiếu Mua Hàng không?

Trả lời: CÓ / KHÔNG
```

**Nếu user trả lời "CÓ":**
```python
# Chuyển sang command /tao-phieu
# hoặc gọi Purchase Order Creator Agent
```

### Bước 6: Lưu Kết Quả
```python
import json
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"workspace/calculations/comparison_{timestamp}.json"

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump({
        'file_ton_kho': file_path,
        'timestamp': timestamp,
        'so_khach': so_khach,
        'goi_dv': goi_dv,
        'can_mua': [item for item in items if item['trang_thai'] != 'ĐỦ KHO'],
        'du_kho': [item for item in items if item['trang_thai'] == 'ĐỦ KHO'],
        'summary': {
            'tong_loai': len(items),
            'can_mua': len([i for i in items if i['trang_thai'] != 'ĐỦ KHO']),
            'du_kho': len([i for i in items if i['trang_thai'] == 'ĐỦ KHO'])
        }
    }, f, ensure_ascii=False, indent=2)
```

## Format File Tồn Kho

### Excel (.xlsx) hoặc CSV (.csv)

| Tên sản phẩm | Tồn kho | Ghi chú |
|--------------|---------|---------|
| Lammen 22x22 | 0       |         |
| GLUCOSE GLU 440 | 1.2  | 1.2 hộp |
| ALT          | 0.5     | 0.5 hộp |
| AST          | 2.5     | 2.5 hộp |

**Yêu cầu:**
- Cột "Tên sản phẩm": Tên sản phẩm (bắt buộc)
- Cột "Tồn kho": Số lượng tồn kho **đơn vị lớn** (Hộp) (bắt buộc)
- Tồn kho có thể là số thập phân (1.2, 0.5, 2.5)

## Output Format

### Bảng CẦN MUA
- **Tên SP**: Tên sản phẩm
- **Cần (lọ)**: Nhu cầu đơn vị nhỏ
- **Tồn (lọ)**: Tồn kho đơn vị nhỏ
- **Mua (lọ)**: Số lượng cần mua đơn vị nhỏ
- **Mua (Hộp)**: Số lượng cần mua đơn vị lớn (ROUNDUP)
- **Trạng Thái**: HẾT KHO hoặc CẦN MUA

### Bảng ĐỦ KHO
- **Tên SP**: Tên sản phẩm
- **Cần (lọ)**: Nhu cầu đơn vị nhỏ
- **Tồn (lọ)**: Tồn kho đơn vị nhỏ
- **Trạng Thái**: ĐỦ KHO

## Agent Used

Command này sử dụng **Inventory Manager Agent** (`inventory-manager.md`)

## Related Commands

- `/tinh-vtth` - Tính VTTH (chạy trước)
- `/tinh-hoa-chat` - Tính hóa chất (chạy trước)
- `/tao-phieu` - Tạo phiếu mua hàng (chạy sau)
- `/kho` - Menu chính

## Error Handling

| Lỗi | Thông Báo |
|-----|-----------|
| Chưa có kết quả tính toán | ❌ Chưa chạy /tinh-vtth hoặc /tinh-hoa-chat |
| File not found | ❌ File không tồn tại: [path] |
| Invalid format | ❌ File phải là .xlsx hoặc .csv |
| Missing columns | ❌ Thiếu cột '[col_name]' trong file |
| Empty file | ❌ File rỗng hoặc không có dữ liệu |
| Tên sản phẩm không khớp | ⚠️ [X] sản phẩm không tìm thấy trong file tồn kho |

## CHECKLIST

Trước khi trả kết quả, kiểm tra:
- [ ] Đã có kết quả tính toán?
- [ ] Đã đọc file tồn kho thành công?
- [ ] Đã chuẩn hóa tên sản phẩm?
- [ ] Đã chuyển tồn kho sang đơn vị nhỏ?
- [ ] Đã so sánh bằng đơn vị nhỏ?
- [ ] Đã ROUNDUP khi quy đổi sang đơn vị lớn?
- [ ] Đã hiển thị cả 2 đơn vị (nhỏ và lớn)?
- [ ] Đã phân loại rõ: CẦN MUA vs ĐỦ KHO?
- [ ] Đã lưu kết quả?
- [ ] Đã hỏi về tạo phiếu?

## Notes

- **CRITICAL**: LUÔN so sánh bằng đơn vị nhỏ!
- Tồn kho trong file Excel/CSV phải là **đơn vị lớn** (Hộp)
- Hệ thống tự động quy đổi sang đơn vị nhỏ để so sánh
- Kết quả hiển thị CẢ đơn vị nhỏ VÀ lớn để dễ hiểu
- Phiếu mua hàng sẽ dùng đơn vị lớn (đã ROUNDUP)
