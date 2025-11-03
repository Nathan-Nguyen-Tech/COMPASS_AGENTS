# Agents - Danh Sách Tất Cả Agents

Hiển thị danh sách tất cả agents có sẵn trong COMPASS_AGENTS.

## Available Agents

### 1. 🏥 /kho - Hệ Thống Mua Hàng Tự Động
**Project:** `BO_KHO_MUA_HANG_THEO_TARGET`

Quản lý mua hàng cho phòng xét nghiệm y tế:
- Tính toán nhu cầu VTTH và Hóa Chất
- So sánh với tồn kho
- Tạo phiếu mua hàng tự động

**Commands trong project:**
- `/tinh-vtth` - Tính VTTH
- `/tinh-hoa-chat` - Tính hóa chất
- `/so-sanh-kho` - So sánh kho
- `/tao-phieu` - Tạo phiếu mua hàng

---

### 2. 📚 /learn - Tech Learning Assistant
**Project:** `tech-learning-assistant`

Trợ lý học công nghệ mới:
- Thu thập tài liệu học tập chất lượng cao
- Trích xuất nội dung từ video tutorials
- Tạo study guides và learning paths
- Xây dựng lộ trình học tập

**Commands trong project:**
- `/learn <topic>` - Bắt đầu học
- `/youtube <url>` - Trích xuất video
- `/summarize` - Tóm tắt tài liệu

---

### 3. 🏗️ /meta - Claude Code Meta-Builder
**Project:** `claude-code-meta-builder`

Tạo và tối ưu hóa Claude Code projects:
- Tạo project structure chuẩn
- Setup agents, commands, workspace
- Nghiên cứu best practices
- Tối ưu hóa projects

---

## Instructions

Hiển thị thông tin trên cho user và hỏi: "Bạn muốn sử dụng agent nào? (Gõ /kho, /learn, hoặc /meta)"
