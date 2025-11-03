# COMPASS AGENTS - Hệ Thống Quản Lý AI Agents

Tập hợp các Claude Code AI Agents chuyên biệt. **Chỉ cần mở Claude Code và gõ `/` để chọn agent!**

## 📦 Cài Đặt

**Có 2 cách sử dụng COMPASS_AGENTS:**

### Cách 1: Sử Dụng Claude Code CLI (Terminal) - Khuyến Nghị

Sử dụng trực tiếp trong terminal mà không cần mở VS Code.

**👉 [Xem Hướng Dẫn Cài Đặt Chi Tiết](./INSTALL_GUIDE.md)**

**Tóm tắt:**
```bash
# 1. Cài Node.js (nếu chưa có)
# Download từ: https://nodejs.org/

# 2. Cài Claude Code CLI
npm install -g @anthropic-ai/claude-code

# 3. Cấu hình API Key
claude config

# 4. Clone COMPASS_AGENTS
git clone https://github.com/Nathan-Nguyen-Tech/COMPASS_AGENTS.git
cd COMPASS_AGENTS

# 5. Khởi động Claude
claude

# 6. Sử dụng slash commands
> /agents
> /bo-kho
```

### Cách 2: Sử Dụng Trong VS Code

#### Bước 1: Clone Repository

```bash
git clone https://github.com/Nathan-Nguyen-Tech/COMPASS_AGENTS.git
cd COMPASS_AGENTS
```

#### Bước 2: Mở trong VS Code

```bash
code .
```

#### Bước 3: Mở Claude Code

Trong VS Code:
- Nhấn `Ctrl+Shift+P` (hoặc `Cmd+Shift+P` trên Mac)
- Gõ "Claude Code: Open"
- Hoặc click vào icon Claude Code ở sidebar

### Bước 4: Sử dụng Slash Commands

Trong Claude Code, gõ `/` để xem danh sách agents. Agents được tổ chức theo bộ phận:

```
/agents          - Xem tất cả agents (tổ chức theo bộ phận)

Back-Office (BO):
/bo-kho          - Hệ thống mua hàng tự động

Compass (Dùng chung):
/compass-learn   - Trợ lý học công nghệ
/compass-meta    - Claude Code project builder
```

**Mẹo:** Gõ tiền tố bộ phận để filter (ví dụ: `/bo-` cho Back-Office, `/compass-` cho agents dùng chung)

## 📋 Tổng Quan

COMPASS AGENTS cho phép bạn:
- ✅ **Chọn agent bằng slash commands** - Gõ `/` → Chọn agent
- ✅ **Làm việc trong Claude Code** - Chat tự nhiên với AI
- ✅ **Auto-load context** - Tự động đọc CLAUDE.md của agent
- ✅ **Quản lý nhiều agents** từ một workspace
- ✅ **Chuyển đổi nhanh** giữa các agents

## 🚀 Quickstart

**Cách sử dụng đơn giản nhất:**

1. Mở VS Code tại thư mục COMPASS_AGENTS
2. Mở Claude Code (Ctrl+Shift+P → "Claude Code: Open")
3. Gõ `/agents` để xem danh sách
4. Chọn agent bạn muốn dùng (vd: `/kho`)
5. Bắt đầu chat!

**Ví dụ:**
```
You: /bo-kho
Claude: [Chuyển sang BO_KHO_MUA_HANG_THEO_TARGET agent]
        Bạn muốn làm gì hôm nay?

You: Tính VTTH cho 100 khách hàng
Claude: [Thực hiện tính toán...]
```

## 💡 Cách Sử Dụng

### Sử dụng Slash Commands (Khuyến nghị)

**Đây là cách đơn giản và hiệu quả nhất:**

1. Mở VS Code tại thư mục COMPASS_AGENTS
2. Mở Claude Code
3. Gõ `/` và chọn agent

**Ví dụ workflow:**
```
You: /agents
Claude: [Hiển thị danh sách agents theo bộ phận]

You: /bo-kho
Claude: [Chuyển sang agent mua hàng]
        Bạn muốn làm gì hôm nay?

You: Tính VTTH cho 100 khách hàng
Claude: [Thực hiện...]
```

