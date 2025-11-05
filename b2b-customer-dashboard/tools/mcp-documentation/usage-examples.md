# MCP Usage Examples

Practical examples of using MCP tools in common workflows for the B2B Customer Dashboard.

## Workflow 1: Generate Dashboard from Google Sheets

### Step-by-Step Process

**1. User runs command:**
```bash
/generate-dashboard --year 2025 --month 6
```

**2. Dashboard Generator agent activates:**
- Uses MCP `gdrive_read_file` to fetch spreadsheet data
- Passes data to Python script
- Generates HTML dashboard
- Uses MCP `write_file` to save result

**3. Behind the scenes:**

```markdown
Agent workflow:
1. Call gdrive_read_file with spreadsheet ID
2. Receive customer data as JSON
3. Filter data (year=2025, month=6)
4. Calculate metrics
5. Generate charts with Plotly
6. Build HTML from template
7. Call write_file to save dashboard
8. Return file path to user
```

---

## Workflow 2: Refresh Dashboard Data

### Step-by-Step Process

**1. User runs command:**
```bash
/refresh-data
```

**2. Dashboard Generator agent:**

```markdown
1. Use list_directory to find latest dashboard
   → filesystem: list_directory("workspace/dashboards/generated")

2. Read current dashboard to get filter settings
   → filesystem: read_file("dashboard_20250115.html")

3. Fetch fresh data from Google Sheets
   → gdrive: gdrive_read_file(spreadsheet_id)

4. Compare with previous data (detect changes)

5. Regenerate dashboard with same filters

6. Save updated dashboard
   → filesystem: write_file("dashboard_20250115.html", new_content)

7. Report what changed to user
```

---

## Workflow 3: Analyze Specific Metrics

### Step-by-Step Process

**1. User runs command:**
```bash
/analyze-metrics contract-value --period monthly
```

**2. Data Analyzer agent:**

```markdown
1. Fetch all customer data
   → gdrive: gdrive_read_file(spreadsheet_id)

2. Process and aggregate data by month

3. Calculate metrics:
   - Total contract value per month
   - Month-over-month growth
   - Trends and patterns

4. Generate analysis report (JSON)

5. Save report
   → filesystem: write_file("workspace/analysis/contract_value.json", report)

6. Present insights to user
```

---

## Example: MCP Tool Calls

### Reading the Spreadsheet

```javascript
// Agent makes this call
const data = await mcp.tools.gdrive_read_file({
  fileId: "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A",
  mimeType: "application/vnd.google-apps.spreadsheet"
});

// Returns structured data like:
{
  "sheets": [
    {
      "name": "Customers",
      "data": [
        {
          "Customer ID": "001",
          "Company Legal Name": "ABC Corp",
          "Company Size": "100-200",
          "Estimate Contract Value (Million VND)": "150",
          // ... more fields
        },
        // ... more rows
      ]
    }
  ]
}
```

### Saving Dashboard

```javascript
// Agent generates HTML content
const dashboardHTML = generateDashboardHTML(data, charts);

// Save using MCP
await mcp.tools.write_file({
  path: "workspace/dashboards/generated/dashboard_20250615.html",
  content: dashboardHTML
});

// Returns: { success: true, path: "..." }
```

### Listing Generated Dashboards

```javascript
// List all dashboards
const files = await mcp.tools.list_directory({
  path: "workspace/dashboards/generated"
});

// Returns:
{
  "files": [
    "dashboard_20250615_143022.html",
    "dashboard_20250614_090512.html",
    "dashboard_20250613_161145.html"
  ]
}

// Agent can find latest by timestamp
```

---

## Common Patterns

### Pattern 1: Data Fetch → Process → Save

```markdown
Most dashboard operations follow this pattern:

1. **Fetch** (MCP gdrive)
   → Get source data from Google Sheets

2. **Process** (Python script)
   → Clean, filter, aggregate, calculate
   → Generate visualizations

3. **Save** (MCP filesystem)
   → Write output to workspace

4. **Present** (Agent)
   → Show results to user
```

### Pattern 2: Read → Modify → Write

