# Command: /tao-phieu

Tạo phiếu mua hàng tự động trong Google Sheets từ template.

## 🛠️ SCRIPT AVAILABLE

**⚠️ CRITICAL: Đã có script Python sẵn để chạy command này!**

**LUÔN SỬ DỤNG SCRIPT CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!**

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/create_purchase_order.py
```

📖 **Chi tiết:** [tools/SCRIPTS_GUIDE.md](../tools/SCRIPTS_GUIDE.md#5-create_purchase_orderpy---tạo-phiếu-mua-hàng--canonical)

## Mô Tả

Command này sẽ:
1. Copy template "Phiếu mua hàng mẫu version 1"
2. Tạo sheet mới với tên unique (timestamp)
3. Cập nhật header (ngày lập, người đề nghị, nội dung)
4. Điền chi tiết sản phẩm **CẦN MUA** (DÙNG ĐƠN VỊ LỚN + ROUNDUP)
5. Lưu metadata vào 2 sheets: "Phiếu Mua Hàng" và "Chi Tiết Phiếu Mua Hàng"
6. Trả link Google Sheets

## ⚠️ YÊU CẦU

Phải đã chạy `/so-sanh-kho` trước đó!

## Sử Dụng

```bash
/tao-phieu
```

Không cần tham số. Command sẽ dùng kết quả từ `/so-sanh-kho`.

## ⭐ QUY TẮC QUAN TRỌNG

### 1. COPY Template, KHÔNG Tạo Mới

```python
# ✅ ĐÚNG: Copy template
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
new_sheet_name = f"Phiếu_{timestamp}"

copy_sheet(
    src_spreadsheet="1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800",
    src_sheet="Phiếu mua hàng mẫu version 1",
    dst_spreadsheet="1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800",
    dst_sheet=new_sheet_name
)

# ❌ SAI - KHÔNG tạo sheet mới rồi copy values
```

### 2. DÙNG ĐƠN VỊ LỚN + ROUNDUP

```python
# ✅ ĐÚNG
for item in can_mua_list:
    so_luong_lon = item['can_mua_lon']  # Đã ROUNDUP
    dvt_lon = item['dvt_lon']            # "Hộp", "Chai", "Thùng"

# ❌ SAI - Dùng đơn vị nhỏ
# so_luong_nho = item['can_mua_nho']  # SAI!
```

### 3. Chỉ Điền Items CẦN MUA

```python
# ✅ ĐÚNG: Lọc bỏ ĐỦ KHO
can_mua_list = [item for item in items if item['trang_thai'] != 'ĐỦ KHO']

# ❌ SAI: Điền cả items ĐỦ KHO
```

## Workflow

### Bước 1: Kiểm Tra Điều Kiện
```python
# Kiểm tra đã có kết quả so sánh chưa
if not has_comparison_results():
    print("❌ Chưa có kết quả so sánh tồn kho!")
    print("Vui lòng chạy /so-sanh-kho trước.")
    return

# Lọc items CẦN MUA
can_mua_list = [item for item in items if item['trang_thai'] != 'ĐỦ KHO']

if not can_mua_list:
    print("✅ Tất cả items đều ĐỦ KHO!")
    print("Không cần tạo phiếu mua hàng.")
    return

print(f"📦 Sẽ tạo phiếu cho {len(can_mua_list)} loại sản phẩm")
```

### ⭐ Bước 2: Copy Template
```python
from datetime import datetime

spreadsheet_id = "1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
new_sheet_name = f"Phiếu_{timestamp}"

# Copy sheet template (GIỮ NGUYÊN FORMAT)
copy_sheet(
    src_spreadsheet=spreadsheet_id,
    src_sheet="Phiếu mua hàng mẫu version 1",
    dst_spreadsheet=spreadsheet_id,
    dst_sheet=new_sheet_name
)

print(f"✅ Đã copy template → {new_sheet_name}")
```

### Bước 3: Cập Nhật Header
```python
header_updates = {
    'A3': [[f"1. Ngày lập: {datetime.now().strftime('%d/%m/%Y')}"]],
    'A4': [["2. Người đề nghị: Phòng Xét Nghiệm"]],
    'E4': [["Phòng ban: Phòng XN"]],
    'A5': [[f"3. Nội dung: Mua VTTH/Hóa chất cho {so_khach} khách - {goi_dv}"]]
}