### Sử dụng CLI (Tùy chọn)

Nếu bạn muốn dùng terminal, vẫn có sẵn CLI tool:

```bash
# Xem danh sách agents
python compass.py list

# Xem thông tin agent
python compass.py info <agent-id>

# Mở VS Code tại thư mục agent
python compass.py open <agent-id>
```

**Lưu ý:** CLI chỉ dùng để quản lý files, không thể chat với AI. Để chat với agent, bạn cần dùng Claude Code.

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

### Workflow 1: Làm việc với agent Mua Hàng (Back-Office)

```
You: /agents
Claude: [Hiển thị danh sách tất cả agents theo bộ phận]

You: /bo-kho
Claude: Bạn muốn làm gì hôm nay?

You: Tính VTTH cho 150 khách hàng, gọi đông
Claude: [cd BO_KHO_MUA_HANG_THEO_TARGET]
        [Thực hiện tính toán VTTH...]
        [Hiển thị kết quả]

You: Tạo phiếu mua hàng
Claude: [Tạo phiếu mua hàng trong Google Sheets]
```

### Workflow 2: Học công nghệ mới (Compass - Dùng chung)

```
You: /compass-learn
Claude: Bạn muốn học công nghệ gì hôm nay?

You: Tôi muốn học React Hooks
Claude: [cd tech-learning-assistant]
        [Research Agent tìm tài liệu...]
        [Tạo study guide 8 tuần]
        [Tổ chức tài liệu vào workspace/]

You: /youtube https://youtube.com/watch?v=...
Claude: [Trích xuất transcript từ video]
        [Lưu vào context/research/]
```

### Workflow 3: Tạo Claude Code project mới (Compass - Dùng chung)

```
You: /compass-meta
Claude: Bạn muốn tạo project mới hay làm việc với project hiện có?

You: Tạo project mới tên "inventory-tracker"
Claude: [cd claude-code-meta-builder]
        [Tạo cấu trúc project chuẩn]
        [Setup agents, commands, workspace]
        [Generate documentation templates]
```

### Workflow 4: Thêm agent mới vào COMPASS_AGENTS

```bash
# Bước 1: Tạo thư mục agent mới
mkdir my-new-agent
cd my-new-agent

# Bước 2: Tạo cấu trúc chuẩn (dùng /meta)
# Trong Claude Code:
/meta
"Tạo structure cho agent my-new-agent"

# Bước 3: Quay về COMPASS_AGENTS và tạo slash command
cd ..
# Tạo file .claude/commands/my-agent.md

# Bước 4: Reload Claude Code và test
/my-agent
```

## 🔧 Yêu Cầu Hệ Thống

- **Python 3.6+** (đã cài đặt sẵn trên hầu hết các hệ thống)
- **Windows/Linux/Mac** (cross-platform)

Không cần cài thêm thư viện Python nào, chỉ dùng standard library.

## 📊 Agents Hiện Có

Agents được tổ chức theo 4 bộ phận: **Back-Office (BO)**, **Business Development (BD)**, **Clinic**, và **Compass (Dùng chung)**.

### 🏥 Back-Office (BO)

#### `/bo-kho` - Hệ Thống Mua Hàng Tự Động
**Project:** `BO_KHO_MUA_HANG_THEO_TARGET`

Hệ thống tự động mua hàng cho phòng xét nghiệm y tế, tích hợp với Google Sheets.

**Chức năng:**
- Tính toán nhu cầu VTTH và Hóa Chất
- So sánh với tồn kho
- Tạo phiếu mua hàng tự động

**Slash commands bên trong:**
- `/tinh-vtth` - Tính VTTH
- `/tinh-hoa-chat` - Tính hóa chất
- `/so-sanh-kho` - So sánh kho
- `/tao-phieu` - Tạo phiếu

---

### 💼 Business Development (BD)

*Chưa có agents. Sẽ được thêm vào sau.*

**Quy tắc đặt tên:** `/bd-{tên-agent}`

---

### 🏥 Clinic

*Chưa có agents. Sẽ được thêm vào sau.*

