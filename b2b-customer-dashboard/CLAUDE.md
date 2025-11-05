# B2B Customer Dashboard - Project Context

You are working in the B2B Customer Dashboard project, a specialized system for analyzing potential customer data from Google Sheets and generating interactive web dashboards.

## Project Overview

**Purpose:** Generate and maintain interactive analytics dashboards for B2B potential customer pipeline management

**Data Source:** Google Sheets spreadsheet
- Spreadsheet ID: `1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A`
- Sheet Name: **"Data"**
- Total Records: ~1,687 customers
- Fields: 43 columns including Sales Stage, Contract Value, AHCU Budget, etc.

**Output:** Interactive HTML dashboards with 9 charts and comprehensive metrics

**Technology Stack:**
- **Data Access:** Google Sheets API (via service account)
- **Data Processing:** Python (custom processors for Vietnamese currency format)
- **Visualization:** Plotly.js (interactive charts)
- **UI Framework:** Bootstrap 5 (responsive design)
- **Client-Side Filtering:** JavaScript (instant updates, no reload)
- **File Operations:** Local filesystem

**Current Version:** v2.1.0
- ✅ Client-side filtering (instant, no page reload)
- ✅ Auto-open dashboard in browser
- ✅ Filter by "Est Month to close" (pipeline forecast)
- ✅ Cached data mode (5-10s generation)

## Your Primary Functions

### 1. Dashboard Generation
Generate complete interactive dashboards from Google Sheets data:
- Use `/generate-dashboard` command
- Support monthly and quarterly views
- Apply filters (year, month, quarter)
- Create 9 interactive charts
- Save to workspace/dashboards/generated/

### 2. Data Refresh
Update existing dashboards with latest data:
- Use `/refresh-data` command
- Preserve current filters
- Show what changed
- Quick update workflow

### 3. Metrics Analysis
Deep-dive analysis on specific metrics:
- Use `/analyze-metrics` command
- Support various metrics (contract value, conversion rate, etc.)
- Time-based comparisons
- Segment analysis

### 4. Research & Support
Help users understand the system:
- Explain data fields and metrics
- Troubleshoot issues
- Suggest optimizations
- Answer questions about dashboards

## Available Agents

### Dashboard Generator (.claude/agents/dashboard-generator.md)
**Use for:** Generating and refreshing dashboards
- Fetches data from Google Sheets via MCP
- Processes and filters data
- Generates 9 interactive charts
- Creates HTML dashboard files
- Starts local web server

### Data Analyzer (.claude/agents/data-analyzer.md)
**Use for:** Analyzing metrics and generating insights
- Calculates business metrics
- Performs trend analysis
- Identifies patterns and anomalies
- Generates analysis reports

### Chart Builder (.claude/agents/chart-builder.md)
**Use for:** Creating specific visualizations
- Designs Plotly.js charts
- Applies consistent styling
- Implements interactive features
- Handles responsive design

### Research (.claude/agents/research.md)
**Use for:** Gathering information and finding solutions
- Technical research
- Best practices
- Problem solving
- Documentation search

## Available Commands

### /generate-dashboard
Generate complete interactive dashboard from Google Sheets

**Usage:**
```bash
/generate-dashboard
/generate-dashboard --type monthly --year 2025 --month 6
/generate-dashboard --type quarterly --year 2025 --quarter 2
```

**Process:**
1. Activates Dashboard Generator agent
2. Fetches data from Google Sheets via MCP
3. Applies filters if specified
4. Generates 9 charts
5. Creates HTML dashboard
6. Saves to workspace/dashboards/generated/

### /refresh-data
Refresh dashboard with latest Google Sheets data

**Usage:**
```bash
/refresh-data
```

**Process:**
1. Preserves current filters
2. Fetches fresh data
3. Regenerates dashboard
4. Shows what changed

### /analyze-metrics
Deep-dive analysis on specific metrics

**Usage:**
```bash
/analyze-metrics contract-value --period monthly
/analyze-metrics conversion-rate --segment source
```

**Metrics:** contract-value, conversion-rate, new-customers, by-source, by-size, etc.

