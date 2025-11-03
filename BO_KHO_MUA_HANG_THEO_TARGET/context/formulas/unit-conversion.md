# Quy Đổi Đơn Vị - Unit Conversion

## 🎯 Mục Đích

Hướng dẫn chi tiết về quy đổi đơn vị trong hệ thống mua hàng, đặc biệt là **QUY TẮC VÀNG**: So sánh tồn kho bằng đơn vị nhỏ, phiếu mua hàng dùng đơn vị lớn.

---

## 📊 Cấu Trúc Đơn Vị

### Đơn Vị Nhỏ (DVT Nhỏ)
- **lọ**: Hóa chất thường đóng gói theo lọ
- **miếng**: VTTH như lammen, kim tiêm
- **ml**: Dung dịch, hóa chất lỏng

### Đơn Vị Lớn (DVT Lớn)
- **Hộp**: Đóng gói nhiều lọ/miếng
- **Chai**: Dung dịch, hóa chất lỏng
- **Thùng**: Số lượng lớn (VD: 20L)

### Tỷ Lệ Quy Đổi
```
1 Hộp = 100 lọ
1 Hộp = 50 miếng
1 Chai = 1000 ml
```

Ví dụ:
- GLUCOSE: 1 hộp = 100 lọ
- Lammen 22x22: 1 hộp = 100 miếng
- Dung dịch LYSE: 1 chai = 500 ml

---

## 🔴 QUY TẮC VÀNG #1: SO SÁNH TỒN KHO

### LUÔN So Sánh Bằng Đơn Vị Nhỏ!

**Tại sao?**
- Tồn kho có thể là số thập phân (1.2 hộp, 0.5 hộp)
- Nếu so sánh bằng đơn vị lớn sẽ CHO KẾT QUẢ SAI!

### Công Thức

```python
# Bước 1: Chuyển tồn kho sang đơn vị nhỏ
ton_kho_nho = ton_kho_lon × ty_le_quy_doi

# Bước 2: Chuyển nhu cầu sang đơn vị nhỏ (nếu chưa có)
nhu_cau_nho = nhu_cau_lon × ty_le_quy_doi

# Bước 3: So sánh
can_mua_nho = MAX(0, nhu_cau_nho - ton_kho_nho)

# Bước 4: Quy đổi sang đơn vị lớn CHO PHIẾU (ROUNDUP)
can_mua_lon = ⌈can_mua_nho ÷ ty_le_quy_doi⌉
```

### Ví Dụ Chi Tiết

#### Ví dụ 1: Tình huống đơn giản
```
Input:
- Sản phẩm: GLUCOSE
- Nhu cầu: 150 lọ
- Tồn kho: 1.2 hộp
- Tỷ lệ quy đổi: 100 lọ/hộp

Bước 1: Chuyển tồn kho sang đơn vị nhỏ
ton_kho_nho = 1.2 × 100 = 120 lọ

Bước 2: So sánh
can_mua_nho = 150 - 120 = 30 lọ

Bước 3: Quy đổi cho phiếu (ROUNDUP)
can_mua_lon = ⌈30 ÷ 100⌉ = ⌈0.3⌉ = 1 hộp ✅

---

❌ NẾU SO SÁNH BẰNG ĐƠN VỊ LỚN (SAI):
nhu_cau_lon = 150 ÷ 100 = 1.5 hộp
can_mua_lon = 1.5 - 1.2 = 0.3 hộp
→ ROUNDUP = 1 hộp

→ Kết quả tình cờ GIỐNG NHAU!
→ NHƯNG LOGIC SAI, sẽ sai trong trường hợp khác!
```

#### Ví dụ 2: Tình huống phức tạp hơn
```
Input:
- Sản phẩm: ALT
- Nhu cầu: 320 lọ
- Tồn kho: 1.5 hộp
- Tỷ lệ quy đổi: 100 lọ/hộp

✅ ĐÚNG (so sánh đơn vị nhỏ):
ton_kho_nho = 1.5 × 100 = 150 lọ
can_mua_nho = 320 - 150 = 170 lọ
can_mua_lon = ⌈170 ÷ 100⌉ = 2 hộp ✅

❌ SAI (so sánh đơn vị lớn):
nhu_cau_lon = 320 ÷ 100 = 3.2 hộp
can_mua_lon = 3.2 - 1.5 = 1.7 hộp
→ ROUNDUP = 2 hộp

→ Lại tình cờ giống!
```

