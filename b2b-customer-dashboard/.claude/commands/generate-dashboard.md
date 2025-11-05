# Generate Dashboard Command

Generate a complete interactive web dashboard from Google Sheets data with all 9 charts and Vietnamese currency support.

## Usage

```bash
/generate-dashboard
```

This will activate the Dashboard Generator agent and execute the full workflow.

## What This Command Does

### 1. Activates Dashboard Generator Agent
Switches to the specialized Dashboard Generator agent (version 2.1.0) which will:

### 2. Execute Full Dashboard Generation
Runs the optimized Python script:
```bash
python tools/scripts/generate_full_dashboard.py --cache-data
```

This single command will:
- ✅ Use cached data from `workspace/data/real_data.json` (1,687 records)
- ✅ Process data with Vietnamese currency format handling
- ✅ Generate all 9 interactive charts
- ✅ Create HTML dashboard with client-side filters (instant, no reload)
- ✅ Save to `workspace/dashboards/generated/dashboard.html`
- ✅ Auto-open dashboard in browser (NEW in v2.1.0)

### 3. Dashboard Output

**Generated File:**
- Location: `workspace/dashboards/generated/dashboard.html`
- Size: ~23KB
- Records: 1,632 customers (after filtering)
- Charts: All 9 charts with real data

**Key Metrics:**
- Total Contract Value: ~64,127 M VND
- Average Contract Value: ~66 M VND
- Total AHCU Budget: ~965,785,100 VND
- Sales Funnel: All 6 stages displayed correctly

## The 9 Interactive Charts

All charts are generated with real data from Google Sheets:

1. ✅ **Phân bố Quy mô Công ty** (Company Size Distribution) - Horizontal Bar
2. ✅ **Trạng thái Khách hàng Top 10** (Client Status Top 10) - Horizontal Bar
3. ✅ **Phân bố Giá trị Hợp đồng** (Contract Value Distribution) - Vertical Bar
   - Bins: 0-50M, 50-100M, 100-200M, 200-500M, 500M+
4. ✅ **Phân bố Nguồn Khách hàng Top 8** (Customer Source Top 8) - Vertical Bar
5. ✅ **Top 10 Quận theo Số lượng** (Top 10 Districts) - Horizontal Bar
6. ✅ **Phân bố Ngân sách AHCU** (AHCU Budget Distribution) - Vertical Bar
   - Bins: 0-2M, 2M-5M, 5M-10M, 10M+
7. ✅ **Lý do Thất bại Deals Top 10** (Failure Reasons Top 10) - Horizontal Bar
8. ✅ **Xu hướng Doanh thu theo Tháng/Quý** (Revenue Trend) - Line Chart
9. ✅ **Sales Funnel - Pipeline Overview** (Sales Pipeline) - Funnel Chart
   - All 6 stages: Prospecting → Proposal → Meeting/Tour → Negotiation → Verbal Confirm → Closed

## Dashboard Features

- ✅ Responsive design (desktop, tablet, mobile)
- ✅ Interactive filters (year, month/quarter, dashboard type)
- ✅ Hover tooltips on all charts
- ✅ Zoom and pan capabilities
- ✅ Download charts as PNG
- ✅ Vietnamese labels and currency format
- ✅ Refresh button to update data

## How to View Dashboard

After generation, the agent will provide:

**Direct Open:**
```bash
start workspace\dashboards\generated\dashboard.html
```

**Or view in browser:**
```
file:///D:/Compass_Coding/COMPASS_AGENTS/b2b-customer-dashboard/workspace/dashboards/generated/dashboard.html
```

**Or start web server:**
```bash
python tools/scripts/serve_dashboard.py
# Then open: http://localhost:8000/dashboard.html
```

## Data Source

**Google Sheets:**
- Spreadsheet ID: `1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A`
- Sheet Name: **"Data"**
- Total Records: ~1,687 customers
- Fields: 43 columns

**Cached Data:**
- Location: `workspace/data/real_data.json`
- Size: 2.9MB
- Updated: When you run with fresh data fetch

## Advanced Usage

### Generate with Fresh Data (Fetch from Google Sheets)

If you need the absolute latest data:

**Note:** The agent will guide you through this if needed, but the command is:
```bash
python tools/scripts/generate_full_dashboard.py
```

This will:
1. Fetch latest data from Google Sheets (requires service account credentials)
2. Save to `workspace/data/real_data.json`
3. Generate dashboard with new data

### Generate with Filters

**Monthly View - Specific Month:**
You can ask the agent: "Generate dashboard for June 2025"

**Quarterly View - Specific Quarter:**
You can ask the agent: "Generate quarterly dashboard for Q2 2025"

The agent will execute:
```bash
# Monthly
python tools/scripts/generate_full_dashboard.py --cache-data --year 2025 --month 6

# Quarterly
python tools/scripts/generate_full_dashboard.py --cache-data --type quarterly --year 2025 --quarter 2
```

## Technical Implementation

**Workflow:**
```
Cached Data (real_data.json)
    ↓
Python Data Processor (Vietnamese currency handling)
    ↓
Chart Builder (9 Plotly.js charts)
    ↓
HTML Dashboard (Bootstrap 5 + Plotly.js)
    ↓
workspace/dashboards/generated/dashboard.html
```

**Technologies:**
- Python 3.12
- Plotly.js (interactive charts)
- Bootstrap 5 (responsive UI)
- Google Sheets API (data source)

**Performance:**
- Generation time: 5-15 seconds (using cached data)
- Dashboard load time: 1-3 seconds
- Supports: 10,000+ records

## Troubleshooting

### "No cached data found"
**Solution:** Ask agent to fetch fresh data first:
```bash
python tools/scripts/fetch_sheets_data.py \
  --spreadsheet-id "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A" \
  --sheet-name "Data" \
  --output "workspace/data/real_data.json"
```

### "Contract values showing as 0"
**Solution:** This is already fixed! The system handles Vietnamese currency:
- `"1,750,000,000 ₫"` → 1,750 Million VND ✅

### "Sales Funnel missing stages"
**Solution:** This is already fixed! All 6 stages display correctly ✅

### "Dashboard not opening"
**Solution:**
1. Check file exists: `workspace/dashboards/generated/dashboard.html`
2. Try: `start workspace\dashboards\generated\dashboard.html`
3. Or copy full path to browser address bar

## Configuration Required

**Environment Variables (.env):**
```bash
GDRIVE_CREDENTIALS_PATH=path/to/service-account-key.json
SPREADSHEET_ID=1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A
SPREADSHEET_NAME=Data
```

**Note:** If using cached data (`--cache-data`), credentials are NOT required!

## Success Criteria

After running `/generate-dashboard`, you should see:

✅ Dashboard Generator agent activated
✅ "Loaded 1687 records" message
✅ "1632 records after filtering"
✅ All 9 charts generated successfully
✅ "Dashboard generated successfully!" message
✅ File path provided: `workspace/dashboards/generated/dashboard.html`
✅ Dashboard opens in browser showing all charts
✅ Sales Funnel shows 6 stages: 1365 → 171 → 47 → 4 → 7 → 38 customers
✅ Contract values in Million VND (not billions)
✅ Vietnamese labels display correctly

## Related Commands

- Use `/refresh-data` to fetch latest data from Google Sheets and regenerate
- Open dashboard directly: `start workspace\dashboards\generated\dashboard.html`

---

**Ready to generate? Just run:**
```bash
/generate-dashboard
```

The Dashboard Generator agent will handle everything automatically! 🚀
