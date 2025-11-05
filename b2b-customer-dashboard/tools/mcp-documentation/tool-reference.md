# MCP Tools Reference

Complete reference for all MCP tools available in this project.

## Google Drive Server Tools

### `gdrive_list_files`

List files in Google Drive.

**Parameters:**
- `q` (string, optional): Query string to filter files
- `pageSize` (number, optional): Maximum number of files to return (default: 100)

**Example:**
```javascript
gdrive_list_files({
  q: "name contains '2025_B2B'",
  pageSize: 10
})
```

**Common Queries:**
- `name = 'exact filename'` - Exact match
- `name contains 'keyword'` - Contains keyword
- `mimeType = 'application/vnd.google-apps.spreadsheet'` - Google Sheets only

---

### `gdrive_read_file`

Read file content from Google Drive.

**Parameters:**
- `fileId` (string, required): Google Drive file ID
- `mimeType` (string, optional): MIME type for export

**Example:**
```javascript
// Read our B2B spreadsheet
gdrive_read_file({
  fileId: "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A",
  mimeType: "application/vnd.google-apps.spreadsheet"
})
```

**Returns:** File content (for Sheets: CSV or structured data)

---

### `gdrive_search_files`

Search for files in Google Drive.

**Parameters:**
- `query` (string, required): Search query
- `maxResults` (number, optional): Maximum results (default: 10)

**Example:**
```javascript
gdrive_search_files({
  query: "PotentialCustomers",
  maxResults: 5
})
```

---

## Filesystem Server Tools

### `read_file`

Read file from allowed directories.

**Parameters:**
- `path` (string, required): Relative path from allowed directory

**Allowed Directories:**
- `workspace/dashboards/`
- `tools/templates/`

**Example:**
```javascript
read_file({
  path: "workspace/dashboards/generated/dashboard.html"
})
```

---

### `write_file`

Write file to allowed directories.

**Parameters:**
- `path` (string, required): Relative path from allowed directory
- `content` (string, required): File content

**Example:**
```javascript
write_file({
  path: "workspace/dashboards/generated/dashboard_new.html",
  content: "<html>...</html>"
})
```

---

### `list_directory`

List files in directory.

**Parameters:**
- `path` (string, required): Directory path

**Example:**
```javascript
list_directory({
  path: "workspace/dashboards/generated"
})
```

---

## Usage in Agents

Agents specify which MCP tools they can use in their YAML frontmatter:

```yaml
---
name: Dashboard Generator
mcp:
  gdrive:
    - gdrive_list_files
    - gdrive_read_file
  filesystem:
    - read_file
    - write_file
---
```

## Integration with Python Scripts

While agents use MCP tools directly, Python scripts receive data as JSON:

```python
# Agent uses MCP to fetch data
data = gdrive_read_file(spreadsheet_id)

# Agent passes data to Python script
python dashboard_generator.py --data data.json
```

## Best Practices

### Google Drive Tools

1. **Use specific file IDs when possible**
   - Faster than search
   - More reliable

2. **Limit pageSize for lists**
   - Reduces API calls
   - Faster response

3. **Cache spreadsheet ID**
   - Store in environment variable
   - Don't search every time

### Filesystem Tools

1. **Always use relative paths**
   - Relative to allowed directory
   - More portable

2. **Check file existence before writing**
   - Avoid overwriting accidentally
   - Use meaningful filenames

3. **Organize output files**
   - Use timestamps in filenames
   - Keep workspace clean

## Error Handling

### Common Errors

**Google Drive:**
- `404 Not Found` - File doesn't exist or no access
- `403 Forbidden` - Permission denied
- `401 Unauthorized` - Invalid credentials

**Filesystem:**
- `ENOENT` - File or directory not found
- `EACCES` - Permission denied (outside allowed directories)
- `EEXIST` - File already exists (when expecting new)

### Handling in Agents

Agents should gracefully handle MCP errors:

```markdown
If gdrive_read_file fails:
1. Verify spreadsheet ID is correct
2. Check service account has access
3. Confirm MCP server is running
4. Report error to user with specific guidance
```

## Performance Tips

1. **Batch operations when possible**
   - Read multiple files in one session
   - Minimize API calls

2. **Cache results**
   - Store frequently accessed data locally
   - Refresh only when needed

3. **Use filters and queries**
   - Reduce data transfer
   - Faster processing

## Security Notes

- MCP tools respect configured permissions
- Service account has limited access (only what's shared)
- Filesystem tools can't access parent directories
- Credentials never exposed to Python scripts
- All access is logged by MCP

## Additional Resources

- **MCP Protocol Spec:** https://modelcontextprotocol.io/specification
- **Google Drive API:** https://developers.google.com/drive/api/v3/reference
- **File MIME Types:** https://developers.google.com/drive/api/guides/mime-types
