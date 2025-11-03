# Hướng Dẫn Cài Đặt COMPASS_AGENTS

Hướng dẫn chi tiết để cài đặt và sử dụng COMPASS_AGENTS cho tất cả bộ phận.

## 📋 Mục Lục

1. [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
2. [Cài Đặt Claude Code CLI](#cài-đặt-claude-code-cli)
3. [Clone COMPASS_AGENTS](#clone-compass_agents)
4. [Sử Dụng Claude CLI](#sử-dụng-claude-cli)
5. [Troubleshooting](#troubleshooting)

---

## 🔧 Yêu Cầu Hệ Thống

### Windows
- Windows 10 trở lên
- Node.js 18+ (để cài Claude CLI)
- Git (để clone repository)
- PowerShell hoặc Command Prompt

### Mac/Linux
- macOS 11+ hoặc Ubuntu 20.04+
- Node.js 18+
- Git
- Terminal/Bash

---

## 📦 Cài Đặt Claude Code CLI

### Bước 1: Cài Đặt Node.js

**Windows:**
1. Tải Node.js từ: https://nodejs.org/
2. Download bản **LTS** (Long Term Support)
3. Chạy installer và làm theo hướng dẫn
4. Khởi động lại Terminal sau khi cài xong

**Mac:**
```bash
# Sử dụng Homebrew
brew install node

# Hoặc tải từ: https://nodejs.org/
```

**Linux (Ubuntu/Debian):**
```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**Kiểm tra cài đặt:**
```bash
node --version
npm --version
```

Kết quả mong đợi:
```
v20.x.x
10.x.x
```

---

### Bước 2: Cài Đặt Claude Code CLI

**Cài đặt global qua npm:**

```bash
npm install -g @anthropic-ai/claude-code
```

**Trên Windows, nếu gặp lỗi permission:**
```powershell
# Chạy PowerShell với quyền Administrator
npm install -g @anthropic-ai/claude-code
```

**Trên Mac/Linux, nếu cần sudo:**
```bash
sudo npm install -g @anthropic-ai/claude-code
```

**Kiểm tra cài đặt:**
```bash
claude --version
```

Kết quả mong đợi:
```
2.0.31 (Claude Code)
```

---

### Bước 3: Cấu Hình Anthropic API Key

Claude CLI cần API key để hoạt động.

#### Lấy API Key:

1. Truy cập: https://console.anthropic.com/
2. Đăng nhập hoặc tạo tài khoản
3. Vào **API Keys** → Click **Create Key**
4. Copy API key (chỉ hiển thị 1 lần!)

#### Cấu hình API Key:

**Cách 1: Sử dụng lệnh config (Khuyến nghị)**
```bash
claude config
```

Làm theo hướng dẫn:
1. Nhập API key khi được hỏi
2. Chọn model mặc định (Sonnet 4.5 khuyến nghị)
3. Cấu hình sẽ được lưu tự động

**Cách 2: Thêm vào Environment Variable**

**Windows (PowerShell):**
```powershell
# Tạm thời (chỉ trong session hiện tại)
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."

# Vĩnh viễn (thêm vào User Environment Variables)
[System.Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', 'sk-ant-api03-...', 'User')
```

**Mac/Linux:**
```bash
# Thêm vào ~/.bashrc hoặc ~/.zshrc
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.bashrc
source ~/.bashrc
```

**Kiểm tra:**
```bash
claude config show
```

---

## 🚀 Clone COMPASS_AGENTS

### Bước 1: Clone Repository

```bash
# Clone về máy
git clone https://github.com/Nathan-Nguyen-Tech/COMPASS_AGENTS.git

# Di chuyển vào thư mục
cd COMPASS_AGENTS
```

### Bước 2: Kiểm Tra Cấu Trúc

```bash
# Xem danh sách agents
ls -la
# hoặc trên Windows:
dir
```

Bạn sẽ thấy:
```
.claude/                  # Chứa slash commands
BO_KHO_MUA_HANG_THEO_TARGET/
tech-learning-assistant/
claude-code-meta-builder/
README.md
```

---

## 💻 Sử Dụng Claude CLI

### Khởi Động Claude CLI

Trong thư mục COMPASS_AGENTS:

```bash
claude
```

Bạn sẽ thấy:
```
Claude Code v2.0.31
Sonnet 4.5 : Claude Max
D:\Compass_Coding\COMPASS_AGENTS

> /
```

### Xem Danh Sách Agents

Gõ `/` và nhấn Tab để xem tất cả slash commands có sẵn:

```
> /
/agents          Agents - Danh Sách Tất Cả Agents (project)
/bo-kho          Kho - Hệ thống Mua Hàng Tự Động (project)
/compass-learn   Learn - Tech Learning Assistant (project)
/compass-meta    Meta - Claude Code Meta-Builder (project)
...
```

### Sử Dụng Agents

**Xem danh sách theo bộ phận:**
```
> /agents
```

Claude sẽ hiển thị tất cả agents được tổ chức theo:
- Back-Office (BO)
- Business Development (BD)
- Clinic
- Compass (Dùng chung)

**Chọn agent theo bộ phận:**

```
> /bo-kho
```

Claude sẽ load context của agent và hỏi:
```
Bạn muốn làm gì hôm nay?
```

**Chat với agent:**
```
> Tính VTTH cho 100 khách hàng
```

Claude sẽ thực hiện tính toán dựa trên context của agent.

---

## 🎯 Workflow Cho Từng Bộ Phận

### Back-Office

```bash
# 1. Khởi động Claude
cd COMPASS_AGENTS
claude

# 2. Xem agents Back-Office
> /agents

# 3. Chọn agent (ví dụ: Mua Hàng)
> /bo-kho

# 4. Làm việc
> Tính VTTH cho 150 khách hàng, gọi đông
> Tạo phiếu mua hàng
```

### Business Development (BD)

```bash
# Tương tự, sử dụng các BD agents khi có
> /bd-sales
> /bd-leads
```

### Clinic

```bash
# Tương tự, sử dụng các Clinic agents khi có
> /clinic-patients
> /clinic-schedule
```

### Compass (Dùng Chung)

```bash
# Học công nghệ mới
> /compass-learn
> Tôi muốn học React Hooks

# Tạo Claude Code project mới
> /compass-meta
> Tạo project mới cho inventory tracking
```

---

## 🔍 Các Lệnh Hữu Ích

### Lệnh Slash Cơ Bản

```bash
/agents           # Xem danh sách tất cả agents
/help             # Xem hướng dẫn
/clear            # Xóa lịch sử chat
/config           # Mở config panel
/bashes           # Xem background tasks
```

### Filter Agents Theo Bộ Phận

**Gõ prefix để filter:**

```bash
/bo-      # Hiển thị tất cả Back-Office agents
/bd-      # Hiển thị tất cả BD agents
/clinic-  # Hiển thị tất cả Clinic agents
/compass- # Hiển thị tất cả Compass agents (dùng chung)
```

### Thoát Claude CLI

```bash
Ctrl + C    # hoặc
/exit       # hoặc
exit
```

---

## 🆕 Cập Nhật COMPASS_AGENTS

### Pull Code Mới

```bash
# Di chuyển vào thư mục COMPASS_AGENTS
cd COMPASS_AGENTS

# Pull code mới nhất
git pull origin main

# Khởi động lại Claude
claude
```

### Kiểm Tra Phiên Bản

```bash
# Xem commit hiện tại
git log -1 --oneline

# Xem lịch sử cập nhật
git log --oneline -5
```

---

## 🐛 Troubleshooting

### Lỗi: "claude: command not found"

**Nguyên nhân:** Claude CLI chưa được cài đặt hoặc PATH chưa đúng.

**Giải pháp:**
```bash
# Kiểm tra npm global bin
npm config get prefix

# Cài lại Claude CLI
npm install -g @anthropic-ai/claude-code

# Khởi động lại Terminal
```

### Lỗi: "API key not configured"

**Nguyên nhân:** Chưa cấu hình Anthropic API key.

**Giải pháp:**
```bash
# Cấu hình lại API key
claude config

# Hoặc set environment variable
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

### Lỗi: "Permission denied" (Windows)

**Nguyên nhân:** Không có quyền Administrator.

**Giải pháp:**
1. Mở PowerShell với quyền Administrator
2. Chạy lại lệnh cài đặt:
   ```powershell
   npm install -g @anthropic-ai/claude-code
   ```

### Lỗi: "/agents command not found"

**Nguyên nhân:** Đang ở sai thư mục hoặc chưa có `.claude/commands/`.

**Giải pháp:**
```bash
# Đảm bảo đang ở thư mục COMPASS_AGENTS
cd COMPASS_AGENTS
pwd  # Kiểm tra thư mục hiện tại

# Kiểm tra có .claude/commands/ không
ls .claude/commands/

# Nếu không có, pull lại code
git pull origin main
```

### Lỗi: "Node.js version too old"

**Nguyên nhân:** Node.js version < 18.

**Giải pháp:**
```bash
# Kiểm tra version
node --version

# Cập nhật Node.js lên version mới nhất
# Windows: Tải từ https://nodejs.org/
# Mac: brew upgrade node
# Linux: Xem hướng dẫn ở Bước 1
```

### Slash Commands Không Hiển Thị

**Nguyên nhân:** Claude CLI chưa load đúng thư mục.

**Giải pháp:**
```bash
# Thoát Claude
Ctrl + C

# Chuyển vào đúng thư mục
cd COMPASS_AGENTS

# Khởi động lại
claude
```

---

## 📞 Hỗ Trợ

Nếu gặp vấn đề, liên hệ:
- **Email:** support@compass.com (thay bằng email thực tế)
- **GitHub Issues:** https://github.com/Nathan-Nguyen-Tech/COMPASS_AGENTS/issues
- **IT Department:** Liên hệ bộ phận IT nội bộ

---

## 📚 Tài Liệu Tham Khảo

- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [COMPASS_AGENTS README](./README.md)
- [Anthropic Console](https://console.anthropic.com/)
- [Node.js Documentation](https://nodejs.org/docs/)

---

**Phiên bản:** 1.0.0
**Cập nhật:** 2025-11-03
**Tác giả:** Compass Coding Team