```markdown
For updates and refreshes:

1. **Read** existing file (MCP filesystem)
   → Get current dashboard or config

2. **Modify** content
   → Update data, change settings

3. **Write** back (MCP filesystem)
   → Save updated version
```

### Pattern 3: Search → Select → Operate

```markdown
When working with multiple files:

1. **Search** (MCP gdrive or filesystem)
   → Find files matching criteria

2. **Select** best match
   → Latest, by name, by size, etc.

3. **Operate** on selected file
   → Read, process, update
```

---

## Error Handling Examples

### Handle Missing Spreadsheet Access

```markdown
Agent workflow:

try {
  data = gdrive_read_file(spreadsheet_id)
} catch (error) {
  if (error.code === 403) {
    Message to user:
    "❌ Permission denied to access spreadsheet.

    The service account needs access. Please:
    1. Open the spreadsheet
    2. Click 'Share'
    3. Add: [service-account-email]
    4. Grant 'Viewer' permission
    5. Try again"
  }
}
```

### Handle File Not Found

```markdown
Agent workflow:

try {
  dashboard = read_file("workspace/dashboards/generated/dashboard.html")
} catch (error) {
  if (error.code === 'ENOENT') {
    Message to user:
    "No dashboard found. Generate one first:
    /generate-dashboard"
  }
}
```

---

## Performance Optimization

### Cache Spreadsheet Data

```markdown
Instead of reading spreadsheet every time:

1. Read spreadsheet once
   → gdrive_read_file(spreadsheet_id)

2. Save as local cache
   → write_file("workspace/cache/data.json", data)

3. Use cached data for quick operations

4. Refresh cache only when needed
   → /refresh-data command
```

### Batch Operations

```markdown
Instead of multiple gdrive calls:

BAD:
for each customer:
  read_customer_details(customer_id)  # Many API calls

GOOD:
all_data = gdrive_read_file(spreadsheet_id)  # One API call
for each customer in all_data:
  process(customer)
```

---

## Integration with Python Scripts

Agents use MCP, but Python scripts work with files:

```markdown
Agent → MCP → Python → MCP → User

Example flow:

1. Agent: Use MCP to get data
   data = gdrive_read_file(...)

2. Agent: Save data to temp file
   write_file("temp/data.json", data)

3. Agent: Call Python script
   python dashboard_generator.py --data temp/data.json

4. Python: Process data, generate output
   output = generate_dashboard(data)
   save_to("workspace/dashboards/dashboard.html")

5. Agent: Confirm to user
   "Dashboard saved to: workspace/dashboards/dashboard.html"
```

---

## Best Practices Summary

1. **Minimize MCP calls**
   - Fetch once, use multiple times
   - Cache when appropriate

2. **Handle errors gracefully**
   - Provide specific error messages
   - Suggest concrete fixes

3. **Use meaningful file names**
   - Include timestamps
   - Descriptive names

4. **Clean up temporary files**
   - Delete after use
   - Keep workspace organized

5. **Respect rate limits**
   - Don't hammer Google Sheets API
   - Use appropriate pageSize

6. **Test with small datasets first**
   - Verify logic
   - Then scale to full data

---

## Debugging MCP Issues

### Check MCP Server Status

```markdown
If MCP calls fail:

1. Check .claude/mcp-config.json is valid JSON
2. Verify environment variables are set (.env file)
3. Check service account credentials exist
4. Test with simple call (list files)
5. Check Claude Code logs for MCP errors
```

### Verbose Logging

```markdown
To debug MCP calls:

1. Check what data MCP returns
2. Verify format matches expectations
3. Test MCP calls in isolation
4. Compare with expected schema
```

---

## Quick Reference

| Task | MCP Tool | Example |
|------|----------|---------|
| Get spreadsheet data | gdrive_read_file | `gdrive_read_file({fileId: "..."})` |
| Save dashboard | write_file | `write_file({path: "...", content: "..."})` |
| List dashboards | list_directory | `list_directory({path: "workspace/dashboards"})` |
| Search files | gdrive_search_files | `gdrive_search_files({query: "..."})` |

---

**You now have all the patterns needed to work with MCP in this project!** 🎉