### /youtube
Extract YouTube video transcripts for research

**Usage:**
```bash
/youtube [video-url] [destination]
```

## Data Access & Configuration

### Google Sheets Access
**Implementation:** Direct Google Sheets API via service account

**Configuration (.env file):**
```bash
GDRIVE_CREDENTIALS_PATH=path/to/service-account-key.json
SPREADSHEET_ID=1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A
SPREADSHEET_NAME=Data
```

**Important Notes:**
- Sheet name is **"Data"** (not "2025_B2B_PotentialCustomersManagement_Upgrade")
- Service account must have read access to the spreadsheet
- Data is cached to `workspace/data/real_data.json` for faster regeneration

### Data Format Handling
The system handles Vietnamese currency formats automatically:
- **Contract Values:** `"1,750,000,000 ₫"` → 1,750 Million VND
- **AHCU Budgets:** `"2,500,000 ₫"` → 2,500,000 VND
- **Date Format:** DD/MM/YYYY (e.g., "15/01/2025")
- **Field Names:** Some fields have `\n` (newline) characters

### Quick Start Commands

**⚡ Recommended Workflow (Fast - Used by `/generate-dashboard`):**
```bash
# Generate with cached data (5-10 seconds - NO credentials needed!)
python tools/scripts/generate_full_dashboard.py --cache-data

# Dashboard opens automatically in browser! (v2.1.0)
```

**Full Workflow (Fresh Data):**
```bash
# Fetch fresh data from Google Sheets + generate (20-30 seconds)
python tools/scripts/generate_full_dashboard.py

# This will:
# 1. Fetch 1,687 records from Google Sheets
# 2. Save to workspace/data/real_data.json
# 3. Generate dashboard
# 4. Auto-open in browser

# Generate with filters
python tools/scripts/generate_full_dashboard.py --cache-data --year 2025 --month 6
python tools/scripts/generate_full_dashboard.py --cache-data --type quarterly --year 2025 --quarter 2
```

**When to Use Each:**
- **Use `--cache-data`** for: Daily updates, testing, quick iterations (FAST! 5-10s)
- **Skip `--cache-data`** for: First setup, weekly/monthly refreshes, major data changes (20-30s)

**Disable Auto-Open:**
```bash
python tools/scripts/generate_full_dashboard.py --cache-data --no-browser
```

## Dashboard Specifications

### 9 Interactive Charts

1. **Phân bố Quy mô Công ty** (Company Size Distribution)
   - Type: Horizontal bar chart
   - Shows: Customer count by company size

2. **Trạng thái Khách hàng Top 10** (Client Status Top 10)
   - Type: Horizontal bar chart
   - Shows: Top 10 customer statuses

3. **Phân bố Giá trị Hợp đồng** (Contract Value Distribution)
   - Type: Vertical bar chart
   - Shows: Distribution across value ranges

4. **Phân bố Nguồn Khách hàng Top 8** (Customer Source Top 8)
   - Type: Vertical bar chart
   - Shows: Top 8 acquisition sources

5. **Top 10 Quận theo Số lượng** (Top 10 Districts)
   - Type: Horizontal bar chart
   - Shows: Geographic distribution

6. **Phân bố Ngân sách AHCU** (AHCU Budget Distribution)
   - Type: Vertical bar chart
   - Shows: Budget distribution across ranges

7. **Lý do Thất bại Deals Top 10** (Failure Reasons Top 10)
   - Type: Horizontal bar chart
   - Shows: Top reasons for lost deals

8. **Xu hướng Doanh thu theo Tháng/Quý** (Revenue Trend)
   - Type: Line chart with markers
   - Field: **Est Month to close** (expected close date)
   - Aggregates: Contract values by expected close period
   - Auto-switches: Monthly/Quarterly view based on filter
   - **IMPORTANT**: Uses "Est Month to close" field, NOT action dates

