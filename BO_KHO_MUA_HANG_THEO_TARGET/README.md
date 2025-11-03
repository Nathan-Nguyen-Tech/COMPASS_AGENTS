# BỘ KHO MUA HÀNG THEO TARGET

Hệ thống tự động tính toán nhu cầu mua hàng (VTTH và Hóa Chất) cho phòng xét nghiệm y tế, tích hợp với Google Sheets.

---

## 🎯 Tính Năng Chính

### ✅ Tính Toán Tự Động
- **Tính VTTH**: Vật tư tiêu hao theo số khách hàng và gói dịch vụ
- **Tính Hóa Chất**: Bao gồm QC/CALIB tự động
- **Quy đổi đơn vị**: Chính xác với ROUNDUP

### ✅ So Sánh Tồn Kho
- Đọc file Excel/CSV tồn kho
- **So sánh bằng đơn vị nhỏ** (quy tắc vàng!)
- Xác định: ĐỦ KHO / CẦN MUA / HẾT KHO

### ✅ Tạo Phiếu Tự Động
- Copy template từ Google Sheets
- Giữ nguyên 100% format
- Tự động điền dữ liệu
- Lưu metadata để tracking

---

## 🚀 Quick Start

### 1. Cài Đặt Dependencies

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
pip install -r tools/requirements.txt
```

### 2. Cấu Hình Credentials

Copy service account credentials vào `config/`:

```bash
cp c:\Users\nguye\Desktop\AI\config\service-account-key.json config/
```

### 3. Chạy Workflow Đầu Tiên

```bash
# Tính VTTH cho 300 khách
/tinh-vtth 300

# So sánh với tồn kho
/so-sanh-kho workspace/inventory-files/ton-kho.xlsx

# Tạo phiếu mua hàng
/tao-phieu
```

---

## 📋 Commands

| Command | Mô Tả |
|---------|-------|
| `/kho` | Menu chính - Hiển thị 3 lựa chọn |
| `/tinh-vtth [số_khách] [gói]` | Tính VTTH |
| `/tinh-hoa-chat [số_khách] [gói]` | Tính Hóa Chất (bao gồm QC/CALIB) |
| `/so-sanh-kho [file_path]` | So sánh với file tồn kho |
| `/tao-phieu` | Tạo phiếu mua hàng tự động |
| `/youtube [url]` | Trích xuất transcript YouTube |

---

## 🤖 Agents

| Agent | Vai Trò |
|-------|---------|
| **calculator** | Tính VTTH & Hóa Chất |
| **inventory-manager** | So sánh tồn kho |
| **purchase-order-creator** | Tạo phiếu mua hàng |
| **research** | Tra cứu & hỗ trợ |

---

## 📊 Google Sheets

**Spreadsheet ID**: `1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800`

### Sheets Sử Dụng:

| Sheet | Mục Đích |
|-------|----------|
| **VTTH** | Dữ liệu vật tư tiêu hao |
| **Hoa Chat Chi Tiet** | ⭐ SHEET CHÍNH - Lọc danh sách HC |
| **Hoa Chat** | ⭐ SHEET PHỤ - Tra cứu QC/CALIB |
| **Phiếu Mua Hàng** | Metadata các phiếu |
| **Chi Tiết Phiếu Mua Hàng** | Chi tiết từng phiếu |
| **Phiếu mua hàng mẫu version 1** | ⭐ TEMPLATE |

---

## 🔴 Quy Tắc Quan Trọng

### ⚠️ QUY TẮC #1: So Sánh Tồn Kho
**LUÔN so sánh bằng đơn vị nhỏ nhất (lọ, miếng, ml)**

```python
# ✅ ĐÚNG
ton_kho_nho = ton_kho_lon × ty_le_quy_doi
can_mua_nho = nhu_cau_nho - ton_kho_nho

# ❌ SAI
# can_mua_lon = can_lon - ton_kho_lon
```

### ⚠️ QUY TẮC #2: Phiếu Mua Hàng
**LUÔN dùng đơn vị lớn (Hộp, Chai, Thùng) + ROUNDUP**

```python
# ✅ ĐÚNG
can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi)