#### Ví dụ 3: Tình huống SAI RÕ
```
Input:
- Sản phẩm: AST
- Nhu cầu: 80 lọ (ít hơn tồn kho!)
- Tồn kho: 1.2 hộp = 120 lọ
- Tỷ lệ quy đổi: 100 lọ/hộp

✅ ĐÚNG:
ton_kho_nho = 1.2 × 100 = 120 lọ
can_mua_nho = MAX(0, 80 - 120) = 0 lọ
→ Trạng thái: ĐỦ KHO ✅

❌ SAI:
nhu_cau_lon = 80 ÷ 100 = 0.8 hộp
can_mua_lon = MAX(0, 0.8 - 1.2) = 0 hộp
→ Trạng thái: ĐỦ KHO

→ Kết quả lại giống!

NHƯNG với tồn kho 0.9 hộp:
✅ ĐÚNG:
ton_kho_nho = 0.9 × 100 = 90 lọ
can_mua_nho = MAX(0, 80 - 90) = 0 lọ
→ ĐỦ KHO ✅

❌ SAI:
can_mua_lon = MAX(0, 0.8 - 0.9) = 0 hộp
→ ĐỦ KHO (giống nhau)

→ Vẫn giống!

KẾT LUẬN: Dù KẾT QUẢ CUỐI CÙNG có thể giống nhau,
NHƯNG LOGIC SO SÁNH BẰNG ĐƠN VỊ NHỎ mới CHÍNH XÁC VÀ ĐỒNG NHẤT!
```

---

## 🔴 QUY TẮC VÀNG #2: PHIẾU MUA HÀNG

### LUÔN Dùng Đơn Vị Lớn + ROUNDUP!

**Tại sao?**
- Không thể mua 0.3 hộp, phải mua nguyên hộp
- ROUNDUP đảm bảo đủ số lượng cần thiết

### Công Thức

```python
# Từ kết quả so sánh (đơn vị nhỏ)
can_mua_nho = 30  # lọ

# Quy đổi sang đơn vị lớn (ROUNDUP)
can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi)
```

### Ví Dụ ROUNDUP

```python
import math

# Ví dụ 1:
can_mua_nho = 30 lọ
ty_le_quy_doi = 100 lọ/hộp
can_mua_lon = math.ceil(30 / 100)  # ⌈0.3⌉ = 1 hộp ✅

# Ví dụ 2:
can_mua_nho = 150 lọ
can_mua_lon = math.ceil(150 / 100)  # ⌈1.5⌉ = 2 hộp ✅

# Ví dụ 3:
can_mua_nho = 100 lọ
can_mua_lon = math.ceil(100 / 100)  # ⌈1.0⌉ = 1 hộp ✅

# Ví dụ 4:
can_mua_nho = 101 lọ
can_mua_lon = math.ceil(101 / 100)  # ⌈1.01⌉ = 2 hộp ✅
```

### ❌ KHÔNG Làm Tròn Thông Thường

```python
# ❌ SAI - round() làm tròn gần nhất
can_mua_lon = round(0.3)  # = 0 → THIẾU HÀNG!
can_mua_lon = round(1.5)  # = 2 ✅ (tình cờ đúng)

# ❌ SAI - int() làm tròn xuống
can_mua_lon = int(0.3)  # = 0 → THIẾU HÀNG!
can_mua_lon = int(1.9)  # = 1 → THIẾU HÀNG!

# ✅ ĐÚNG - math.ceil() luôn làm tròn LÊN
can_mua_lon = math.ceil(0.3)  # = 1 ✅
can_mua_lon = math.ceil(1.9)  # = 2 ✅
can_mua_lon = math.ceil(1.0)  # = 1 ✅
```

---

## 📐 CÔNG THỨC TỔNG HỢP

### Từ Đầu Đến Cuối

