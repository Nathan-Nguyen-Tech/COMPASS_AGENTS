# B2B Customer Dashboard - Generation Guide

Complete guide for generating interactive customer analytics dashboards.

**Version:** 2.1.0
**Last Updated:** November 2025

## 🚀 Quick Start (Recommended)

### Using Claude Code (Easiest Method)

```bash
# Start Claude Code
claude

# Generate dashboard with cached data (5-10 seconds)
/generate-dashboard
```

That's it! The Dashboard Generator agent will handle everything automatically.

### Option 1: Generate with Cached Data (Fast - Recommended)

**Best for:** Daily updates, testing, quick regeneration

```bash
# Navigate to project directory
cd D:\Compass_Coding\COMPASS_AGENTS\b2b-customer-dashboard

# Generate from cached data (5-10 seconds)
python tools/scripts/generate_full_dashboard.py --cache-data

# View the dashboard
python tools/scripts/serve_dashboard.py
```

**What happens:**
- ✅ Uses `workspace/data/real_data.json` (1,687 records)
- ✅ No Google Sheets API calls (fast!)
- ✅ Generates in 5-10 seconds
- ✅ No credentials required

### Option 2: Generate with Fresh Data from Google Sheets

**Best for:** First-time setup, monthly updates, after major data changes

```bash
# Navigate to project directory
cd D:\Compass_Coding\COMPASS_AGENTS\b2b-customer-dashboard

# Set up environment (first time only)
# 1. Copy .env.example to .env
# 2. Update GDRIVE_CREDENTIALS_PATH with your service account key path
# 3. Verify SPREADSHEET_ID is correct

# Fetch fresh data from Google Sheets and generate (20-30 seconds)
python tools/scripts/generate_full_dashboard.py \
  --credentials "path/to/service-account-key.json" \
  --spreadsheet-id "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A"

# Or use environment variables
python tools/scripts/generate_full_dashboard.py
```

**What happens:**
- ✅ Fetches latest data from Google Sheets
- ✅ Saves to `workspace/data/real_data.json` for future use
- ✅ Generates dashboard with fresh data
- ✅ Takes 20-30 seconds
- ✅ Auto-opens dashboard in browser (use `--no-browser` to disable)

## 🎯 Filtering Logic (IMPORTANT - v2.1.0)

### How Dashboard Filters Work

The dashboard filters data based on the **"Est Month to close"** field, which represents the expected month when a deal will close. This is critical for sales pipeline forecasting.

**Filter Field:** `"Est Month to close"`

**Field Format:**
- Format: `"MMM-YYYY"` (e.g., `"Oct-2025"`, `"Nov-2025"`, `"Dec-2025"`)
- Examples: `"Jan-2025"`, `"Feb-2026"`, `"Mar-2025"`
- Invalid values: `"Undefined"`, `"-"`, empty strings (automatically excluded from filtering)

**Filter Behavior:**
- **No filters applied**: Shows all customers with valid "Est Month to close" (~1,687 records)
- **Year filter** (e.g., 2025): Shows all customers expected to close in 2025
- **Year + Month filter** (e.g., 2025 + Oct): Shows customers expected to close in October 2025 (~120 customers)
- **Year + Quarter filter** (e.g., 2025 + Q4): Shows customers expected to close in Q4 2025 (Oct-Dec)

**What Fields Are NOT Used for Filtering:**
- ❌ `Latest Action Date` (last activity date)
- ❌ `Calling Day` (when customer was contacted)
- ❌ `PIPELINE WEEK` (pipeline tracking field)

**Why This Matters:**
- **Correct for:** Sales forecasting, pipeline management, revenue prediction
- **Shows:** When deals are expected to close (future-focused)
- **Not:** When we last contacted customers (historical activity)

**Example Comparison:**
```
Filter: October 2025

Incorrect approach (old):
- Field: Latest Action Date / Calling Day
- Result: 2 customers (who had actions in October)
- Meaning: Shows historical activity

Correct approach (v2.1.0):
- Field: Est Month to close
- Result: ~120 customers (expected to close in October)
- Meaning: Shows pipeline forecast
```

### Client-Side Filtering

**How It Works:**
1. Dashboard embeds complete raw data in HTML
2. JavaScript filters data in real-time (no backend needed)
3. Charts regenerate instantly when filters change
4. All 9 charts update dynamically

**Technical Implementation:**
- Raw data embedded via `{{RAW_DATA}}` placeholder
- JavaScript `parseEstMonthToClose()` function parses "MMM-YYYY" format
- `filterData()` function applies year/month/quarter filters
- Charts regenerate using Plotly.newPlot()

