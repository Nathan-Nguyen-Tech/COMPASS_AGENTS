# COMPASS AGENTS - Hướng Dẫn Bắt Đầu Nhanh

## 🚀 Bắt đầu SIÊU ĐƠN GIẢN - Chỉ 2 bước!

### Bước 1: Chạy COMPASS

```bash
python compass.py
```

Hoặc nếu đã setup PATH:
```bash
compass
```

### Bước 2: Chọn số agent

Danh sách sẽ hiển thị:
```
1. Hệ Thống Tự Động Mua Hàng - Phòng Xét Nghiệm
   ID: BO_KHO_MUA_HANG_THEO_TARGET

2. Claude Code Meta-Builder
   ID: claude-code-meta-builder

3. Tech Learning Assistant
   ID: tech-learning-assistant

Chon agent de chay (nhap so 1-3, hoac Enter de thoat): █
```

**Nhập số (VD: 1) và Enter**

### ✅ XONG! Agent sẵn sàng làm việc trong session hiện tại!

```
============================================================
    AGENT: Hệ Thống Tự Động Mua Hàng - Phòng Xét Nghiệm
============================================================

[*] Trang thai: Agent da san sang trong session hien tai!

[+] San sang lam viec! Ban can toi giup gi?
```

## 📝 Lưu Ý

- ✅ **KHÔNG cần** mở terminal mới
- ✅ **KHÔNG cần** cd vào thư mục
- ✅ Làm việc **NGAY** trong session hiện tại
- ✅ Claude Code đã đọc CLAUDE.md và hiểu rõ về agent

## 📖 Các Lệnh Khác

### Xem chi tiết về một agent

```bash
python compass.py info <agent-id>
```

Ví dụ:
```bash
python compass.py info BO_KHO_MUA_HANG_THEO_TARGET
```

### Xem hướng dẫn đầy đủ

```bash
python compass.py help
```

## ⚙️ Setup PATH (Optional)

Để có thể gọi `compass` từ bất kỳ đâu:

### Windows

1. Mở Command Prompt với quyền Administrator
2. Chạy:
```cmd
setx PATH "%PATH%;D:\Compass_Coding\COMPASS_AGENTS"
```

3. Đóng và mở lại terminal
4. Bây giờ có thể dùng `compass` thay vì `python compass.py`:
```cmd
compass scan
compass list
compass info tech-learning-assistant
```

### Linux/Mac

1. Thêm vào `~/.bashrc` hoặc `~/.zshrc`:
```bash
alias compass='python3 /path/to/COMPASS_AGENTS/compass.py'
```

2. Reload shell:
```bash
source ~/.bashrc
```

## 🎯 Use Cases

### Use Case 1: Khám phá agents

```bash
# 1. Quét agents
compass scan

# 2. Xem danh sách
compass list

# 3. Xem chi tiết từng agent
compass info BO_KHO_MUA_HANG_THEO_TARGET
compass info tech-learning-assistant
compass info claude-code-meta-builder
```

### Use Case 2: Làm việc với agent

```bash
# Cách 1: Mở terminal mới tại agent
compass open tech-learning-assistant

# Cách 2: Lấy lệnh cd để chuyển thư mục
compass cd tech-learning-assistant
# Copy và chạy lệnh được hiển thị
```

### Use Case 3: Thêm agent mới

```bash
# 1. Tạo thư mục agent mới
mkdir my-new-agent
cd my-new-agent

# 2. Tạo file CLAUDE.md (bắt buộc)
# Thêm nội dung hướng dẫn cho agent

# 3. Tạo file README.md (khuyến nghị)
# Thêm mô tả về agent

# 4. Quay lại thư mục gốc và quét lại
cd ..
compass scan

# 5. Kiểm tra agent mới
compass list
compass info my-new-agent
```

## 🐛 Troubleshooting

### Lỗi: "python: command not found"
```bash
# Thử dùng python3
python3 compass.py scan
```

### Lỗi: "compass: command not found"
```bash
# Chưa setup PATH, dùng đường dẫn đầy đủ
python D:\Compass_Coding\COMPASS_AGENTS\compass.py scan

# Hoặc cd vào thư mục trước
cd D:\Compass_Coding\COMPASS_AGENTS
python compass.py scan
```

### Không tìm thấy agents
```bash
# Đảm bảo mỗi agent có file CLAUDE.md
# Sau đó quét lại
compass scan
```

## 📚 Tài Liệu Đầy Đủ

Xem file `README.md` để có hướng dẫn chi tiết hơn về:
- Cài đặt và cấu hình
- Tất cả các lệnh
- Cấu trúc thư mục
- Các agent có sẵn
- Tính năng nâng cao

## 💡 Tips

1. **Luôn chạy `compass scan` sau khi thêm agent mới**
2. **Dùng `compass list` để xem tất cả agents**
3. **Dùng `compass info <id>` để xem chi tiết trước khi làm việc**
4. **Setup PATH để gọi nhanh hơn**

## 🔗 Links Nhanh

- [README đầy đủ](./README.md)
- [Agents có sẵn](#agents-có-sẵn)
  - [BO_KHO_MUA_HANG_THEO_TARGET](./BO_KHO_MUA_HANG_THEO_TARGET/)
  - [tech-learning-assistant](./tech-learning-assistant/)
  - [claude-code-meta-builder](./claude-code-meta-builder/)

---

**Bắt đầu ngay:** `python compass.py scan`
