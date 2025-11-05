# B2B Customer Dashboard - Quick Start Guide

**Version 2.0.0** | November 2025

## 🎉 What's New in v2.0.0

- ⚡ **Cache Data Feature** - Generate dashboards 3-5x faster với `--cache-data`
- 📍 **Standardized Cache** - Dùng `real_data.json` làm standard cache location
- 💰 **Fixed Currency** - Vietnamese currency format hoạt động hoàn hảo
- 📊 **Fixed Sales Funnel** - Tất cả 6 stages hiển thị đúng
- 🚀 **Optimized Workflow** - Workflow mới nhanh và hiệu quả hơn

---

## ⚡ TL;DR - Chạy Ngay

```bash
/generate-dashboard
```

Xong! Dashboard sẽ được tạo tự động với tất cả 9 charts từ cached data (5-10 giây).

---

## 📋 Chi Tiết

### Bước 1: Chạy Command

```bash
/generate-dashboard
```

### Bước 2: Đợi Agent Xử Lý

Agent sẽ tự động:
- ✅ Load 1,687 records từ cached data
- ✅ Process Vietnamese currency format
- ✅ Generate 9 interactive charts
- ✅ Create HTML dashboard
- ✅ Save to `workspace/dashboards/generated/dashboard.html`

### Bước 3: Xem Dashboard

Agent sẽ tự động mở, hoặc bạn có thể:

```bash
start workspace\dashboards\generated\dashboard.html
```

---

## 🎯 Dashboard Bao Gồm

### 9 Charts Được Generate:

1. **Phân bố Quy mô Công ty** - Horizontal bar
2. **Trạng thái Khách hàng Top 10** - Horizontal bar
3. **Phân bố Giá trị Hợp đồng** - Vertical bar (0-50M, 50-100M, 100-200M, 200-500M, 500M+)
4. **Phân bố Nguồn Khách hàng Top 8** - Vertical bar
5. **Top 10 Quận theo Số lượng** - Horizontal bar
6. **Phân bố Ngân sách AHCU** - Vertical bar (0-2M, 2M-5M, 5M-10M, 10M+)
7. **Lý do Thất bại Deals Top 10** - Horizontal bar
8. **Xu hướng Doanh thu theo Tháng/Quý** - Line chart
9. **Sales Funnel - Pipeline Overview** - Funnel (6 stages)

### Metrics Hiển Thị:

- Total Customers: ~1,632
- Total Contract Value: ~64,127 M VND
- Average Contract Value: ~66 M VND
- Total AHCU Budget: ~965,785,100 VND

### Sales Funnel Breakdown:

```
1. Prospecting (10%)      → 1,365 customers (83.6%)
2. Proposal (30%)         →   171 customers (10.5%)
3. Meeting/Tour (50%)     →    47 customers (2.9%)
4. Negotiation (70%)      →     4 customers (0.2%)
5. Verbal Confirm (90%)   →     7 customers (0.4%)
6. Closed (100%)          →    38 customers (2.3%)
```

---

## 🔄 Use Cases Khác

### Refresh Data Mới Nhất

Nếu muốn fetch data mới nhất từ Google Sheets:

```bash
/refresh-data
```

Hoặc tự chạy:

```bash
python tools/scripts/generate_full_dashboard.py
```

### Generate Với Filters

**Monthly View - Tháng 6/2025:**
```bash
/generate-dashboard --year 2025 --month 6
```

**Quarterly View - Q2 2025:**
```bash
/generate-dashboard --type quarterly --year 2025 --quarter 2
```

---

## 💡 Tips

### ⚡ Cache Data Workflow (NEW in v2.0.0)

**Recommended workflow cho tốc độ tối ưu:**

#### Lần Đầu Setup (Chỉ 1 lần):

```bash
# Fetch fresh data từ Google Sheets
python tools/scripts/generate_full_dashboard.py

# Lưu vào: workspace/data/real_data.json
# Thời gian: ~20-30 giây
# Cần: Credentials
```

#### Hàng Ngày (Nhanh):

```bash
# Dùng cached data (RECOMMENDED!)
python tools/scripts/generate_full_dashboard.py --cache-data

# Đọc từ: workspace/data/real_data.json
# Thời gian: ~5-10 giây (3-5x nhanh hơn!)
# KHÔNG cần: Credentials
```

#### Khi Nào Refresh Cache:

- ✅ Hàng tuần/tháng (tùy tần suất data thay đổi)
- ✅ Sau khi có major data updates trong Google Sheets
- ✅ Trước presentation quan trọng
- ✅ Khi cần data hoàn toàn mới nhất

**So Sánh Performance:**

| Method | Thời Gian | Credentials | API Calls |
|--------|-----------|-------------|-----------|
| Fresh fetch | 20-30s | ✅ Cần | Có (chậm) |
| `--cache-data` | 5-10s | ❌ Không cần | Không (nhanh!) |

**Best Practice:**
- Fetch fresh: 1 lần/tuần hoặc 1 lần/tháng
- Dùng cache: Mọi lần generate khác
- Kết quả: Nhanh + Data luôn fresh!

### Open Dashboard Nhanh

```bash
# Windows
start workspace\dashboards\generated\dashboard.html

# Hoặc start web server
python tools/scripts/serve_dashboard.py
# Mở: http://localhost:8000/dashboard.html
```

---

## ❓ Troubleshooting

### "No cached data found"

**Giải pháp:** Fetch data từ Google Sheets trước:

```bash
python tools/scripts/fetch_sheets_data.py \
  --spreadsheet-id "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A" \
  --sheet-name "Data" \
  --output "workspace/data/real_data.json"
```

### Dashboard không mở được

**Giải pháp:**
1. Check file tồn tại: `workspace/dashboards/generated/dashboard.html`
2. Copy full path và paste vào browser

### Credentials error

**Giải pháp:**

Nếu dùng cached data (`--cache-data`), KHÔNG cần credentials!

Nếu cần fetch fresh data, check `.env` file:

```bash
GDRIVE_CREDENTIALS_PATH=path/to/service-account-key.json
SPREADSHEET_ID=1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A
SPREADSHEET_NAME=Data
```

---

## 📂 File Structure

Sau khi chạy `/generate-dashboard`:

```
workspace/
├── dashboards/generated/
│   └── dashboard.html          ← Dashboard file (23KB)
└── data/
    └── real_data.json          ← Cached data (2.9MB, 1,687 records)
```

---

## ✅ Success Checklist

Sau khi chạy command, bạn sẽ thấy:

- ✅ "Dashboard Generator agent activated"
- ✅ "Loaded 1687 records"
- ✅ "1632 records after filtering"
- ✅ "All 9 charts generated"
- ✅ "Dashboard generated successfully!"
- ✅ File path: `workspace/dashboards/generated/dashboard.html`
- ✅ Dashboard mở được trong browser
- ✅ Tất cả 9 charts hiển thị đúng
- ✅ Sales Funnel có 6 stages
- ✅ Contract values đúng format (Million VND)
- ✅ Vietnamese labels hiển thị đúng

---

## 🚀 That's It!

Chỉ cần chạy:

```bash
/generate-dashboard
```

Dashboard Generator agent sẽ tự động handle mọi thứ! 🎉

---

**Need help?** Check:
- `CLAUDE.md` - Full project documentation
- `.claude/agents/dashboard-generator.md` - Agent instructions
- `.claude/commands/generate-dashboard.md` - Command details