**Quy tắc đặt tên:** `/clinic-{tên-agent}`

---

### 🧭 Compass (Dùng Chung)

Các agents này có sẵn cho tất cả bộ phận.

#### `/compass-learn` - Tech Learning Assistant
**Project:** `tech-learning-assistant`

Trợ lý học công nghệ mới, thu thập và tổ chức tài liệu học tập.

**Chức năng:**
- Tìm kiếm tài liệu học tập chất lượng cao
- Trích xuất nội dung từ video tutorials
- Tạo study guides và learning paths
- Xây dựng lộ trình học tập cá nhân

**Slash commands bên trong:**
- `/learn <topic>` - Bắt đầu học
- `/youtube <url>` - Trích xuất video
- `/summarize` - Tóm tắt tài liệu

#### `/compass-meta` - Claude Code Meta-Builder
**Project:** `claude-code-meta-builder`

Hệ thống tạo và tối ưu hóa các dự án Claude Code AI agents.

**Chức năng:**
- Tạo cấu trúc dự án Claude Code chuẩn
- Setup agents, commands, và workspace
- Nghiên cứu patterns và best practices
- Tối ưu hóa existing projects

---

## 📝 Quy Tắc Đặt Tên Agents

Khi tạo agent mới, tuân theo quy tắc:

| Bộ Phận | Prefix | Ví Dụ |
|---------|--------|-------|
| Back-Office | `bo-` | `/bo-kho`, `/bo-inventory`, `/bo-accounting` |
| Business Development | `bd-` | `/bd-sales`, `/bd-leads`, `/bd-pipeline` |
| Clinic | `clinic-` | `/clinic-patients`, `/clinic-schedule` |
| Compass (Dùng chung) | `compass-` | `/compass-learn`, `/compass-meta` |

**Lợi ích:**
- ✅ Dễ phân biệt agents theo bộ phận
- ✅ Autocomplete thông minh (gõ `/bo-` để thấy tất cả Back-Office agents)
- ✅ Tránh trùng tên giữa các bộ phận
- ✅ Dễ quản lý khi có nhiều agents

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

## 🔄 Cập Nhật Code Mới Từ GitHub

### Cách 1: Pull code mới nhất (Khuyến nghị)

```bash
# Di chuyển vào thư mục COMPASS_AGENTS
cd COMPASS_AGENTS

# Pull code mới nhất từ GitHub
git pull origin main

# Quét lại agents (nếu có agent mới)
python compass.py scan
```

### Cách 2: Xem thay đổi trước khi pull

```bash
# Kiểm tra xem có cập nhật mới không
git fetch origin
git status

# Xem chi tiết những gì sẽ được cập nhật
git log HEAD..origin/main --oneline

# Pull về
git pull origin main
```

### Cách 3: Reset về phiên bản GitHub (Nếu có conflict)

**⚠️ CẢNH BÁO: Lệnh này sẽ XÓA tất cả thay đổi local của bạn!**

```bash
# Backup thay đổi của bạn trước (nếu cần)
git stash

# Reset về phiên bản GitHub
git fetch origin
git reset --hard origin/main

# Lấy lại thay đổi đã backup (nếu cần)
git stash pop
```

### Kiểm Tra Phiên Bản

```bash
# Xem commit hiện tại
git log -1 --oneline

# Xem lịch sử cập nhật
git log --oneline -10
```

## 📝 Đóng Góp

Nếu bạn muốn thêm tính năng hoặc sửa lỗi:

### Cho người dùng:
1. Fork repository trên GitHub
2. Clone fork của bạn về máy
3. Tạo branch mới: `git checkout -b feature/ten-tinh-nang`
4. Thực hiện thay đổi và commit: `git commit -m "Thêm tính năng X"`
5. Push lên fork: `git push origin feature/ten-tinh-nang`
6. Tạo Pull Request trên GitHub

### Cho maintainers:
1. Thực hiện thay đổi local
2. Commit: `git add . && git commit -m "Mô tả thay đổi"`
3. Push lên GitHub: `git push origin main`
4. Người dùng sẽ pull về bằng `git pull`

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