```python
import math

# INPUT
so_khach = 300
dinh_muc = 0.5  # lọ/khách
ty_le_quy_doi = 100  # lọ/hộp
ton_kho_lon = 1.2  # hộp

# BƯỚC 1: Tính nhu cầu (đơn vị nhỏ)
nhu_cau_nho = so_khach * dinh_muc  # 300 × 0.5 = 150 lọ

# BƯỚC 2: Chuyển tồn kho sang đơn vị nhỏ
ton_kho_nho = ton_kho_lon * ty_le_quy_doi  # 1.2 × 100 = 120 lọ

# BƯỚC 3: So sánh (đơn vị nhỏ)
can_mua_nho = max(0, nhu_cau_nho - ton_kho_nho)  # 150 - 120 = 30 lọ

# BƯỚC 4: Quy đổi cho phiếu (đơn vị lớn + ROUNDUP)
can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi)  # ⌈30÷100⌉ = 1 hộp

# BƯỚC 5: Xác định trạng thái
if ton_kho_nho >= nhu_cau_nho:
    trang_thai = "ĐỦ KHO"
elif ton_kho_nho == 0:
    trang_thai = "HẾT KHO"
else:
    trang_thai = "CẦN MUA"

# OUTPUT
print(f"Nhu cầu: {nhu_cau_nho} lọ ({nhu_cau_nho/ty_le_quy_doi:.1f} hộp)")
print(f"Tồn kho: {ton_kho_nho} lọ ({ton_kho_lon} hộp)")
print(f"Cần mua: {can_mua_nho} lọ ({can_mua_lon} hộp)")
print(f"Trạng thái: {trang_thai}")
```

**Output:**
```
Nhu cầu: 150.0 lọ (1.5 hộp)
Tồn kho: 120.0 lọ (1.2 hộp)
Cần mua: 30.0 lọ (1 hộp)
Trạng thái: CẦN MUA
```

---

## 🎯 CHECKLIST

Trước khi tính toán, kiểm tra:

### So Sánh Tồn Kho
- [ ] Đã chuyển tồn kho sang đơn vị nhỏ?
- [ ] Đã chuyển nhu cầu sang đơn vị nhỏ (nếu cần)?
- [ ] Đã so sánh bằng đơn vị nhỏ?
- [ ] Đã dùng MAX(0, ...) để tránh âm?

### Phiếu Mua Hàng
- [ ] Đã quy đổi sang đơn vị lớn?
- [ ] Đã dùng math.ceil() (ROUNDUP)?
- [ ] Đã kiểm tra đơn vị lớn đúng? (Hộp, Chai, Thùng)
- [ ] Đã convert sang int() trước khi điền phiếu?

---

## ⚠️ LỖI THƯỜNG GẶP

### Lỗi 1: Quên chuyển tồn kho sang đơn vị nhỏ
```python
# ❌ SAI
can_mua = nhu_cau_nho - ton_kho_lon  # Sai đơn vị!

# ✅ ĐÚNG
ton_kho_nho = ton_kho_lon * ty_le_quy_doi
can_mua = nhu_cau_nho - ton_kho_nho
```

### Lỗi 2: Quên ROUNDUP khi quy đổi
```python
# ❌ SAI
can_mua_lon = can_mua_nho / ty_le_quy_doi  # 0.3 hộp → SAI!

# ✅ ĐÚNG
can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi)  # 1 hộp ✅
```

### Lỗi 3: Dùng round() thay vì ceil()
```python
# ❌ SAI
can_mua_lon = round(can_mua_nho / ty_le_quy_doi)  # 0.3 → 0 → THIẾU!

# ✅ ĐÚNG
can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi)  # 0.3 → 1 ✅
```

### Lỗi 4: Quên xử lý số âm
```python
# ❌ SAI
can_mua = nhu_cau - ton_kho  # Có thể âm!

# ✅ ĐÚNG
can_mua = max(0, nhu_cau - ton_kho)  # Luôn >= 0
```

---

## 📚 TÓM TẮT

### Quy Tắc Vàng

1. **SO SÁNH TỒN KHO**: Luôn dùng đơn vị nhỏ
2. **PHIẾU MUA HÀNG**: Luôn dùng đơn vị lớn + ROUNDUP
3. **ROUNDUP**: Dùng `math.ceil()`, KHÔNG dùng `round()` hay `int()`
4. **TRÁNH ÂM**: Dùng `max(0, ...)` khi tính cần mua

### Công Thức Tóm Tắt

```python
# So sánh (đơn vị nhỏ)
ton_kho_nho = ton_kho_lon × ty_le_quy_doi
can_mua_nho = MAX(0, nhu_cau_nho - ton_kho_nho)

# Phiếu (đơn vị lớn + ROUNDUP)
can_mua_lon = ⌈can_mua_nho ÷ ty_le_quy_doi⌉
```

**Luôn nhớ: NHỎ để so sánh, LỚN để mua, ROUNDUP để đủ!**
