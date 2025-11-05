# Workspace Directory

Active working directory for dashboard generation and analysis outputs.

## Contents

### dashboards/
Generated dashboard HTML files:

- **generated/** - Auto-generated dashboard files from `/generate-dashboard` command
  - Dashboard HTML files with timestamps
  - Latest dashboard available here

## Structure

```
workspace/
├── dashboards/
│   └── generated/
│       ├── dashboard_20250615_143022.html
│       ├── dashboard_20250614_090512.html
│       └── ...
└── README.md (this file)
```

## Generated Files

### Dashboard Files
- **Format:** HTML with embedded JavaScript (Plotly.js)
- **Naming:** `dashboard_YYYYMMDD_HHMMSS.html`
- **Content:** Complete interactive dashboard with all 9 charts
- **Size:** Typically 200-500 KB per file

## Usage

### Opening Dashboards
```bash
# Option 1: Start local server
python tools/scripts/serve_dashboard.py

# Option 2: Open directly in browser
# Navigate to workspace/dashboards/generated/
# Double-click the HTML file
```

### Finding Latest Dashboard
Latest dashboard is the file with most recent timestamp in filename.

## Cleanup

### Manual Cleanup
Periodically delete old dashboards to save space:
```bash
# Keep last 7 days only
# Manually delete older files
```

### Recommended Retention
- **Last 24 hours:** Keep all (for comparison)
- **Last 7 days:** Keep daily snapshots
- **Older than 7 days:** Archive or delete

## Storage Notes

- Each dashboard is self-contained (no external dependencies)
- Dashboards can be archived or shared via email
- No sensitive credentials embedded (only data snapshot)
- Average size: ~300 KB per dashboard

## Best Practices

1. **Regular cleanup:** Don't let old dashboards accumulate
2. **Archive important versions:** Save monthly/quarterly snapshots
3. **Name meaningfully:** If manually renaming, keep timestamp
4. **Share carefully:** Dashboards contain business data