batch_update_cells(spreadsheet_id, new_sheet_name, header_updates)
print("✅ Đã cập nhật header")
```

### ⭐ Bước 4: Điền Dữ Liệu (ĐƠN VỊ LỚN + ROUNDUP)
```python
DATA_START_ROW = 9

data_rows = []
for idx, item in enumerate(can_mua_list):
    # ⭐ DÙNG ĐƠN VỊ LỚN ĐÃ ROUNDUP
    so_luong_lon = item['can_mua_lon']
    dvt_lon = item['dvt_lon']

    row = [
        idx + 1,                         # STT
        item['ten'],                     # Tên hàng
        "",                              # Merge với B
        "",                              # Quy cách
        dvt_lon,                         # ĐVT
        int(so_luong_lon),              # Số lượng
        f"Phục vụ {so_khach} khách - {goi_dv}"  # Mục đích
    ]
    data_rows.append(row)

# Điền vào sheet
end_row = DATA_START_ROW + len(data_rows) - 1
update_cells(spreadsheet_id, new_sheet_name, f"A{DATA_START_ROW}:G{end_row}", data_rows)

print(f"✅ Đã điền {len(data_rows)} items vào phiếu")
```

### Bước 5: Lưu Metadata - Sheet "Phiếu Mua Hàng"
```python
phieu_data = get_sheet_data(spreadsheet_id, "Phiếu Mua Hàng", include_grid_data=False)
next_row = len(phieu_data['valueRanges'][0]['values']) + 1

# Tính tổng
tong_so_luong_lon = sum(item['can_mua_lon'] for item in can_mua_list)

metadata = [[
    new_sheet_name,
    datetime.now().strftime("%d/%m/%Y"),
    "Phòng Xét Nghiệm",
    "Phòng XN",
    "VTTH/Hóa Chất",
    so_khach,
    goi_dv,
    f"Mua cho {so_khach} khách - {goi_dv}",
    len(can_mua_list),
    tong_so_luong_lon,
    "Đã tạo",
    "Copy từ template, dùng đơn vị lớn (ROUNDUP)",
    "",
    ",".join([item['ten'] for item in can_mua_list[:10]])
]]

update_cells(spreadsheet_id, "Phiếu Mua Hàng", f"A{next_row}:N{next_row}", metadata)
print("✅ Đã lưu metadata vào 'Phiếu Mua Hàng'")
```

### Bước 6: Lưu Chi Tiết - Sheet "Chi Tiết Phiếu Mua Hàng"
```python
chi_tiet_data = get_sheet_data(spreadsheet_id, "Chi Tiết Phiếu Mua Hàng", include_grid_data=False)
next_row_ct = len(chi_tiet_data['valueRanges'][0]['values']) + 1

chi_tiet = []
for item in can_mua_list:
    chi_tiet.append([
        item['ten'],
        new_sheet_name,
        int(item['can_mua_lon']),
        item['dvt_lon'],
        "",
        f"Phục vụ {so_khach} khách - {goi_dv}",
        "", "", ""
    ])

end_row_ct = next_row_ct + len(chi_tiet) - 1
update_cells(spreadsheet_id, "Chi Tiết Phiếu Mua Hàng", f"A{next_row_ct}:I{end_row_ct}", chi_tiet)
print("✅ Đã lưu chi tiết vào 'Chi Tiết Phiếu Mua Hàng'")
```

### Bước 7: Thông Báo Hoàn Thành
```markdown
✅ Đã tạo Phiếu Mua Hàng thành công!

📋 Thông tin phiếu:
- Tên sheet: Phiếu_20250202_143052
- Link: https://docs.google.com/spreadsheets/d/1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800

📊 Tóm tắt:
- Số lượng mặt hàng: 15
- Tổng SL cần mua: 8 hộp (đơn vị lớn - đã ROUNDUP)
- Gói dịch vụ: B2B-Gói đồng
- Số khách hàng: 300