**Benefits:**
- ⚡ Instant filtering (no page reload)
- 🔒 Works offline (no API calls)
- 📊 All charts stay synchronized
- 🎨 Smooth user experience

## Generated Dashboard Features

### Dashboard Components

The generated dashboard includes:

#### Header
- Project title with gradient background
- Last updated timestamp
- Data source information

#### Control Panel
- Dashboard Type selector (Monthly/Quarterly)
- Year filter
- Month/Quarter filter
- Apply Filter button
- Refresh Data button

#### 9 Interactive Charts

1. **Phân bố Quy mô Công ty** (Company Size Distribution)
   - Type: Horizontal bar chart
   - Shows: Customer count by company size
   - Colors: Blue gradient

2. **Trạng thái Khách hàng Top 10** (Client Status Top 10)
   - Type: Horizontal bar chart
   - Shows: Top 10 customer statuses with percentages
   - Colors: Multi-color palette

3. **Phân bố Giá trị Hợp đồng** (Contract Value Distribution)
   - Type: Vertical bar chart
   - Shows: Distribution across value ranges (<50M, 50-100M, etc.)
   - Colors: Green gradient

4. **Phân bố Nguồn Khách hàng Top 8** (Customer Source Top 8)
   - Type: Vertical bar chart
   - Shows: Top 8 acquisition sources + Others
   - Colors: Multi-color palette

5. **Top 10 Quận theo Số lượng** (Top 10 Districts by Count)
   - Type: Horizontal bar chart
   - Shows: Geographic distribution
   - Colors: Orange gradient

6. **Phân bố Ngân sách AHCU** (AHCU Budget Distribution)
   - Type: Vertical bar chart
   - Shows: Budget distribution across ranges
   - Colors: Purple gradient

7. **Lý do Thất bại Deals Top 10** (Failure Reasons Top 10)
   - Type: Horizontal bar chart
   - Shows: Top reasons for lost deals
   - Colors: Red gradient

8. **Xu hướng Doanh thu theo Tháng/Quý** (Revenue Trend)
   - Type: Line chart with markers
   - Shows: Revenue trend over time based on "Est Month to close"
   - Auto-switches between monthly/quarterly view
   - Based on expected close dates, not activity dates

9. **Sales Funnel - Pipeline Overview**
   - Type: Funnel chart
   - Shows: Customer progression through sales stages
   - Colors: Green to red gradient

#### Footer
- Generation timestamp
- Data source reference
- Total records count

### Interactive Features

All charts include:
- Hover tooltips with detailed information
- Zoom and pan capabilities
- Download as PNG option
- Responsive design (desktop, tablet, mobile)
- Auto-resize on window changes

## Command Reference

### Generate Dashboard from Sample Data

```bash
# Basic generation (no filters)
python tools/scripts/dashboard_generator.py --data workspace/data/sample_data.json

# Monthly dashboard for specific year and month
python tools/scripts/dashboard_generator.py \
  --data workspace/data/sample_data.json \
  --type monthly \
  --year 2025 \
  --month 6

# Quarterly dashboard
python tools/scripts/dashboard_generator.py \
  --data workspace/data/sample_data.json \
  --type quarterly \
  --year 2025 \
  --quarter 2

# Custom output path
python tools/scripts/dashboard_generator.py \
  --data workspace/data/sample_data.json \
  --output workspace/dashboards/generated/custom_dashboard.html
```

### Fetch Data from Google Sheets

```bash
# Fetch data and save to JSON
python tools/scripts/fetch_sheets_data.py \
  --credentials "path/to/credentials.json" \
  --spreadsheet-id "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A" \
  --output workspace/data/latest_data.json

# Then generate dashboard from fetched data
python tools/scripts/dashboard_generator.py --data workspace/data/latest_data.json
```

### Full Generation (Fetch + Generate)

```bash
# Basic - uses environment variables (fetches fresh data)
python tools/scripts/generate_full_dashboard.py

# With explicit credentials
python tools/scripts/generate_full_dashboard.py \
  --credentials "path/to/credentials.json" \
  --spreadsheet-id "YOUR_SPREADSHEET_ID"

# With filters (and fresh data fetch)
python tools/scripts/generate_full_dashboard.py \
  --type monthly \
  --year 2025 \
  --month 6

# ⚡ WITH CACHED DATA (FASTEST - Recommended for daily use)
python tools/scripts/generate_full_dashboard.py --cache-data

# Cached data with filters (5-10 seconds)
python tools/scripts/generate_full_dashboard.py \
  --cache-data \
  --type monthly \
  --year 2025 \
  --month 6

# Disable auto-open browser (NEW in v2.1.0)
python tools/scripts/generate_full_dashboard.py --cache-data --no-browser
```

