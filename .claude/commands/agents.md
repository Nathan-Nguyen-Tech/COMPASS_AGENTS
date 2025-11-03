# Agents - Danh Sách Tất Cả Agents

Hiển thị danh sách tất cả agents có sẵn trong COMPASS_AGENTS, được tổ chức theo bộ phận.

## 🏢 Tổ Chức Theo Bộ Phận

Agents được phân theo 4 bộ phận:
- **Back-Office (BO):** Các agent cho bộ phận hậu cần
- **Business Development (BD):** Các agent cho bộ phận phát triển kinh doanh
- **Clinic:** Các agent cho phòng khám
- **Compass:** Các agent dùng chung cho tất cả bộ phận

**Mẹo:** Gõ tiền tố bộ phận để filter commands (ví dụ: gõ `/bo-` để thấy tất cả Back-Office agents)

---

## 🏥 Back-Office (BO)

### /bo-kho - Hệ Thống Mua Hàng Tự Động
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

## 💼 Business Development (BD)

*Chưa có agents. Sẽ được thêm vào sau.*

**Quy tắc đặt tên:** Các BD agents sẽ có prefix `/bd-`
- Ví dụ: `/bd-sales`, `/bd-leads`, `/bd-pipeline`

---

## 🏥 Clinic

*Chưa có agents. Sẽ được thêm vào sau.*

**Quy tắc đặt tên:** Các Clinic agents sẽ có prefix `/clinic-`
- Ví dụ: `/clinic-patients`, `/clinic-schedule`, `/clinic-records`

---

## 🧭 Compass (Dùng Chung)

Các agents này có sẵn cho tất cả bộ phận.

### /compass-learn - Tech Learning Assistant
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

### /compass-meta - Claude Code Meta-Builder
**Project:** `claude-code-meta-builder`

Tạo và tối ưu hóa Claude Code projects:
- Tạo project structure chuẩn
- Setup agents, commands, workspace
- Nghiên cứu best practices
- Tối ưu hóa projects

---

## 📝 Quy Tắc Đặt Tên

Khi tạo agent mới, tuân theo quy tắc:
- Back-Office: `bo-{tên-agent}`
- BD: `bd-{tên-agent}`
- Clinic: `clinic-{tên-agent}`
- Compass (dùng chung): `compass-{tên-agent}`

---

## Instructions

Hiển thị thông tin trên cho user và hỏi: "Bạn thuộc bộ phận nào? (Back-Office, BD, Clinic) hoặc muốn dùng Compass agents (dùng chung)?"