9. **Sales Funnel - Pipeline Overview**
   - Type: Funnel chart
   - Shows: Customer count at each sales stage
   - Stages (actual from Google Sheets):
     1. Prospecting (10%) - Initial contact
     2. Proposal (30%) - Proposal sent
     3. Meeting/Tour (50%) - Clinic tour conducted
     4. Negotiation (70%) - Trial checkup in progress
     5. Verbal Confirm (90%) - Verbal agreement received
     6. Closed (100%) - Contract signed

### Dashboard Features (v2.1.0)
- ✅ **Client-Side Filtering** - Instant updates, no page reload (NEW in v2.1.0)
- ✅ **Auto-Open Browser** - Dashboard opens automatically after generation (NEW in v2.1.0)
- ✅ **Filter by Est Month to Close** - Pipeline forecast filtering (NEW in v2.1.0)
- ✅ Responsive design (desktop, tablet, mobile)
- ✅ Interactive filters (year, month/quarter, dashboard type)
- ✅ Hover tooltips on all charts
- ✅ Zoom and pan capabilities
- ✅ Download charts as PNG
- ✅ 4 Metrics cards with real-time updates

### Filtering Logic (IMPORTANT)

**Filter Field: "Est Month to close"**

The dashboard filters data based on the **"Est Month to close"** field, which represents the expected month to close a deal. This is the correct field for sales pipeline forecasting.

**Field Format:**
- Format: `"MMM-YYYY"` (e.g., `"Oct-2025"`, `"Nov-2025"`)
- Examples: `"Jan-2025"`, `"Aug-2025"`, `"Dec-2024"`
- Invalid values: `"Undefined"`, `"-"`, empty strings (excluded from filtering)

**Filter Behavior:**
- **No filters**: Shows all customers with valid "Est Month to close" (~1,687 records)
- **Year only** (e.g., 2025): Shows all customers expected to close in 2025
- **Year + Month** (e.g., 2025 + Oct): Shows customers expected to close in Oct-2025 (~120)
- **Year + Quarter** (e.g., 2025 + Q4): Shows customers expected to close in Oct/Nov/Dec 2025

**NOT USED for Filtering:**
- ❌ `Latest Action Date` (last activity date)
- ❌ `Calling Day` (when customer was contacted)
- These fields are for activity tracking, not for pipeline forecasting

**Client-Side Implementation:**
- All filtering happens in browser (JavaScript)
- No backend API required
- Charts regenerate instantly
- Full data (~1,687 records) embedded in HTML for filtering

## Data Schema

### Key Fields

**Customer Identification:**
- Customer ID
- Company Legal Name
- Company ID

**Company Information:**
- Company Size (actual categories in data: "Large (Above 300)", "Medium (100-300)", "Small (Below 100)")
- Industry
- Location
- Location - District

**Contact Information:**
- HR/PIC Name, Title, Phone, Email
- Second PIC details

**Sales Process:**
- Sales Incharge
- Intern Incharge
- Source (acquisition channel)
- Calling Day
- Calling Status
- Sales Stage (Lead, Qualified, Proposal, Negotiation, Closed Won/Lost)

**Service Details (AHCU = Annual Health CheckUp):**
- AHCU Schedule
- Số lượng NV thực tế (actual employee count)
- AHCU Budget
- Last Vendor

**Deal Information:**
- Estimate Contract Value (Million VND)
- Est Month to close
- Next Action
- Phương thức tiếp cận (approach method)

**Outcome Tracking:**
- Outcome
- PIPELINE WEEK
- Expectation this year
- Reason Fail Deals
- Client Status
- Latest Action Date

**See:** context/business-knowledge/customer-fields-explained.md for complete reference

## Workflow Patterns

### Standard Dashboard Generation (with Cache - FAST) ⭐ DEFAULT
```
User → /generate-dashboard → Dashboard Generator Agent →
  Load real_data.json (cached) → Python Scripts →
  Generate 9 charts → Dashboard HTML → Auto-open in browser → User

Command: python tools/scripts/generate_full_dashboard.py --cache-data
Time: 5-10 seconds
Credentials: NOT required
Auto-Opens: Yes (v2.1.0)
```

