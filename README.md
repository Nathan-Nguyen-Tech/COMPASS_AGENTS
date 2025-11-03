# COMPASS AGENTS - Hệ Thống Quản Lý AI Agents

Hệ thống CLI siêu đơn giản để quản lý và sử dụng các Claude Code AI Agents. **Chỉ cần gõ `compass` và chọn số!**

## 📋 Tổng Quan

COMPASS AGENTS cho phép bạn:
- ✅ **Chọn agent chỉ với 2 bước** - Gõ `compass` → Chọn số
- ✅ **Làm việc ngay trong session hiện tại** - Không cần mở terminal mới
- ✅ **Auto-load context** - Tự động đọc CLAUDE.md của agent
- ✅ **Quản lý nhiều agents** từ một nơi
- ✅ **Tự động phát hiện agents mới**

## 🚀 Quickstart (2 Bước)

```bash
# Bước 1: Chạy compass
compass

# Bước 2: Chọn số agent (VD: 1)
1

# ✅ XONG! Agent sẵn sàng làm việc!
```

## 🚀 Cài Đặt & Sử Dụng

### Cách 1: Sử Dụng Trực Tiếp (Không cần cài đặt)

```bash
# Chạy ngay
python compass.py

# Chọn số agent
1
```

### Cách 2: Setup PATH (Khuyến Nghị - Chỉ làm 1 lần)

**Windows:**
```cmd
setx PATH "%PATH%;D:\Compass_Coding\COMPASS_AGENTS"
```

**Linux/Mac:**
```bash
# Thêm vào ~/.bashrc hoặc ~/.zshrc
alias compass='python3 /path/to/COMPASS_AGENTS/compass.py'
source ~/.bashrc
```

**Sau khi setup, chỉ cần:**
```bash
compass
```

## 🎯 Các Lệnh Chính

### 1. Quét và cập nhật danh sách agents

```bash
compass scan
```

Lệnh này sẽ:
- Tự động tìm tất cả các thư mục con có file `CLAUDE.md`
- Đọc thông tin từ `CLAUDE.md` và `README.md`
- Lưu vào file `agents.json`

### 2. Xem danh sách agents (Interactive)

```bash
compass list
# hoặc
compass ls
```

**Tính năng mới: Interactive Mode!**

Sau khi hiển thị danh sách, bạn có thể:
- Nhập số (1, 2, 3...) để chọn và chạy agent ngay lập tức
- Nhấn Enter để thoát

Ví dụ:
```
[*] Danh sach Agents:

1. Hệ Thống Tự Động Mua Hàng - Phòng Xét Nghiệm
   ID: BO_KHO_MUA_HANG_THEO_TARGET
   ...

2. Tech Learning Assistant
   ID: tech-learning-assistant
   ...

============================================================
Chon agent de chay (nhap so 1-2, hoac Enter de thoat): 1

[+] Chay Agent: Hệ Thống Tự Động Mua Hàng...
```

### 2b. Chạy agent trực tiếp

```bash
compass run <agent-id>
```

Ví dụ:
```bash
compass run tech-learning-assistant
```

Lệnh này sẽ:
- Hiển thị thông tin agent
- Hỏi có muốn mở terminal mới không
- Mở terminal tại thư mục agent (nếu chọn yes)
- Hoặc hiển thị lệnh cd (nếu chọn no)

### 3. Xem thông tin chi tiết

```bash
compass info <agent-id>
```

Ví dụ:
```bash
compass info BO_KHO_MUA_HANG_THEO_TARGET
compass info tech-learning-assistant
compass info claude-code-meta-builder
```

Hiển thị:
- Thông tin đầy đủ về agent
- Cấu trúc thư mục
- Các file quan trọng có sẵn

### 4. Mở terminal tại thư mục agent (Nhanh)

```bash
compass open <agent-id>
```

Ví dụ:
```bash
compass open tech-learning-assistant
```

Lệnh này sẽ mở một terminal/cmd mới tại thư mục của agent ngay lập tức (không hỏi).

### 5. Lấy lệnh cd để chuyển thư mục

```bash
compass cd <agent-id>
```

Hiển thị lệnh cd để bạn có thể copy và chạy trong terminal hiện tại.

### 6. Xem hướng dẫn

```bash
compass help
```

## 📁 Cấu Trúc Thư Mục

```
COMPASS_AGENTS/
├── compass.py              # CLI script chính (Python)
├── compass.bat             # Wrapper cho Windows
├── compass.sh              # Wrapper cho Linux/Mac
├── agents.json             # Cấu hình agents (tự động tạo)
├── README.md               # File này
│
├── BO_KHO_MUA_HANG_THEO_TARGET/     # Agent 1
│   ├── CLAUDE.md
│   ├── README.md
│   └── ...
│
├── tech-learning-assistant/          # Agent 2
│   ├── CLAUDE.md
│   ├── README.md
│   └── ...
│
└── claude-code-meta-builder/         # Agent 3
    ├── CLAUDE.md
    ├── README.md
    └── ...
```

