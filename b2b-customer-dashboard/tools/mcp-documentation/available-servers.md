# Available MCP Servers

This project uses Model Context Protocol (MCP) servers for external integrations. Below are the configured servers and their setup instructions.

## Configured MCP Servers

### 1. Google Drive/Sheets (`@modelcontextprotocol/server-gdrive`)

**Purpose:** Access Google Sheets data for the B2B customer spreadsheet

**Quality:** ⭐⭐⭐⭐⭐ Official Anthropic server

**Capabilities:**
- Read Google Sheets data
- List files in Google Drive
- Search for files
- Read/write Google Docs

---

## Setup Instructions

### Google Drive/Sheets Server

#### Prerequisites
- Google Cloud Project
- Service Account credentials
- Spreadsheet access permissions

#### Step 1: Service Account Setup (If not already done)

Since you already have the service account key at:
```
D:\Compass_Coding\COMPASS_AGENTS\claude-code-meta-builder\config\service-account-key.json
```

You can skip this step!

#### Step 2: Environment Configuration

1. Create `.env` file in project root:
```bash
cp .env.example .env
```

2. Edit `.env` and add:
```env
GDRIVE_CREDENTIALS_PATH=D:\Compass_Coding\COMPASS_AGENTS\claude-code-meta-builder\config\service-account-key.json
```

#### Step 3: Grant Spreadsheet Access

1. Open the service account key JSON file
2. Find the `client_email` field (e.g., `your-service@project.iam.gserviceaccount.com`)
3. Open your Google Sheet: "2025_B2B_PotentialCustomersManagement_Upgrade"
4. Click "Share" button
5. Add the service account email with "Viewer" or "Editor" permissions
6. Click "Send"

#### Step 4: Test Connection

```bash
# From project root
claude

# Try reading the spreadsheet
# The MCP server will automatically connect when agents use it
```

---

### Filesystem Server

**Purpose:** Read/write dashboard files and templates

**Quality:** ⭐⭐⭐⭐⭐ Official Anthropic server

#### Configuration

Already configured in `.claude/mcp-config.json`:
```json
{
  "filesystem": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "${PROJECT_ROOT}/workspace/dashboards",
      "${PROJECT_ROOT}/tools/templates"
    ]
  }
}
```

**Allowed Directories:**
- `workspace/dashboards/` - Generated dashboards
- `tools/templates/` - HTML templates

**No additional setup required!**

---

## Verification

To verify MCP servers are working:

1. **Check MCP Status:**
```bash
# In Claude Code session
# MCP servers auto-start when needed
# Check for any error messages
```

2. **Test Google Sheets Access:**
```bash
# Run the dashboard generator
/generate-dashboard

# If successful, MCP is working!
```

---

## Troubleshooting

### Google Drive Server Issues

#### Error: "Failed to connect to Google Sheets"

**Possible causes:**
1. Service account credentials path is incorrect
2. Service account doesn't have access to spreadsheet
3. Spreadsheet ID is wrong

**Solutions:**
1. Verify `GDRIVE_CREDENTIALS_PATH` in `.env`
2. Check spreadsheet sharing settings
3. Confirm spreadsheet ID: `1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A`

#### Error: "Permission denied"

**Solution:**
- Share the spreadsheet with the service account email
- Grant at least "Viewer" permission

#### Error: "Credentials file not found"

**Solution:**
- Check that the file exists at the specified path
- Use absolute path in `.env`
- Ensure no typos in the path

### Filesystem Server Issues

#### Error: "Path not allowed"

**Solution:**
- Filesystem server only has access to configured directories
- Files must be in `workspace/dashboards/` or `tools/templates/`
- Check `.claude/mcp-config.json` configuration

---

## MCP Server Updates

MCP servers are fetched from npm and automatically updated.

To use a specific version:
```json
{
  "gdrive": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-gdrive@1.0.0"
    ]
  }
}
```

To force update:
```bash
# Clear npm cache
npm cache clean --force

# Next run will fetch latest version
```

---

## Additional Resources

- **MCP Documentation:** https://modelcontextprotocol.io/
- **Official Servers:** https://github.com/modelcontextprotocol/servers
- **Google Drive Server:** https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
- **Filesystem Server:** https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem

---

## Quick Reference

| Server | Purpose | Setup Time | Difficulty |
|--------|---------|------------|------------|
| Google Drive | Access spreadsheet | ~10 min | Easy |
| Filesystem | Read/write files | 0 min | None |

**Estimated total setup time:** ~10 minutes (if service account already exists)

**You're ready to go!** 🚀