**⚡ Cache Data Feature (v2.0.0):**
- Uses `workspace/data/real_data.json` (standard cache location)
- No Google Sheets API calls = 3-5x faster
- Perfect for daily updates and quick iterations
- Credentials NOT required when using cache
- Data stays fresh for your daily needs

**🚀 Auto-Open Feature (NEW in v2.1.0):**
- Dashboard automatically opens in browser after generation
- No need to manually open HTML file
- Use `--no-browser` flag to disable if needed
- Improves workflow efficiency

### Serve Dashboard Locally

```bash
# Serve latest dashboard (auto-opens browser)
python tools/scripts/serve_dashboard.py

# Serve on custom port
python tools/scripts/serve_dashboard.py --port 8080

# Serve specific dashboard
python tools/scripts/serve_dashboard.py \
  --dashboard workspace/dashboards/generated/dashboard_20251104_102519.html

# Don't auto-open browser
python tools/scripts/serve_dashboard.py --no-browser
```

## File Locations

### Generated Dashboards
```
workspace/dashboards/generated/
├── dashboard_20251104_102519.html  (timestamped)
├── dashboard_20251104_103045.html
└── dashboard.html                  (latest)
```

### Data Files
```
workspace/data/
├── sample_data.json              (demo data - 8 records)
├── real_data.json                (🔥 STANDARD CACHE - 1,687 records from Google Sheets)
└── latest_data.json              (manual fetch - optional)
```

**Note:** `real_data.json` is the standard cache location used by `--cache-data` flag.

### Scripts
```
tools/scripts/
├── dashboard_generator.py        (core generator)
├── data_processor.py             (data processing)
├── chart_builder.py              (chart creation)
├── fetch_sheets_data.py          (Google Sheets fetcher)
├── generate_full_dashboard.py    (full workflow)
└── serve_dashboard.py            (local server)
```

## Dashboard Summary Statistics

### From Latest Generation (Sample Data)

```
Total Customers: 8
Total Contract Value: 2,095 M VND
Average Contract Value: 262 M VND
Total AHCU Budget: 51,500,000 VND

Dashboard Type: Monthly
Filters: None (showing all data)
```

### Chart Data Breakdown

1. **Company Size Distribution**: 4 categories
2. **Client Status**: 7 unique statuses
3. **Contract Values**: 6 value ranges
4. **Customer Sources**: 8 sources
5. **Districts**: 8 districts
6. **AHCU Budget**: 6 budget ranges
7. **Failure Reasons**: 2 reasons recorded
8. **Revenue Trend**: 4 time periods
9. **Sales Funnel**: 6 sales stages

## Troubleshooting

### Issue: "Credentials path not provided"

**Solution:**
```bash
# Option 1: Create .env file
cp .env.example .env
# Edit .env and set GDRIVE_CREDENTIALS_PATH

# Option 2: Pass credentials explicitly
python tools/scripts/generate_full_dashboard.py \
  --credentials "path/to/credentials.json" \
  --spreadsheet-id "YOUR_SPREADSHEET_ID"
```

### Issue: "Invalid JWT Signature"

**Cause:** Service account credentials are invalid or expired

**Solution:**
1. Verify service account key file is correct
2. Check service account has access to the spreadsheet
3. Ensure spreadsheet is shared with service account email
4. Regenerate service account key if needed

### Issue: "No data found in spreadsheet"

**Solution:**
1. Verify spreadsheet ID is correct
2. Check sheet name (default: first sheet)
3. Ensure spreadsheet is not empty
4. Verify service account has read access

### Issue: "Port already in use"

**Solution:**
```bash
# Try a different port
python tools/scripts/serve_dashboard.py --port 8001

# Or find and kill the process using port 8000
# Windows: netstat -ano | findstr :8000
# Linux/Mac: lsof -ti:8000 | xargs kill
```

### Issue: "Charts not rendering"

**Solution:**
1. Check browser console for JavaScript errors
2. Ensure internet connection (for CDN resources)
3. Try different browser (Chrome, Firefox, Edge recommended)
4. Clear browser cache
5. Verify Plotly.js loaded correctly

## Advanced Usage

### Custom Data Processing

To modify how data is processed:

1. Edit `tools/scripts/data_processor.py`
2. Update field mappings in `FIELD_MAPPING`
3. Modify filtering logic in `_apply_filters()`
4. Add custom metrics in `calculate_metrics()`

### Custom Chart Styling

To customize chart appearance:

1. Edit `tools/scripts/chart_builder.py`
2. Modify color palettes in `COLORS`
3. Update chart configurations in individual chart methods
4. Change Plotly layout options

### Custom Dashboard Template

To modify dashboard layout:

1. Edit `tools/templates/dashboard_template.html`
2. Update CSS styles
3. Change grid layout
4. Add/remove chart containers
5. Modify JavaScript behavior

## Integration with MCP

### Current MCP Configuration

The project is configured to use:

1. **MCP server-gdrive**: Google Drive/Sheets access
2. **MCP server-filesystem**: Local file operations

### Using MCP Tools Directly

When MCP tools are available (in Claude Code sessions):

```javascript
// Read Google Sheets data
gdrive_read_file({
  fileId: "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A"
})

// Write dashboard file
write_file({
  path: "workspace/dashboards/generated/dashboard.html",
  content: dashboardHTML
})
```

## ⚡ Performance Optimization

### Cache Data Workflow (RECOMMENDED)

The `--cache-data` flag is your best friend for fast dashboard generation!

**Initial Setup (First Time Only):**
```bash
# Step 1: Fetch fresh data from Google Sheets (requires credentials)
python tools/scripts/generate_full_dashboard.py

# This saves data to: workspace/data/real_data.json
# Time: ~20-30 seconds
```

**Daily Usage (Fast):**
```bash
# Step 2: Use cached data for subsequent generations
python tools/scripts/generate_full_dashboard.py --cache-data

# This uses: workspace/data/real_data.json
# Time: ~5-10 seconds (3-5x faster!)
# No credentials required!
```

**When to Refresh Cache:**
- Weekly/monthly (depends on data change frequency)
- After major data updates in Google Sheets
- When you need absolute latest data
- Before important presentations

**Performance Comparison:**
| Method | Time | Credentials Required | API Calls |
|--------|------|---------------------|-----------|
| Fresh fetch | 20-30s | ✅ Yes | Yes (slow) |
| Cached data (`--cache-data`) | 5-10s | ❌ No | None (fast!) |
| Sample data | 3-5s | ❌ No | None |

### Cache Location

**Standard Cache File:** `workspace/data/real_data.json`
- Size: ~2.9 MB
- Records: 1,687 customers (from Google Sheets)
- Updated: When you run without `--cache-data` flag
- Format: JSON array of customer objects

### Large Datasets

For spreadsheets with >1000 rows:

1. ✅ **Always use `--cache-data`** for daily work
2. ✅ Use filters to reduce dataset size
3. ✅ Refresh cache weekly/monthly only
4. ✅ Consider archiving old data in separate sheet
5. ⚠️ Avoid fetching fresh data multiple times per day

## Next Steps

### To Generate Dashboard from Real Google Sheets:

1. **Verify Service Account Setup**
   ```bash
   # Check credentials file exists
   ls -la "D:\Compass_Coding\COMPASS_AGENTS\claude-code-meta-builder\config\service-account-key.json"
   ```

2. **Verify Spreadsheet Access**
   - Open Google Sheets
   - Share spreadsheet with service account email
   - Give "Viewer" permission

3. **Update Service Account Key** (if JWT error persists)
   - Go to Google Cloud Console
   - Navigate to IAM & Admin > Service Accounts
   - Create new key or use existing
   - Download JSON key
   - Update path in .env file

4. **Run Full Generation**
   ```bash
   python tools/scripts/generate_full_dashboard.py \
     --credentials "D:\Compass_Coding\COMPASS_AGENTS\claude-code-meta-builder\config\service-account-key.json" \
     --spreadsheet-id "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A"
   ```

### To View Current Dashboard:

1. **Direct File Access**
   ```
   File path: D:\Compass_Coding\COMPASS_AGENTS\b2b-customer-dashboard\workspace\dashboards\generated\dashboard_20251104_102519.html

   Browser URL: file:///D:/Compass_Coding/COMPASS_AGENTS/b2b-customer-dashboard/workspace/dashboards/generated/dashboard_20251104_102519.html
   ```

2. **Via Local Server**
   ```bash
   python tools/scripts/serve_dashboard.py
   # Opens http://localhost:8000/dashboard_20251104_102519.html
   ```

## Support

For issues or questions:

1. Check this guide's Troubleshooting section
2. Review `tools/mcp-documentation/` for MCP-specific issues
3. Check Python script error messages
4. Verify all dependencies installed: `pip install -r requirements.txt`

---

**Dashboard Generated:** 2025-11-04 10:25:19
**Data Source:** Sample data (8 records)
**Status:** Successfully generated with all 9 charts