⚠️ LƯU Ý QUAN TRỌNG:
✅ So sánh tồn kho: Dùng đơn vị nhỏ (lọ, miếng)
✅ Phiếu mua hàng: Dùng đơn vị lớn (hộp) - ROUNDUP
✅ Ví dụ: 0.5 hộp → 1 hộp, 1.3 hộp → 2 hộp

🔗 [Mở Phiếu Mua Hàng](https://docs.google.com/spreadsheets/d/1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800)
```

## Template Structure

### Phiếu mua hàng mẫu version 1

```
Row 1: PHIẾU MUA HÀNG (Title)
Row 2: (Blank)
Row 3: 1. Ngày lập: [DATE]
Row 4: 2. Người đề nghị: [NAME]    Phòng ban: [DEPT]
Row 5: 3. Nội dung: [CONTENT]
Row 6-7: (Blank)
Row 8: HEADER (STT | Tên hàng | ... | Mục đích)
Row 9+: DATA (điền từ đây)

Columns:
A: STT
B-C: Tên hàng (merged)
D: Quy cách
E: ĐVT
F: Số lượng
G: Mục đích
```

## Sheet Name Format

```
Phiếu_YYYYMMDD_HHMMSS

Ví dụ:
- Phiếu_20250202_143052
- Phiếu_20250202_151230
- Phiếu_20250203_090000
```

## Output

### Google Sheets Link
```
https://docs.google.com/spreadsheets/d/1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800
```

### Thông Tin Phiếu
- Tên sheet
- Ngày lập
- Số lượng mặt hàng
- Tổng số lượng (đơn vị lớn)
- Gói dịch vụ
- Số khách hàng

## Agent Used

Command này sử dụng **Purchase Order Creator Agent** (`purchase-order-creator.md`)

## Related Commands

- `/tinh-vtth` - Tính VTTH (bước 1)
- `/tinh-hoa-chat` - Tính hóa chất (bước 1)
- `/so-sanh-kho` - So sánh tồn kho (bước 2, BẮT BUỘC)
- `/kho` - Menu chính

## Error Handling

| Lỗi | Thông Báo |
|-----|-----------|
| Chưa so sánh kho | ❌ Chưa chạy /so-sanh-kho |
| Không có items cần mua | ✅ Tất cả ĐỦ KHO, không cần tạo phiếu |
| Template not found | ❌ Không tìm thấy template 'Phiếu mua hàng mẫu version 1' |
| Copy failed | ❌ Lỗi khi copy template. Kiểm tra permissions |
| Update failed | ❌ Lỗi khi cập nhật cells. Kiểm tra range |
| Duplicate sheet name | Dùng timestamp để tạo tên unique |

## CHECKLIST

Trước khi tạo phiếu, kiểm tra:
- [ ] Đã chạy /so-sanh-kho?
- [ ] Có ít nhất 1 item CẦN MUA?
- [ ] Đã lọc bỏ items ĐỦ KHO?
- [ ] Đã dùng `copy_sheet()`?
- [ ] Đã dùng đơn vị lớn?
- [ ] Đã ROUNDUP số lượng?
- [ ] Đã cập nhật header?
- [ ] Đã lưu metadata vào 2 sheets?
- [ ] Đã tạo link Google Sheets?

## Complete Workflow Example

```bash
# Bước 1: Tính hóa chất
/tinh-hoa-chat 300

# Bước 2: So sánh với tồn kho
/so-sanh-kho workspace/inventory-files/ton-kho.xlsx
# → Hỏi: Có muốn tạo phiếu? → CÓ

# Bước 3: Tạo phiếu (tự động hoặc manual)
/tao-phieu
# → Phiếu_20250202_143052 được tạo
```

## Notes

- **GIỮ NGUYÊN FORMAT** từ template bằng cách dùng `copy_sheet()`
- **ĐƠN VỊ LỚN** trong phiếu: Hộp, Chai, Thùng (KHÔNG phải lọ, miếng, ml)
- **ROUNDUP**: 0.5 → 1, 1.3 → 2 (LUÔN làm tròn lên)
- Phiếu tự động lưu vào Google Sheets, không cần export
- Metadata được lưu vào 2 sheets để tracking và reporting