# ❌ SAI
# can_mua_lon = round(can_mua_nho / ty_le_quy_doi)
```

### ⚠️ QUY TẮC #3: Tính Hóa Chất
**LUÔN lọc từ sheet "Hoa Chat Chi Tiet", KHÔNG phải "Hoa Chat"**

---

## 📁 Cấu Trúc Dự Án

```
BO_KHO_MUA_HANG_THEO_TARGET/
├── .claude/
│   ├── settings.json              # Cấu hình project
│   ├── agents/                    # AI agents
│   │   ├── calculator.md
│   │   ├── inventory-manager.md
│   │   ├── purchase-order-creator.md
│   │   └── research.md
│   └── commands/                  # Slash commands
│       ├── kho.md
│       ├── tinh-vtth.md
│       ├── tinh-hoa-chat.md
│       ├── so-sanh-kho.md
│       ├── tao-phieu.md
│       └── youtube.md
│
├── context/                       # Tài liệu hướng dẫn
│   ├── formulas/                  # Công thức tính
│   ├── google-sheets/             # Hướng dẫn sheets
│   └── workflows/                 # Quy trình
│
├── workspace/                     # Vùng làm việc
│   ├── calculations/              # Kết quả tính toán
│   ├── inventory-files/           # File tồn kho
│   └── purchase-orders/           # Lịch sử phiếu
│
├── tools/                         # Scripts & SOPs
│   ├── scripts/                   # Python scripts
│   ├── SOPs/                      # Hướng dẫn setup
│   └── requirements.txt           # Dependencies
│
├── config/                        # Cấu hình (GITIGNORED)
│   └── service-account-key.json
│
├── CLAUDE.md                      # AI instructions
├── README.md                      # This file
├── USAGE_GUIDE.md                 # Hướng dẫn chi tiết
└── .gitignore
```

---

## 🎓 Tài Liệu

### Bắt Đầu
- [USAGE_GUIDE.md](USAGE_GUIDE.md) - Hướng dẫn sử dụng chi tiết
- [context/workflows/complete-workflow.md](context/workflows/complete-workflow.md) - Quy trình đầy đủ

### Quan Trọng Nhất
⭐ [context/formulas/unit-conversion.md](context/formulas/unit-conversion.md) - **QUY TẮC VÀNG** về quy đổi đơn vị

### Setup
- [tools/SOPs/setup-google-sheets-api.md](tools/SOPs/setup-google-sheets-api.md) - Setup Google Sheets API
- [tools/SOPs/configure-credentials.md](tools/SOPs/configure-credentials.md) - Cấu hình credentials

---

## 🔧 Requirements

### Python 3.12.8+

### Packages
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- pandas
- openpyxl

### Google Cloud
- Google Cloud Project
- Google Sheets API enabled
- Service Account credentials

---

## 🎯 Use Cases

### Hàng Ngày
1. **Tính nhu cầu cho đợt khách mới**
   ```bash
   /tinh-vtth 300
   /tinh-hoa-chat 300
   ```

2. **So sánh và tạo phiếu**
   ```bash
   /so-sanh-kho workspace/inventory-files/ton-kho-latest.xlsx
   # Trả lời "CÓ" khi được hỏi tạo phiếu
   ```

### Định Kỳ
- Cập nhật file tồn kho mới
- Review phiếu mua hàng đã tạo
- Kiểm tra dữ liệu trong Google Sheets

---

## 📊 Gói Dịch Vụ

- **B2B-Gói đồng** (mặc định)
- **B2B-Gói cơ bản**
- **B2B-Gói bạc**

Mỗi gói có danh sách VTTH và Hóa Chất riêng.

---

## 🔒 Bảo Mật

### Files KHÔNG Commit
- `config/service-account-key.json`
- `workspace/calculations/*.json`
- `workspace/inventory-files/*`
- Tất cả file chứa dữ liệu thực

### .gitignore
Đã cấu hình để bảo vệ:
- Credentials
- Dữ liệu làm việc
- File tồn kho

---

## ⚡ Performance

- **Tính VTTH**: < 5 giây
- **Tính Hóa Chất**: < 10 giây
- **So sánh tồn kho**: < 5 giây
- **Tạo phiếu**: < 30 giây

---

## 🐛 Troubleshooting

### Lỗi thường gặp
Xem: [context/workflows/troubleshooting.md](context/workflows/troubleshooting.md)

### Hỗ trợ
- Kiểm tra CLAUDE.md
- Xem context documentation
- Review agent instructions

---

## 📈 Tính Năng Tương Lai

Các tính năng sẽ phát triển sau:
- [ ] Email notifications
- [ ] Dashboard/analytics
- [ ] Multi-user support
- [ ] Automatic backup
- [ ] Low stock alerts

---

## 📝 Version

**Version**: 1.0.0
**Last Updated**: 2025-02-02
**Python**: 3.12.8
**Google Sheets API**: v4

---

## 🙏 Credits

Dự án được tạo bởi **Claude Code Meta-Builder**.

---

**🚀 Sẵn sàng tự động hóa mua hàng cho phòng xét nghiệm!**
