# Workspace - Vùng Làm Việc

Thư mục này chứa dữ liệu làm việc thực tế, kết quả tính toán, file tồn kho, và lịch sử.

## 📁 Cấu Trúc

### calculations/
Kết quả tính toán VTTH và Hóa Chất
- `vtth_YYYYMMDD_HHMMSS.json` - Kết quả tính VTTH
- `hoa_chat_YYYYMMDD_HHMMSS.json` - Kết quả tính Hóa Chất
- `comparison_YYYYMMDD_HHMMSS.json` - Kết quả so sánh tồn kho

### inventory-files/
File tồn kho upload từ user
- Format hỗ trợ: `.xlsx`, `.csv`
- Cột bắt buộc: "Tên sản phẩm", "Tồn kho"

### purchase-orders/
Lịch sử phiếu mua hàng đã tạo
- Export từ Google Sheets (nếu cần)
- Backup metadata

## 🔒 Bảo Mật

**QUAN TRỌNG:**
- Các folder này được `.gitignore` để bảo vệ dữ liệu
- File Excel/CSV tồn kho KHÔNG được commit vào git
- Chỉ commit cấu trúc folder (.gitkeep)

## 📝 Quy Ước Đặt Tên

### Kết quả tính toán
```
vtth_20250202_143052.json
hoa_chat_20250202_143052.json
comparison_20250202_143052.json
```

Format: `{type}_{timestamp}.json`

### File tồn kho
```
ton-kho-thang-2-2025.xlsx
ton-kho-2025-02-02.csv
inventory-february.xlsx
```

Đặt tên rõ ràng, có ngày tháng.

## 🗂️ Quản Lý File

### Dọn dẹp định kỳ
- Xóa file tính toán > 30 ngày
- Lưu trữ file tồn kho quan trọng
- Backup phiếu mua hàng

### Backup
Nên backup định kỳ:
- File tồn kho: Hàng tuần
- Kết quả tính toán: Hàng tháng
- Phiếu mua hàng: Lưu trên Google Sheets (tự động)

---

*Lưu ý: Không commit file dữ liệu thực tế vào git!*
