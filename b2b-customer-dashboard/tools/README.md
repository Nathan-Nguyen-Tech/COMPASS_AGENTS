# Tools Directory

Automation scripts, templates, and documentation for the B2B Customer Dashboard.

## Contents

### scripts/
Python automation scripts:

- **generate_full_dashboard.py** - **[PRIMARY]** Complete dashboard generation (data fetch + generation)
- **dashboard_generator.py** - Core dashboard generation engine (used by generate_full_dashboard.py)
- **data_processor.py** - Data cleaning, filtering, and metrics calculation
- **chart_builder.py** - Plotly chart generation utilities
- **fetch_sheets_data.py** - Google Sheets data fetcher (standalone)
- **serve_dashboard.py** - Local web server for viewing dashboards

### templates/
HTML templates:

- **dashboard_template.html** - Base template for dashboard generation

### mcp-documentation/
MCP server setup and usage guides:

- **available-servers.md** - MCP servers configured and setup instructions
- **tool-reference.md** - Complete MCP tools API reference
- **usage-examples.md** - Practical MCP usage examples and workflows

### SOPs/
Standard Operating Procedures (currently empty, for future workflow documentation)

## Python Scripts

### generate_full_dashboard.py ⭐ PRIMARY SCRIPT
**Purpose:** Complete orchestration - fetch data from Google Sheets AND generate dashboard

**Usage:**
```bash
# Recommended: Use cached data (FAST! 5-10 seconds)
python tools/scripts/generate_full_dashboard.py --cache-data

# Fetch fresh data from Google Sheets (20-30 seconds)
python tools/scripts/generate_full_dashboard.py

# With filters
python tools/scripts/generate_full_dashboard.py --cache-data --type monthly --year 2025 --month 6
python tools/scripts/generate_full_dashboard.py --cache-data --type quarterly --year 2025 --quarter 2
```

**Features:**
- Fetches data from Google Sheets (optional, uses cache by default)
- Processes Vietnamese currency formats
- Generates all 9 interactive charts
- Creates HTML dashboard with client-side filtering
- Auto-opens dashboard in browser (use `--no-browser` to disable)
- Saves data to `workspace/data/real_data.json` for caching

**Dependencies:** fetch_sheets_data.py, dashboard_generator.py

**This is the script executed by `/generate-dashboard` command.**

---

### dashboard_generator.py
**Purpose:** Core dashboard generation engine (usually called by generate_full_dashboard.py)

**Usage:**
```bash
python tools/scripts/dashboard_generator.py --data workspace/data/real_data.json
python tools/scripts/dashboard_generator.py --data workspace/data/real_data.json --type monthly --year 2025 --month 6
```

**Dependencies:** data_processor.py, chart_builder.py

---

### fetch_sheets_data.py
**Purpose:** Standalone Google Sheets data fetcher

**Usage:**
```bash
python tools/scripts/fetch_sheets_data.py \
  --spreadsheet-id "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A" \
  --sheet-name "Data" \
  --output "workspace/data/real_data.json"
```

**Features:**
- Direct Google Sheets API access via service account
- Handles Vietnamese text encoding
- Validates data before saving
- Provides detailed progress output

---

### data_processor.py
**Purpose:** Process and analyze customer data

**Features:**
- Data cleaning and validation
- Filtering by time periods
- Metrics calculation
- Aggregation and binning

**Used by:** dashboard_generator.py

---

### chart_builder.py
**Purpose:** Generate Plotly.js chart specifications

**Features:**
- 9 chart types implemented
- Consistent styling and colors
- Interactive features (hover, zoom, pan)
- Responsive design

**Used by:** dashboard_generator.py

---

### serve_dashboard.py
**Purpose:** Local web server for dashboard viewing

**Usage:**
```bash
python tools/scripts/serve_dashboard.py
python tools/scripts/serve_dashboard.py --port 8080
python tools/scripts/serve_dashboard.py --dashboard path/to/dashboard.html
```

**Features:**
- Serves latest dashboard automatically
- Auto-opens browser
- CORS headers for development
- Simple HTTP server

## Templates

### dashboard_template.html
**Purpose:** Base HTML structure for generated dashboards

**Features:**
- Plotly.js integration
- Bootstrap 5 styling
- Responsive design
- Interactive filter controls
- Professional gradient design

**Placeholders:**
- `{{CHART_*}}` - Chart JSON data
- `{{METRIC_*}}` - Metric values
- `{{FILTER_SUMMARY}}` - Applied filters
- `{{TIMESTAMP}}` - Generation time

## MCP Documentation

Complete guides for working with Model Context Protocol:

### available-servers.md
- Google Drive/Sheets server setup
- Filesystem server configuration
- Environment setup
- Troubleshooting

### tool-reference.md
- Complete MCP tools API
- Parameters and returns
- Usage examples
- Best practices

### usage-examples.md
- Real workflow examples
- Common patterns
- Error handling
- Performance optimization

## Dependencies

### Python Requirements
```
plotly>=5.18.0
pandas>=2.1.0
```

Install:
```bash
pip install -r requirements.txt
```

### Node.js (for MCP servers)
MCP servers run via npx (no installation needed):
- `@modelcontextprotocol/server-gdrive`
- `@modelcontextprotocol/server-filesystem`

## Development

### Adding New Charts
1. Add chart method to `chart_builder.py`
2. Call from `dashboard_generator.py`
3. Add placeholder to `dashboard_template.html`
4. Update documentation

### Modifying Templates
1. Edit `tools/templates/dashboard_template.html`
2. Test with `dashboard_generator.py`
3. Verify responsive design
4. Check all placeholders work

### Testing Scripts
```bash
# Test dashboard generation
python tools/scripts/dashboard_generator.py --help

# Test server
python tools/scripts/serve_dashboard.py --port 8001 --no-browser
```

## Maintenance

### Regular Tasks
1. Keep Python dependencies updated
2. Test MCP server compatibility
3. Verify template renders correctly
4. Update documentation as needed

### Troubleshooting
See MCP documentation for setup issues:
- `mcp-documentation/available-servers.md`
- `mcp-documentation/tool-reference.md`