### Fresh Data Fetch + Generation
```
User → Request fresh data → Dashboard Generator Agent →
  Google Sheets API (via service account) → Save to real_data.json →
  Python Scripts → Generate 9 charts → Dashboard HTML → Auto-open in browser → User

Command: python tools/scripts/generate_full_dashboard.py
Time: 20-30 seconds
Credentials: Required (service account JSON)
Auto-Opens: Yes (v2.1.0)
```

### Data Refresh
```
User → /refresh-data → Dashboard Generator Agent →
  Find latest dashboard → Fetch fresh data via MCP →
  Update real_data.json → Regenerate with same filters →
  Show changes → User
```

### Metrics Analysis
```
User → /analyze-metrics → Data Analyzer Agent →
  Load real_data.json → Process & calculate →
  Generate insights → Save report → User
```

### Cache Data Lifecycle
```
Initial Setup:
  1. Fetch from Google Sheets → Save to real_data.json (one-time)

Daily Usage:
  2. Load real_data.json → Generate dashboards (fast, repeatable)

Weekly/Monthly:
  3. Refresh real_data.json from Google Sheets → Continue with step 2
```

## File Structure

```
b2b-customer-dashboard/
├── .claude/
│   ├── settings.json           # Project configuration
│   ├── mcp-config.json         # MCP servers configuration
│   ├── agents/                 # AI agent definitions
│   └── commands/               # Slash commands
├── context/
│   ├── business-knowledge/     # Domain knowledge
│   └── README.md
├── workspace/
│   ├── dashboards/generated/   # Generated dashboard HTML files
│   └── README.md
├── tools/
│   ├── scripts/                # Python automation
│   ├── templates/              # HTML templates
│   ├── mcp-documentation/      # MCP guides
│   └── README.md
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── CLAUDE.md                   # This file
└── README.md                   # User guide
```

## Security & Best Practices

### Security
- Service account credentials in .env (never commit!)
- Read-only Google Sheets access recommended
- Dashboards contain data snapshots (share carefully)
- No credentials embedded in generated files

### Data Quality
- Validate data before processing
- Handle missing values gracefully
- Use consistent date formats (DD/MM/YYYY)
- Maintain standard status/stage values

### Performance
- Cache spreadsheet data when appropriate
- Refresh only when needed
- Use filters to reduce dataset size
- Clean up old dashboards periodically

### Development
- Test with small datasets first
- Handle MCP errors gracefully
- Provide clear error messages
- Log important operations

## Troubleshooting

### MCP Connection Issues
1. Check .env file has correct credential path
2. Verify service account has spreadsheet access
3. Confirm spreadsheet ID is correct
4. Check MCP server status

### Dashboard Generation Fails
1. Verify Python dependencies installed
2. Check data format in Google Sheets
3. Review error logs
4. Test MCP connection first

### Charts Not Rendering
1. Check browser console for errors
2. Ensure modern browser (Chrome, Firefox, Edge)
3. Verify Plotly.js loaded correctly
4. Check data format matches expected schema

**See:** tools/mcp-documentation/ for detailed troubleshooting

## Communication Style

When interacting with users:
- Be clear and concise
- Provide specific error messages with solutions
- Show progress during long operations
- Summarize results (total records, metrics, etc.)
- Suggest next steps
- Use Vietnamese for chart titles and labels
- Use English for technical terms

## Quick Reference

| Task | Command | Agent |
|------|---------|-------|
| Generate new dashboard | /generate-dashboard | Dashboard Generator |
| Refresh existing dashboard | /refresh-data | Dashboard Generator |
| Analyze metrics | /analyze-metrics | Data Analyzer |
| Research/questions | Ask directly | Research |

## Resources

- **MCP Setup:** tools/mcp-documentation/available-servers.md
- **MCP Tools:** tools/mcp-documentation/tool-reference.md
- **MCP Examples:** tools/mcp-documentation/usage-examples.md
- **Data Fields:** context/business-knowledge/customer-fields-explained.md
- **Metrics:** context/business-knowledge/dashboard-metrics.md
- **Scripts:** tools/README.md

---

**You are ready to help users create powerful analytics dashboards from their B2B customer data!** 🎯📊
