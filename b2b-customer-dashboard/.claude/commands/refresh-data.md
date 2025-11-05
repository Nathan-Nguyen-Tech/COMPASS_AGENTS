# Refresh Data Command

Refresh the existing dashboard with the latest data from Google Sheets without changing filters.

## Usage

```bash
/refresh-data
```

## What This Command Does

1. **Preserves Current Filters**
   - Reads current dashboard configuration
   - Maintains year/month/quarter selections
   - Keeps dashboard type (monthly/quarterly)

2. **Fetches Fresh Data**
   - Connects to Google Sheets via MCP
   - Retrieves latest customer data
   - Validates data integrity

3. **Updates Dashboard**
   - Recalculates all metrics
   - Regenerates all 9 charts
   - Updates "Last Updated" timestamp
   - Preserves layout and styling

4. **Shows What Changed**
   - Reports new records added
   - Highlights significant metric changes
   - Flags data quality issues if any

## Use Cases

### Daily Refresh
Update dashboard every morning with previous day's sales activities:
```bash
/refresh-data
```

### After Data Entry
Refresh immediately after sales team updates Google Sheets:
```bash
/refresh-data
```

### Pre-Meeting Refresh
Get latest numbers before a sales meeting:
```bash
/refresh-data
```

## Output

The command provides:
- **Update Summary**: What changed since last refresh
- **New Records**: Count of new customers added
- **Metric Changes**: Key metrics comparison (before/after)
- **Data Quality Report**: Any issues found
- **Updated Dashboard**: Fresh HTML file

### Example Output
```
🔄 Refreshing dashboard data...

✓ Connected to Google Sheets
✓ Retrieved 1,247 records (15 new since last refresh)
✓ Data validation passed

📊 Metrics Changes:
  • Total Contract Value: 1,250M → 1,320M VND (+5.6%)
  • Active Pipeline: 145 → 152 customers (+4.8%)
  • This Month Closed: 12 → 15 deals (+25%)

✓ Dashboard updated successfully
📁 Saved to: workspace/dashboards/generated/dashboard.html
⏰ Last updated: 2025-01-15 09:30:25

🌐 View at: http://localhost:8000/dashboard.html
```

## Comparison with /generate-dashboard

| Feature | /refresh-data | /generate-dashboard |
|---------|---------------|---------------------|
| **Speed** | Fast (~10 sec) | Slower (~30 sec) |
| **Filters** | Preserves current | Can change |
| **Data** | Latest only | Latest + filter options |
| **Use Case** | Quick updates | Initial creation or refilter |
| **Agent** | Dashboard Generator | Dashboard Generator |

**Rule of thumb:**
- Use `/refresh-data` for routine updates
- Use `/generate-dashboard` when changing time periods

## Scheduling Automatic Refresh

### Windows (Task Scheduler)
```bash
# Create a batch file: refresh_dashboard.bat
cd D:\Compass_Coding\COMPASS_AGENTS\b2b-customer-dashboard
claude /refresh-data

# Schedule to run daily at 8 AM
```

### Linux/Mac (Cron)
```bash
# Add to crontab
0 8 * * * cd /path/to/b2b-customer-dashboard && claude /refresh-data
```

### Python Script (For Automation)
```python
import subprocess
import schedule
import time

def refresh_dashboard():
    subprocess.run(['claude', '/refresh-data'],
                   cwd='D:/Compass_Coding/COMPASS_AGENTS/b2b-customer-dashboard')

# Schedule daily at 8 AM
schedule.every().day.at("08:00").do(refresh_dashboard)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Data Change Detection

The refresh command detects:

### New Records
- New customers added to sheet
- Date range of new records

### Updated Records
- Modified existing customer data
- Fields that changed

### Deleted Records
- Records removed from sheet
- Archive or accidental deletion

### Metric Shifts
- Significant metric changes (>10%)
- Trend reversals
- Anomalies

## Error Handling

### Connection Issues
```
❌ Failed to connect to Google Sheets
   → Check internet connection
   → Verify MCP gdrive server is running
   → Confirm credentials are valid
```

### Data Validation Errors
```
⚠️  Data quality issues found:
   • 5 records with missing Company Size
   • 2 records with invalid Contract Value
   → Dashboard generated with warnings
   → Review flagged records in Google Sheets
```

### No Changes Detected
```
ℹ️  No new data since last refresh
   → Dashboard is already up to date
   → Last refresh: 5 minutes ago
```

## Best Practices

### Refresh Frequency
- **High activity**: Every hour during business hours
- **Daily updates**: Once every morning
- **Weekly reviews**: Before weekly sales meetings
- **On-demand**: After major data entry sessions

### Data Quality
1. Validate Google Sheets before refresh
2. Fix any data quality issues flagged
3. Keep data schema consistent
4. Document any manual data corrections

### Performance
1. Refresh during off-peak hours for large datasets
2. Clear old dashboard versions periodically
3. Monitor refresh time trends
4. Optimize if refresh takes >1 minute

### Version Control
1. Keep previous dashboard version as backup
2. Note significant data changes in commit messages
3. Archive monthly dashboards for historical reference

## Troubleshooting

### "Dashboard not found"
```bash
# Generate initial dashboard first
/generate-dashboard

# Then refresh works
/refresh-data
```

### "Filters not preserved"
This is expected when:
- First time generating dashboard
- Dashboard file was manually deleted
- Dashboard format was manually changed

**Solution**: Use `/generate-dashboard` to recreate with desired filters

### "Refresh is slow"
Possible causes:
- Large dataset (>5000 records)
- Slow internet connection
- Google Sheets API rate limiting

**Solutions**:
- Archive old data in Google Sheets
- Use filters to reduce dataset size
- Check network connection

## Integration Examples

### Email Alert After Refresh
```python
# In automation script
import smtplib
from email.message import EmailMessage

def send_dashboard_email(summary):
    msg = EmailMessage()
    msg['Subject'] = 'Dashboard Updated - Daily Sales Report'
    msg['From'] = 'dashboard@company.com'
    msg['To'] = 'sales-team@company.com'
    msg.set_content(summary)

    with smtplib.SMTP('smtp.company.com') as smtp:
        smtp.send_message(msg)

# After /refresh-data
send_dashboard_email(refresh_summary)
```

### Slack Notification
```python
import requests

def notify_slack(webhook_url, message):
    payload = {
        "text": f"📊 Dashboard refreshed!\n{message}"
    }
    requests.post(webhook_url, json=payload)

# After /refresh-data
notify_slack(SLACK_WEBHOOK, "New deals: +3, Total value: +120M VND")
```

## Related Commands

- `/generate-dashboard` - Generate dashboard with different filters
- `/analyze-metrics` - Deep dive into specific metrics

## Quick Reference

```bash
# Simple refresh
/refresh-data

# Check if refresh is needed
# (command will tell you if data hasn't changed)
/refresh-data

# Force refresh (even if no changes)
/refresh-data --force  # (future enhancement)
```

---

**Keep your dashboard fresh! Run `/refresh-data` regularly.** 📊
