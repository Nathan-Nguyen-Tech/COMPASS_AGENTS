# B2B Customer Dashboard

Interactive analytics dashboard for B2B potential customer pipeline management, powered by Claude Code and MCP.

![Dashboard Preview](https://img.shields.io/badge/Status-Active-success)
![MCP](https://img.shields.io/badge/MCP-Enabled-blue)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-orange)

## Overview

Transform your Google Sheets customer data into beautiful, interactive dashboards with just one command. This project uses Model Context Protocol (MCP) for seamless Google Sheets integration and generates professional web dashboards with 9 interactive charts.

### Key Features

- **🚀 One-Command Generation** - Generate complete dashboards instantly
- **📊 9 Interactive Charts** - Comprehensive analytics visualizations
- **🔄 Auto-Refresh** - Update with latest data in seconds
- **🎯 Smart Filtering** - Filter by year, month, or quarter based on "Est Month to close"
- **📱 Responsive Design** - Works on desktop, tablet, and mobile
- **🔒 Secure** - MCP-based authentication, no hardcoded credentials
- **⚡ Fast** - Cache mode: 5-10s | Fresh data: 20-30s
- **🌐 Auto-Open** - Dashboard opens in browser automatically (NEW in v2.1.0)

### What You Get

1. **Company Size Distribution** - Understand your customer segments
2. **Client Status Analysis** - Track customer lifecycle states
3. **Contract Value Distribution** - Revenue opportunity analysis
4. **Customer Source Breakdown** - Channel effectiveness
5. **Geographic Distribution** - Top districts by customer count
6. **Budget Distribution** - AHCU budget analysis
7. **Failure Reasons** - Learn why deals are lost
8. **Revenue Trend** - Track growth over time
9. **Sales Funnel** - Pipeline conversion analysis

## Quick Start

### Prerequisites

- **Python 3.8+** installed
- **Node.js** (for MCP servers)
- **Claude Code** CLI
- **Google Cloud Service Account** with Sheets access

### Installation

**1. Install Python Dependencies**
```bash
pip install -r requirements.txt
```

**2. Configure Environment**
```bash
# Copy environment template
cp .env.example .env

# Edit .env and set your credentials path
# GDRIVE_CREDENTIALS_PATH=path/to/your/service-account-key.json
```

**3. Grant Spreadsheet Access**
- Open your service account key JSON file
- Find the `client_email` field
- Share your Google Sheet with that email address (Viewer or Editor permission)

**4. You're Ready!**
```bash
# Start Claude Code
claude

# Generate your first dashboard
/generate-dashboard
```

## Usage

### Generate Dashboard

**Basic (all data):**
```bash
/generate-dashboard
```

**Monthly view for June 2025:**
```bash
/generate-dashboard --type monthly --year 2025 --month 6
```

**Quarterly view for Q2 2025:**
```bash
/generate-dashboard --type quarterly --year 2025 --quarter 2
```

### Refresh Data

**Update dashboard with latest data:**
```bash
/refresh-data
```
Preserves your current filters and shows what changed.

### Analyze Metrics

**Deep dive into specific metrics:**
```bash
/analyze-metrics contract-value --period monthly
/analyze-metrics conversion-rate --segment source
/analyze-metrics by-district
```

### View Dashboard

**Option 1: Auto-serve (recommended)**
```bash
python tools/scripts/serve_dashboard.py
```
Opens dashboard in browser automatically at http://localhost:8000

**Option 2: Manual open**
Navigate to `workspace/dashboards/generated/` and double-click the HTML file.

## Dashboard Features

### Interactive Charts
- **Hover tooltips** - Detailed info on hover
- **Zoom & Pan** - Explore data interactively
- **Download** - Export charts as PNG
- **Responsive** - Adapts to screen size

### Filter Controls
- **Dashboard Type** - Monthly or Quarterly view
- **Year** - Filter by specific year or all
- **Month/Quarter** - Drill down to specific period (based on "Est Month to close")
- **Apply Filters** - Instantly regenerate charts with client-side filtering
- **Refresh Data** - Update with latest from Google Sheets

**Filtering Logic (v2.1.0):**
- Filters use "Est Month to close" field (expected close date)
- Shows pipeline forecast, not historical activity
- Example: Oct-2025 filter shows ~120 customers expected to close in October
- Client-side filtering for instant results (no page reload)

### Performance
- **Generation (fresh data):** 20-30 seconds for full dashboard
- **Generation (cached data):** 5-10 seconds (3-5x faster!) 🚀
- **Client-side filtering:** Instant (no reload)
- **Load Time:** <3 seconds in browser
- **File Size:** ~23 KB per dashboard (embedded data: ~2.9 MB)

## Architecture

### MCP-First Design
This project uses **Model Context Protocol (MCP)** instead of custom code for integrations:

- **Google Sheets Access** - MCP `server-gdrive` (vs. custom Sheets API code)
- **File Operations** - MCP `server-filesystem` (vs. custom file handling)

**Benefits:**
- ✅ ~20 hours saved vs custom code
- ✅ Auto-updates with MCP server improvements
- ✅ Best-practice security built-in
- ✅ Minimal maintenance required

### Technology Stack

```
┌─────────────────────────────────────────┐
│      Web Dashboard (Browser)            │
│   Plotly.js + Bootstrap 5               │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│   Python Dashboard Generator            │
│   - Data Processing (pandas)            │
│   - Chart Generation (Plotly)           │
│   - Template Rendering                  │
└────┬───────────────────┬────────────────┘
     │                   │
┌────▼─────┐      ┌──────▼──────┐
│   MCP    │      │     MCP     │
│  GDrive  │      │ Filesystem  │
└────┬─────┘      └──────┬──────┘
     │                   │
┌────▼─────┐      ┌──────▼──────┐
│  Google  │      │   Local     │
│  Sheets  │      │   Files     │
└──────────┘      └─────────────┘
```

## Data Source

### Google Sheets Configuration

**Spreadsheet Name:** 2025_B2B_PotentialCustomersManagement_Upgrade
**Spreadsheet ID:** `1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A`

### Required Fields
- Customer ID or Company Legal Name
- Sales Incharge (recommended)
- Estimate Contract Value (for revenue analysis)
- Sales Stage (for funnel analysis)
- Client Status (for status analysis)

### Optional Fields
All other fields enhance analytics but aren't required.

**See:** `context/business-knowledge/customer-fields-explained.md` for complete field reference.

## Project Structure

```
b2b-customer-dashboard/
├── .claude/
│   ├── settings.json           # Project config
│   ├── mcp-config.json         # MCP servers
│   ├── agents/                 # 4 specialized agents
│   └── commands/               # 4 slash commands
├── context/
│   └── business-knowledge/     # Data & metrics documentation
├── workspace/
│   └── dashboards/generated/   # Your dashboards here!
├── tools/
│   ├── scripts/                # Python automation
│   ├── templates/              # HTML template
│   └── mcp-documentation/      # MCP setup guides
├── .env.example                # Environment template
├── .gitignore                  # Git ignore
├── requirements.txt            # Python deps
├── CLAUDE.md                   # Project context (for Claude)
└── README.md                   # This file
```

## Documentation

### For Users
- **This README** - Getting started and usage
- **tools/mcp-documentation/available-servers.md** - MCP setup guide
- **context/business-knowledge/customer-fields-explained.md** - Data schema
- **context/business-knowledge/dashboard-metrics.md** - Metrics definitions

### For Developers
- **CLAUDE.md** - Full project context for Claude Code
- **tools/mcp-documentation/tool-reference.md** - MCP API reference
- **tools/mcp-documentation/usage-examples.md** - MCP patterns
- **tools/README.md** - Scripts documentation

## Troubleshooting

### Dashboard Generation Fails

**Error: "Failed to connect to Google Sheets"**

**Solutions:**
1. Check `.env` has correct `GDRIVE_CREDENTIALS_PATH`
2. Verify service account has access to spreadsheet
3. Confirm spreadsheet ID is correct
4. Check MCP gdrive server is running

**Error: "No data matches filters"**

**Solutions:**
1. Check "Est Month to close" field exists in your data
2. Try generating without filters first
3. Verify "Est Month to close" format is "MMM-YYYY" (e.g., "Oct-2025")
4. Ensure records have valid values (not "Undefined", "-", or empty)
5. Open browser console (F12) to see detailed filter debug logs

### Charts Not Rendering

**Solutions:**
1. Open browser console (F12) and check for errors
2. Ensure you're using a modern browser (Chrome, Firefox, Edge, Safari)
3. Verify Plotly.js loaded (check network tab)
4. Try clearing browser cache

### MCP Server Issues

**See:** `tools/mcp-documentation/available-servers.md` for detailed troubleshooting

## Best Practices

### Data Quality
- ✅ Use consistent date formats (DD/MM/YYYY)
- ✅ Maintain standard status/stage values
- ✅ Fill key fields (Contract Value, Sales Stage, Client Status)
- ✅ Validate data before generating dashboard

### Dashboard Management
- ✅ Generate daily during active sales periods
- ✅ Archive monthly/quarterly snapshots
- ✅ Clean up old dashboards (keep last 7 days)
- ✅ Refresh before important meetings

### Security
- ✅ Never commit service account credentials
- ✅ Use read-only Sheets access when possible
- ✅ Be careful when sharing dashboards (contain data snapshots)
- ✅ Review `.gitignore` before committing

## Performance Tips

### For Large Datasets (>5000 records)
- Use filters to reduce dataset size
- Generate quarterly instead of monthly
- Archive old data in separate sheet
- Run generation during off-peak hours

### For Faster Updates
- Use `/refresh-data` instead of `/generate-dashboard`
- Cache data locally when appropriate
- Batch multiple analysis requests

## Roadmap

### Planned Features
- [ ] Email dashboard distribution
- [ ] Scheduled automatic generation
- [ ] Custom chart builder
- [ ] Export to PDF
- [ ] Multi-sheet analysis
- [ ] Comparison dashboards (period-over-period)

### Completed
- [x] MCP integration for Google Sheets
- [x] 9 interactive charts
- [x] Filter by year/month/quarter (v2.1.0: based on "Est Month to close")
- [x] Refresh command
- [x] Metrics analysis
- [x] Responsive design
- [x] Cache data feature (v2.0.0)
- [x] Client-side filtering (v2.1.0)
- [x] Auto-open dashboard in browser (v2.1.0)
- [x] Vietnamese currency format handling (v2.0.0)

## Contributing

This is a private project, but suggestions welcome!

## Support

### Getting Help
1. Check this README
2. Review MCP documentation in `tools/mcp-documentation/`
3. Check field definitions in `context/business-knowledge/`
4. Ask Claude Code for help

### Common Questions

**Q: Can I use this with a different Google Sheet?**
A: Yes! Update `SPREADSHEET_ID` in `.env` and ensure field names match or modify `data_processor.py`.

**Q: Can I customize the charts?**
A: Yes! Edit `tools/scripts/chart_builder.py` to modify chart types, colors, and layouts.

**Q: Can I add more charts?**
A: Yes! Add new methods in `chart_builder.py`, update `dashboard_generator.py`, and modify the HTML template.

**Q: Does this work with Excel files?**
A: Not directly. Export Excel to Google Sheets first, or modify the data loading logic.

**Q: Can I deploy this to a web server?**
A: Generated dashboards are static HTML files that can be hosted anywhere. For dynamic updates, you'd need to set up scheduled generation.

## License

Private project. All rights reserved.

## Acknowledgments

- **Claude Code** - AI-powered development environment
- **MCP** - Model Context Protocol for integrations
- **Plotly** - Interactive visualization library
- **Bootstrap** - UI framework

---

**Ready to transform your customer data into insights?** 🚀

```bash
claude
/generate-dashboard
```

---

## Quick Links

- 📖 [MCP Setup Guide](tools/mcp-documentation/available-servers.md)
- 📊 [Data Fields Reference](context/business-knowledge/customer-fields-explained.md)
- 📈 [Metrics Definitions](context/business-knowledge/dashboard-metrics.md)
- 🔧 [Scripts Documentation](tools/README.md)
- 🤖 [Project Context (Claude)](CLAUDE.md)

**Questions?** Ask Claude Code - it knows this project inside out! 💡
