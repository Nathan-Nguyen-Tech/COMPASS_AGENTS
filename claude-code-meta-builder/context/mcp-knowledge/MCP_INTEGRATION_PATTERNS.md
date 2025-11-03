# MCP Integration Patterns

> **Purpose:** Best practices, security guidelines, and proven patterns for integrating MCP servers into Claude Code projects

This guide helps agents and developers successfully integrate MCP servers following enterprise-grade standards.

---

## 📚 Table of Contents

1. [Configuration Patterns](#configuration-patterns)
2. [Security Best Practices](#security-best-practices)
3. [Error Handling](#error-handling)
4. [Testing MCP Integrations](#testing-mcp-integrations)
5. [Performance Optimization](#performance-optimization)
6. [Troubleshooting Guide](#troubleshooting-guide)
7. [Migration Strategies](#migration-strategies)

---

## Configuration Patterns

### Pattern 1: Project-Level MCP Configuration

**File Location:** `.claude/mcp-config.json` (in project root)

**Structure:**
```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@scope/package-name"],
      "env": {
        "API_KEY": "value",
        "CONFIG_OPTION": "value"
      },
      "disabled": false
    }
  }
}
```

**When to Use:**
- Project-specific MCP servers
- Custom configuration per project
- Different credentials per project

**Example:**
```json
{
  "mcpServers": {
    "google-sheets": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"],
      "env": {
        "GDRIVE_CREDENTIALS_PATH": "config/service-account-key.json"
      }
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "SLACK_TEAM_ID": "T1234567"
      }
    }
  }
}
```

---

### Pattern 2: Global User Configuration

**File Location:** `~/.config/claude/claude_desktop_config.json`

**When to Use:**
- Shared MCP servers across all projects
- Personal credentials (GitHub, email)
- Common tools (filesystem, time)

**Example:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "/home/user/projects/,/home/user/documents/"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

---

### Pattern 3: Hybrid Configuration

**Strategy:** Global defaults + project overrides

**Global:** Common tools (filesystem, memory)
**Project:** Specific integrations (Google Sheets ID, Slack channel)

**Benefits:**
- Reduce duplication
- Easy project setup
- Centralized credential management

---

### Pattern 4: Environment-Based Configuration

**Development vs Production:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION": "${DB_CONNECTION_STRING}",
        "ENVIRONMENT": "${NODE_ENV}"
      }
    }
  }
}
```

**Environment Variables (.env):**
```bash
# .env.development
DB_CONNECTION_STRING=postgresql://localhost:5432/dev_db
NODE_ENV=development

# .env.production
DB_CONNECTION_STRING=postgresql://prod-server:5432/prod_db
NODE_ENV=production
```

---

## Security Best Practices

### 1. Credential Management

**❌ NEVER DO THIS:**
```json
{
  "env": {
    "API_KEY": "sk-1234567890abcdef"  // Hardcoded secret!
  }
}
```

**✅ DO THIS INSTEAD:**
```json
{
  "env": {
    "API_KEY": "${API_KEY}"  // Environment variable
  }
}
```

**Best Practices:**
- Use environment variables for secrets
- Store credentials in `.env` file (gitignored)
- Use service accounts for production
- Rotate credentials regularly
- Never commit secrets to git

---

### 2. Path Restrictions (Filesystem)

**❌ DANGEROUS:**
```json
{
  "env": {
    "ALLOWED_PATHS": "/"  // Full system access!
  }
}
```

**✅ SAFE:**
```json
{
  "env": {
    "ALLOWED_PATHS": "workspace/,context/read-only,tools/scripts/"
  }
}
```

**Principles:**
- Whitelist specific directories only
- Use relative paths when possible
- Read-only for context directories
- Never allow home directory root

---

### 3. Database Access Control

**Use Least Privilege:**

```sql
-- Read-only user for analytics
CREATE USER analytics_reader WITH PASSWORD 'secure_password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analytics_reader;

-- Limited write user for app
CREATE USER app_writer WITH PASSWORD 'secure_password';
GRANT SELECT, INSERT, UPDATE ON specific_tables TO app_writer;
```

**Connection String Security:**
```json
{
  "env": {
    "POSTGRES_CONNECTION": "postgresql://readonly:${DB_PASSWORD}@localhost/analytics"
  }
}
```

---

### 4. API Token Scopes

**GitHub Example:**

**❌ Too Broad:**
```
Scopes: repo, admin:org, delete_repo
```

**✅ Minimal Required:**
```
Scopes: repo:status, repo:read, issues:write
```

**Slack Example:**

**Required scopes only:**
```
chat:write        # Send messages
channels:read     # List channels
files:write       # Upload files
```

Avoid: `admin`, `delete`, `sensitive data access`

---

### 5. Gitignore Configuration

**Always ignore:**
```gitignore
# Credentials
.env
.env.*
*.key
*.pem
config/*credentials*.json
config/service-account-*.json

# MCP sensitive config
.claude/mcp-config.local.json

# Workspace data
workspace/*
!workspace/README.md

# Database files
*.db
*.sqlite
```

---

## Error Handling

### Pattern 1: Graceful Degradation

**Concept:** If MCP server fails, fall back to alternative approach

**Agent Implementation:**
```markdown
## Data Access Strategy

Primary: Use MCP Google Sheets server
  → Try: mcp__google_sheets_read(range)
  → If fails: Log error, try fallback

Fallback: Direct API call (if credentials available)
  → Use: tools/scripts/sheets_api.py
  → If fails: Inform user, request manual intervention

Last Resort: User provides data
  → Ask user to export CSV
  → Process local file
```

---

### Pattern 2: Retry Logic

**For transient failures:**

```json
{
  "mcpServers": {
    "api-service": {
      "command": "npx",
      "args": ["-y", "@company/mcp-server"],
      "env": {
        "RETRY_ATTEMPTS": "3",
        "RETRY_DELAY_MS": "1000",
        "TIMEOUT_MS": "5000"
      }
    }
  }
}
```

**Agent behavior:**
```markdown
When MCP tool fails:
1. Check error type (timeout, auth, not found)
2. If retriable:
   - Wait exponential backoff (1s, 2s, 4s)
   - Retry up to 3 times
3. If persistent:
   - Log detailed error
   - Suggest user actions
   - Use fallback method
```

---

### Pattern 3: Error Context

**Provide actionable error messages:**

**❌ Bad:**
```
Error: MCP call failed
```

**✅ Good:**
```
Error: Google Sheets MCP server failed to read range "A1:D10"
Reason: Service account lacks permission to spreadsheet
Solution: Share spreadsheet with service-account@project.iam.gserviceaccount.com
Alternative: Provide spreadsheet ID and I'll guide you through permission setup
```

---

## Testing MCP Integrations

### Test Level 1: Configuration Validation

**Before project use:**

```bash
# Test MCP server loads
npx -y @modelcontextprotocol/server-gdrive --help

# Test credentials exist
test -f config/service-account-key.json && echo "✓ Credentials found"

# Test environment variables
echo "Slack token: ${SLACK_BOT_TOKEN:0:10}..."
```

---

### Test Level 2: Connection Testing

**Agent command: `/test-mcp`**

```markdown
Test each configured MCP server:

1. Google Sheets:
   ✓ List files in Drive
   ✓ Read test spreadsheet
   ✓ Write to test cell
   Result: All operations successful

2. Slack:
   ✓ List channels
   ✓ Send test message to #testing
   Result: Message sent successfully

3. Memory:
   ✓ Store test memory
   ✓ Retrieve memory
   ✓ Search memories
   Result: All operations successful

Summary: 3/3 MCP servers operational
```

---

### Test Level 3: Integration Testing

**Test workflows end-to-end:**

```markdown
Test Workflow: Purchase Order Creation

Steps:
1. Read customer list from Google Sheets ✓
2. Calculate VTTH for 100 customers ✓
3. Create new sheet from template ✓
4. Write results to sheet ✓
5. Send Slack notification ✓

Result: Workflow completed in 12.3 seconds
All MCP integrations working as expected
```

---

### Test Level 4: Error Scenario Testing

**Test failure modes:**

```markdown
Error Scenario Tests:

1. Invalid credentials:
   - Removed service account key
   - Expected: Clear error message ✓
   - Expected: Fallback suggestion ✓

2. Rate limiting:
   - Sent 100 rapid requests
   - Expected: Retry with backoff ✓
   - Expected: Success after retry ✓

3. Network timeout:
   - Simulated slow connection
   - Expected: Timeout after 5s ✓
   - Expected: Error logged ✓
```

---

## Performance Optimization

### 1. Caching Strategy

**Cache expensive operations:**

```markdown
## Data Access Pattern

Read spreadsheet data:
1. Check cache (workspace/.cache/sheets-data.json)
2. If cache valid (<5 min old): Use cached data
3. If cache stale:
   - Fetch from MCP server
   - Update cache
   - Return data

Benefits:
- 95% faster on repeated access
- Reduces API quota usage
- Offline capability
```

---

### 2. Batch Operations

**Minimize API calls:**

**❌ Inefficient:**
```markdown
For each customer (100 iterations):
  - Read customer data (MCP call)
  - Calculate VTTH (local)
  - Write result (MCP call)

Total: 200 MCP calls
Time: ~30 seconds
```

**✅ Optimized:**
```markdown
1. Read all customers in one call (MCP batch read)
2. Calculate VTTH for all (local loop)
3. Write all results in one call (MCP batch write)

Total: 2 MCP calls
Time: ~3 seconds
```

---

### 3. Connection Pooling

**For database MCP servers:**

```json
{
  "env": {
    "POSTGRES_POOL_SIZE": "10",
    "POSTGRES_POOL_TIMEOUT": "5000"
  }
}
```

**Benefits:**
- Reuse connections
- Faster queries
- Handle concurrent requests

---

### 4. Lazy Loading

**Don't load MCP servers until needed:**

```markdown
Project startup:
- Load essential config
- Initialize Claude context
- DON'T connect to MCP servers yet

When command executed:
- Connect to required MCP servers only
- Cache connections for session
- Disconnect on completion
```

---

## Troubleshooting Guide

### Issue 1: MCP Server Not Found

**Symptoms:**
```
Error: MCP server "google-sheets" not found
```

**Diagnosis:**
```bash
# Check if package exists
npm view @modelcontextprotocol/server-gdrive

# Check spelling in config
cat .claude/mcp-config.json | grep -A 5 "google-sheets"

# Check npx can access
npx -y @modelcontextprotocol/server-gdrive --version
```

**Solutions:**
- Fix package name typo
- Ensure npm registry accessible
- Check internet connection
- Try manual install: `npm install -g @modelcontextprotocol/server-gdrive`

---

### Issue 2: Authentication Failed

**Symptoms:**
```
Error: 403 Forbidden - Service account lacks permission
```

**Diagnosis:**
```bash
# Check credentials file exists
ls -la config/service-account-key.json

# Validate JSON format
cat config/service-account-key.json | jq .

# Check file referenced in config
grep CREDENTIALS .claude/mcp-config.json
```

**Solutions:**
- Share Google Sheet with service account email
- Regenerate credentials if expired
- Check credentials path is correct
- Verify environment variable set

---

### Issue 3: Rate Limiting

**Symptoms:**
```
Error: 429 Too Many Requests - Rate limit exceeded
```

**Solutions:**
- Implement caching (see Performance section)
- Use batch operations
- Add delays between requests
- Upgrade API quota if needed
- Use exponential backoff

---

### Issue 4: Timeout Errors

**Symptoms:**
```
Error: Request timeout after 5000ms
```

**Solutions:**
- Increase timeout: `"TIMEOUT_MS": "10000"`
- Check network connection
- Verify API endpoint operational
- Use smaller data chunks
- Implement retry logic

---

### Issue 5: Tool Not Available

**Symptoms:**
```
Agent tries to call: mcp__google_sheets_read()
Error: Tool not available
```

**Diagnosis:**
```markdown
1. Check MCP server configured:
   - .claude/mcp-config.json exists
   - Server listed in mcpServers

2. Check server started:
   - No errors in Claude logs
   - Server loaded successfully

3. Check tool name:
   - Use correct prefix: mcp__
   - Use exact tool name from docs
```

**Solutions:**
- Restart Claude Code CLI
- Verify MCP configuration
- Check tool name spelling
- Update server package to latest

---

## Migration Strategies

### Strategy 1: Incremental Migration

**From custom code to MCP:**

**Phase 1: Parallel Run (Week 1)**
```markdown
Keep both:
- tools/scripts/sheets_api.py (existing)
- MCP Google Sheets server (new)

Test MCP server thoroughly
Compare results with custom code
```

**Phase 2: Gradual Switch (Week 2)**
```markdown
New workflows: Use MCP
Existing workflows: Keep custom code
Monitor MCP reliability
```

**Phase 3: Full Migration (Week 3)**
```markdown
All workflows: Use MCP
Archive custom code (don't delete)
Document migration
```

**Phase 4: Cleanup (Week 4)**
```markdown
Remove custom code if MCP stable for 1 week
Update all documentation
Remove old dependencies
```

---

### Strategy 2: Feature Flag Approach

**Configuration:**
```json
{
  "features": {
    "use_mcp_google_sheets": true,
    "use_mcp_slack": false
  }
}
```

**Agent Logic:**
```markdown
When accessing Google Sheets:
1. Check feature flag
2. If use_mcp_google_sheets=true:
   - Use MCP server
3. Else:
   - Use custom code
```

**Benefits:**
- Easy rollback
- A/B testing
- Gradual rollout
- Risk mitigation

---

### Strategy 3: Fallback Architecture

**Always maintain fallback:**

```markdown
## Integration Architecture

Primary: MCP Server
├─ Fast
├─ Standard
└─ Best practice

Fallback: Custom Code
├─ Reliable backup
├─ Known working
└─ Manual if needed

Emergency: Manual Operation
├─ User provides data
└─ Export/import
```

---

## Common Patterns by Project Type

### Learning System Projects

**Recommended MCP Servers:**
1. `server-brave-search` - Research
2. `server-youtube-transcript` - Video learning
3. `server-filesystem` - Content storage
4. `server-memory` - Learning progress

**Configuration:**
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    },
    "youtube": {
      "command": "npx",
      "args": ["-y", "@kimtaeyoon83/mcp-server-youtube-transcript"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "context/research/,workspace/study-guides/"
      }
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_STORAGE_PATH": "workspace/.memory/learning-progress.json"
      }
    }
  }
}
```

---

### Data Analysis Projects

**Recommended MCP Servers:**
1. `server-postgres` or `server-sqlite` - Data storage
2. `server-gdrive` - Google Sheets
3. `server-filesystem` - Report generation

**Configuration:**
```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${DB_CONNECTION}"
      }
    },
    "sheets": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"],
      "env": {
        "GDRIVE_CREDENTIALS_PATH": "config/service-account-key.json"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "workspace/datasets/,workspace/reports/"
      }
    }
  }
}
```

---

### Business Automation Projects

**Recommended MCP Servers:**
1. `server-slack` - Notifications
2. `server-smtp` - Email
3. `server-memory` - Context persistence
4. `server-filesystem` - File operations

**Configuration:**
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "DEFAULT_CHANNEL": "#notifications"
      }
    },
    "email": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-smtp"],
      "env": {
        "SMTP_HOST": "smtp.gmail.com",
        "SMTP_PORT": "587",
        "SMTP_USER": "${EMAIL_USER}",
        "SMTP_PASS": "${EMAIL_APP_PASSWORD}"
      }
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_STORAGE_PATH": "workspace/.memory/automation-context.json"
      }
    }
  }
}
```

---

## Security Checklist

Before deploying MCP integrations:

- [ ] All secrets in environment variables
- [ ] `.env` file in `.gitignore`
- [ ] Filesystem paths restricted to project directories
- [ ] Database users have minimum required permissions
- [ ] API tokens have minimum required scopes
- [ ] Service accounts properly configured
- [ ] Credentials rotation schedule established
- [ ] Error messages don't expose secrets
- [ ] Audit logging enabled
- [ ] Backup strategy for MCP storage files

---

## Performance Checklist

- [ ] Caching implemented for repeated operations
- [ ] Batch operations instead of individual calls
- [ ] Connection pooling configured
- [ ] Lazy loading of MCP servers
- [ ] Rate limiting handled gracefully
- [ ] Timeouts configured appropriately
- [ ] Monitoring for slow operations
- [ ] Fallback for performance-critical paths

---

## Resources

- **MCP Protocol:** https://modelcontextprotocol.io/
- **Security Best Practices:** https://docs.anthropic.com/security
- **Performance Tips:** https://docs.anthropic.com/performance
- **Community Patterns:** https://github.com/modelcontextprotocol/servers/discussions

---

**Document Version:** 1.0
**Last Updated:** 2025-01-03
**Next Review:** 2025-04-03
