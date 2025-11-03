# COMPASS AGENTS - Demo & Tutorial

## 🎬 Demo Video Workflow

### Cách 1: Interactive Mode (KHUYẾN NGHỊ - DỄ NHẤT)

```bash
# Bước 1: Chạy list
python compass.py list
```

**Output:**
```
===============================================================
         COMPASS AGENTS - Agent Management CLI
===============================================================

[*] Danh sach Agents:

1. Hệ Thống Tự Động Mua Hàng - Phòng Xét Nghiệm
   ID: BO_KHO_MUA_HANG_THEO_TARGET
   Mô tả: Hệ thống tự động tính toán nhu cầu mua hàng...
   Đường dẫn: BO_KHO_MUA_HANG_THEO_TARGET

2. Claude Code Meta-Builder
   ID: claude-code-meta-builder
   Mô tả: A comprehensive system for creating and optimizing...
   Đường dẫn: claude-code-meta-builder

3. Tech Learning Assistant
   ID: tech-learning-assistant
   Mô tả: Your AI-powered system for mastering new technologies...
   Đường dẫn: tech-learning-assistant

============================================================
Chon agent de chay (nhap so 1-3, hoac Enter de thoat):
```

**Bạn nhập:** `1`

**Kết quả:**
```
[+] Chay Agent: Hệ Thống Tự Động Mua Hàng - Phòng Xét Nghiệm
Thu muc: D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET

[*] Cac cach su dung agent:

1. Mo terminal moi (tu dong):
   - Terminal moi se mo tai thu muc agent
   - Ban co the chay 'claude' hoac lam viec voi agent

2. Trong terminal hien tai:
   cd "D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET"
   claude

============================================================
Ban muon mo terminal moi? (y/n, mac dinh: y):
```

**Bạn nhập:** `y` hoặc Enter

**Kết quả:** Terminal mới sẽ mở tại thư mục agent, sẵn sàng để chạy `claude`!

---

### Cách 2: Direct Run (Nhanh cho user biết ID)

```bash
python compass.py run tech-learning-assistant
```

**Kết quả tương tự như trên, nhưng bỏ qua bước chọn từ list**

---

### Cách 3: Quick Open (Không hỏi, mở ngay)

```bash
python compass.py open claude-code-meta-builder
```

**Kết quả:** Terminal mới mở ngay lập tức tại thư mục agent (không hỏi)

---

## 📝 Các Lệnh Khác

### Quét agents
```bash
python compass.py scan
```

### Xem thông tin chi tiết
```bash
python compass.py info BO_KHO_MUA_HANG_THEO_TARGET
```

### Lấy lệnh cd
```bash
python compass.py cd tech-learning-assistant
```

---

## 🎯 Use Case Thực Tế

### Scenario 1: Người dùng mới, chưa biết có agents gì

```bash
# Bước 1: Quét
python compass.py scan

# Bước 2: Xem danh sách và chọn
python compass.py list
# Nhập 1, 2, hoặc 3 để chọn agent

# Terminal mới mở, sẵn sàng làm việc!
```

**Thời gian:** ~10 giây

---

### Scenario 2: Người dùng đã biết ID agent

```bash
# Chạy trực tiếp
python compass.py run BO_KHO_MUA_HANG_THEO_TARGET

# Nhấn y hoặc Enter
# Terminal mở, bắt đầu làm việc!
```

**Thời gian:** ~5 giây

---

### Scenario 3: Người dùng cần xem chi tiết trước khi quyết định

```bash
# Xem chi tiết
python compass.py info tech-learning-assistant

# Quyết định chạy
python compass.py run tech-learning-assistant
```

**Thời gian:** ~15 giây

---

### Scenario 4: Power user - Setup PATH

```bash
# Sau khi setup PATH (chỉ làm 1 lần)
compass list
# Chọn số
# Xong!
```

**Thời gian:** ~3 giây

---

## 🚀 Tips & Tricks

### Tip 1: Dùng Interactive Mode cho lần đầu
```bash
python compass.py list
# Dễ nhất, không cần nhớ ID
```

### Tip 2: Dùng Direct Run khi đã biết agent
```bash
python compass.py run <agent-id>
# Nhanh nhất khi đã biết tên agent
```

### Tip 3: Setup PATH để tiện hơn
```bash
# Windows
setx PATH "%PATH%;D:\Compass_Coding\COMPASS_AGENTS"

# Sau đó chỉ cần:
compass list
compass run tech-learning-assistant
```

### Tip 4: Dùng Tab completion (nếu shell hỗ trợ)
```bash
compass <TAB>  # Xem các lệnh có sẵn
```

---

## 📊 So Sánh Các Cách

| Cách | Thời gian | Độ khó | Khi nào dùng |
|------|-----------|---------|--------------|
| **compass list** → chọn số | ~10s | ⭐ Rất dễ | Lần đầu, không biết ID |
| **compass run <id>** | ~5s | ⭐⭐ Dễ | Đã biết ID agent |
| **compass open <id>** | ~3s | ⭐⭐ Dễ | Muốn mở nhanh, không cần hỏi |
| **compass cd <id>** → copy → paste | ~8s | ⭐⭐⭐ Trung bình | Muốn cd trong terminal hiện tại |

---

## 🎓 Training Script cho User Mới

### Bước 1: Làm quen với CLI
```bash
python compass.py help
```

### Bước 2: Quét agents
```bash
python compass.py scan
```

### Bước 3: Khám phá từng agent
```bash
python compass.py info BO_KHO_MUA_HANG_THEO_TARGET
python compass.py info tech-learning-assistant
python compass.py info claude-code-meta-builder
```

### Bước 4: Chạy agent đầu tiên
```bash
python compass.py list
# Chọn số 1
# Nhấn y
# Làm việc với agent!
```

### Bước 5: Lần sau đơn giản hơn
```bash
python compass.py run tech-learning-assistant
```

---

## ❓ FAQ

### Q: Tôi có cần biết ID agent không?
**A:** Không! Dùng `compass list` và chọn số. Dễ nhất!

### Q: Làm sao để chạy nhanh nhất?
**A:** Setup PATH, sau đó `compass list` → chọn số → Enter. ~3 giây!

### Q: Tôi muốn cd trong terminal hiện tại?
**A:** `compass cd <agent-id>` → copy lệnh → paste

### Q: Khác gì giữa `run` và `open`?
**A:**
- `run`: Hỏi trước khi mở terminal, hiển thị hướng dẫn đầy đủ
- `open`: Mở terminal ngay lập tức, không hỏi

### Q: Tôi thêm agent mới, phải làm gì?
**A:** Chỉ cần `compass scan` để cập nhật danh sách!

---

## 🎉 Kết Luận

COMPASS AGENTS CLI giúp bạn:
- ✅ **Quản lý nhiều agents** từ 1 nơi
- ✅ **Chọn và chạy nhanh** chỉ với 2-3 clicks
- ✅ **Không cần nhớ đường dẫn** phức tạp
- ✅ **Interactive mode** rất dễ dùng
- ✅ **Cross-platform** Windows/Linux/Mac

**Bắt đầu ngay:** `python compass.py list` 🚀