## 🎨 Ví Dụ Sử Dụng

### Workflow 1: Khám phá agents có sẵn

```bash
# Bước 1: Quét agents
compass scan

# Bước 2: Xem danh sách
compass list

# Bước 3: Xem chi tiết
compass info tech-learning-assistant
```

### Workflow 2: Chạy agent nhanh nhất (KHUYẾN NGHỊ)

```bash
# Cách 1: Interactive - Chọn từ danh sách
compass list
# Nhập số agent (VD: 1) để chạy ngay

# Cách 2: Chạy trực tiếp
compass run tech-learning-assistant
# Chọn y để mở terminal mới
```

### Workflow 3: Làm việc với một agent (Các cách khác)

```bash
# Cách 1: Mở terminal mới nhanh (không hỏi)
compass open BO_KHO_MUA_HANG_THEO_TARGET

# Cách 2: Lấy lệnh cd
compass cd BO_KHO_MUA_HANG_THEO_TARGET
# Sau đó copy lệnh cd và chạy
```

### Workflow 3: Thêm agent mới

```bash
# Bước 1: Tạo thư mục mới với cấu trúc agent
mkdir new-agent
cd new-agent
# Tạo các file cần thiết (CLAUDE.md, README.md, etc.)

# Bước 2: Quay lại thư mục gốc và quét lại
cd ..
compass scan

# Bước 3: Kiểm tra agent mới
compass list
compass info new-agent
```

## 🔧 Yêu Cầu Hệ Thống

- **Python 3.6+** (đã cài đặt sẵn trên hầu hết các hệ thống)
- **Windows/Linux/Mac** (cross-platform)

Không cần cài thêm thư viện Python nào, chỉ dùng standard library.

## 📊 Agents Hiện Có

### 1. BO_KHO_MUA_HANG_THEO_TARGET
Hệ thống tự động mua hàng cho phòng xét nghiệm y tế, tích hợp với Google Sheets.

**Chức năng:**
- Tính toán nhu cầu VTTH và Hóa Chất
- So sánh với tồn kho
- Tạo phiếu mua hàng tự động

### 2. tech-learning-assistant
Trợ lý học công nghệ mới, thu thập và tổ chức tài liệu học tập.

**Chức năng:**
- Tìm kiếm tài liệu học tập
- Trích xuất nội dung từ video
- Tạo study guides
- Tổ chức kiến thức

### 3. claude-code-meta-builder
Hệ thống tạo và tối ưu hóa các dự án Claude Code AI agents.

**Chức năng:**
- Tạo cấu trúc dự án Claude Code
- Phân tích và tối ưu hóa agents
- Nghiên cứu và phát triển patterns
- Tạo documentation

## 🔐 Bảo Mật

- File `agents.json` chỉ chứa thông tin cấu trúc (không có credentials)
- Không đọc hoặc lưu nội dung nhạy cảm
- Chỉ quét các thư mục có file `CLAUDE.md` công khai

## 🐛 Troubleshooting

### Lỗi: "python: command not found"
- **Windows**: Cài Python từ python.org và thêm vào PATH
- **Linux/Mac**: Thử `python3` thay vì `python`

### Lỗi: "compass: command not found"
- Kiểm tra đã thêm thư mục vào PATH chưa
- Thử chạy trực tiếp: `python compass.py`

### Không tìm thấy agents
- Chạy `compass scan` để quét lại
- Kiểm tra các thư mục con có file `CLAUDE.md` không

### Terminal không mở
- **Windows**: Thử chạy từ Command Prompt
- **Linux/Mac**: Kiểm tra terminal emulator đã cài đặt chưa

## 🚧 Tính Năng Sắp Tới

- [ ] Chạy commands trực tiếp cho agents
- [ ] Tìm kiếm agents theo từ khóa
- [ ] Export/import cấu hình agents
- [ ] Tạo agents mới từ template
- [ ] Agent health check
- [ ] Cập nhật tự động

## 📝 Đóng Góp

Nếu bạn muốn thêm tính năng hoặc sửa lỗi:
1. Fork repository
2. Tạo branch mới
3. Commit changes
4. Tạo Pull Request

## 📄 License

MIT License - Tự do sử dụng và chỉnh sửa

## 🙋 Hỗ Trợ

Nếu gặp vấn đề hoặc có câu hỏi, hãy:
- Kiểm tra phần Troubleshooting
- Xem lại hướng dẫn cài đặt
- Chạy `compass help` để xem các lệnh

---

**Phiên bản:** 1.0.0
**Cập nhật:** 2025-11-02
**Tác giả:** Compass Coding Team
