# MCP Server Catalog

> **Last Updated:** 2025-01-03
> **Purpose:** Comprehensive catalog of Model Context Protocol (MCP) servers for agent integration

This catalog provides a curated list of MCP servers organized by category, helping agents quickly discover and recommend appropriate integrations for project needs.

---

## 📚 Table of Contents

1. [Data & Storage](#data--storage)
2. [Communication & Notifications](#communication--notifications)
3. [Development & Code](#development--code)
4. [Search & Research](#search--research)
5. [AI & Memory](#ai--memory)
6. [Utilities & System](#utilities--system)
7. [Evaluation Criteria](#evaluation-criteria)

---

## Data & Storage

### 1. Google Drive / Sheets (`@modelcontextprotocol/server-gdrive`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Access and manipulate Google Drive files, Google Sheets, and Google Docs

**Tools Provided:**
- `gdrive_list_files` - List files in Drive
- `gdrive_read_file` - Read file contents
- `gdrive_write_file` - Write/update files
- `gdrive_search` - Search Drive
- `google_sheets_read` - Read spreadsheet data
- `google_sheets_write` - Update spreadsheet cells
- `google_sheets_create` - Create new sheets
- `google_docs_read` - Read document content

**Use Cases:**
- Inventory management from Google Sheets
- Purchase order creation and tracking
- Document generation and storage
- Data import/export workflows
- Collaborative data management

**Installation:**
```bash
npx -y @modelcontextprotocol/server-gdrive
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"],
      "env": {
        "GDRIVE_CREDENTIALS_PATH": "path/to/service-account-key.json"
      }
    }
  }
}
```

**Security:**
- Requires service account JSON or OAuth2 credentials
- Scope: `https://www.googleapis.com/auth/drive`
- Store credentials in gitignored config/ directory
- Use service accounts for production, OAuth for user-specific access

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive

---

### 2. PostgreSQL Database (`@modelcontextprotocol/server-postgres`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Query and manage PostgreSQL databases

**Tools Provided:**
- `postgres_query` - Execute SQL queries
- `postgres_list_tables` - List database tables
- `postgres_describe_table` - Get table schema
- `postgres_insert` - Insert records
- `postgres_update` - Update records
- `postgres_delete` - Delete records

**Use Cases:**
- Customer data management
- Inventory tracking
- Analytics and reporting
- Order management systems
- User authentication data

**Installation:**
```bash
npx -y @modelcontextprotocol/server-postgres
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://user:pass@localhost:5432/dbname"
      }
    }
  }
}
```

**Security:**
- Use connection pooling for performance
- Never commit connection strings
- Use read-only user for analytics
- Implement row-level security for multi-tenant

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/postgres

---

### 3. SQLite Database (`@modelcontextprotocol/server-sqlite`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Query and manage local SQLite databases

**Tools Provided:**
- `sqlite_query` - Execute SQL queries
- `sqlite_list_tables` - List tables
- `sqlite_describe_table` - Get schema
- `sqlite_create_table` - Create tables
- `sqlite_insert` - Insert data

**Use Cases:**
- Local data storage
- Offline-first applications
- Calculation history
- Configuration storage
- Embedded databases in projects

**Installation:**
```bash
npx -y @modelcontextprotocol/server-sqlite
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite"],
      "env": {
        "SQLITE_DB_PATH": "workspace/data/project.db"
      }
    }
  }
}
```

**Security:**
- Database files should be in workspace/ (gitignored)
- Use WAL mode for concurrent access
- Regular backups recommended

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite

---

### 4. Google Sheets (`@executeautomation/gsheets-mcp-server`)

**Status:** 🌟 Community (Karthik KK)
**Last Updated:** 2024-11
**Maintenance:** Active

**Purpose:** Specialized Google Sheets integration (alternative to gdrive)

**Tools Provided:**
- `gsheets_read_range` - Read cell range
- `gsheets_write_range` - Write to range
- `gsheets_append` - Append rows
- `gsheets_clear` - Clear range
- `gsheets_format` - Format cells
- `gsheets_create_sheet` - Add sheet tab

**Use Cases:**
- VTTH calculations (BO_KHO agent)
- Inventory comparisons
- Report generation
- Data validation
- Batch updates

**Installation:**
```bash
npx -y @executeautomation/gsheets-mcp-server
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "gsheets": {
      "command": "npx",
      "args": ["-y", "@executeautomation/gsheets-mcp-server"],
      "env": {
        "GOOGLE_SHEETS_CREDENTIALS": "config/service-account-key.json",
        "SPREADSHEET_ID": "your-sheet-id"
      }
    }
  }
}
```

**Security:**
- Similar to gdrive server
- Service account recommended
- Share spreadsheet with service account email

**Documentation:** https://github.com/executeautomation/gsheets-mcp-server

---

## Communication & Notifications

### 5. Slack (`@modelcontextprotocol/server-slack`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Send messages and interact with Slack workspaces

**Tools Provided:**
- `slack_post_message` - Send message to channel
- `slack_list_channels` - List available channels
- `slack_get_channel_history` - Read messages
- `slack_upload_file` - Upload file to channel
- `slack_react_to_message` - Add reaction
- `slack_send_dm` - Direct message to user

**Use Cases:**
- Purchase order notifications
- Error alerts
- Report distribution
- Team notifications
- Workflow status updates

**Installation:**
```bash
npx -y @modelcontextprotocol/server-slack
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token",
        "SLACK_SIGNING_SECRET": "your-secret"
      }
    }
  }
}
```

**Security:**
- Use bot tokens (xoxb-) not user tokens
- Minimum required scopes only
- Rotate tokens periodically
- Store in environment variables

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/slack

---

### 6. Email (`@modelcontextprotocol/server-smtp`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-11
**Maintenance:** Active

**Purpose:** Send emails via SMTP

**Tools Provided:**
- `smtp_send_email` - Send email
- `smtp_send_html_email` - Send HTML email
- `smtp_send_with_attachments` - Send with files

**Use Cases:**
- Report delivery
- Purchase order confirmations
- Alert notifications
- Weekly summaries
- Approval requests

**Installation:**
```bash
npx -y @modelcontextprotocol/server-smtp
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "smtp": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-smtp"],
      "env": {
        "SMTP_HOST": "smtp.gmail.com",
        "SMTP_PORT": "587",
        "SMTP_USER": "notifications@company.com",
        "SMTP_PASS": "app-specific-password"
      }
    }
  }
}
```

**Security:**
- Use app-specific passwords for Gmail
- TLS/SSL required
- Rate limiting awareness
- SPF/DKIM configuration

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/smtp

---

## Development & Code

### 7. GitHub (`@modelcontextprotocol/server-github`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Interact with GitHub repositories, issues, and pull requests

**Tools Provided:**
- `github_create_repository` - Create repo
- `github_get_file` - Read file contents
- `github_create_file` - Create/update files
- `github_create_issue` - Create issue
- `github_create_pull_request` - Create PR
- `github_list_issues` - List issues
- `github_search_code` - Search code
- `github_get_commits` - Get commit history

**Use Cases:**
- Code review automation
- Issue tracking
- Documentation generation
- Release management
- Code analysis
- CI/CD integration

**Installation:**
```bash
npx -y @modelcontextprotocol/server-github
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token",
        "GITHUB_OWNER": "organization-name"
      }
    }
  }
}
```

**Security:**
- Use fine-grained tokens
- Minimum permissions (repo, issues, etc.)
- Rotate tokens regularly
- Use GitHub Apps for production

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/github

---

### 8. GitLab (`@modelcontextprotocol/server-gitlab`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-11
**Maintenance:** Active

**Purpose:** Interact with GitLab repositories and CI/CD

**Tools Provided:**
- Similar to GitHub server
- Additional: `gitlab_trigger_pipeline`, `gitlab_get_job_logs`

**Use Cases:**
- Same as GitHub
- CI/CD pipeline management
- Self-hosted Git workflows

**Installation:**
```bash
npx -y @modelcontextprotocol/server-gitlab
```

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab

---

### 9. Filesystem (`@modelcontextprotocol/server-filesystem`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Read, write, and manage files on local filesystem

**Tools Provided:**
- `fs_read_file` - Read file contents
- `fs_write_file` - Write to file
- `fs_list_directory` - List directory contents
- `fs_create_directory` - Create directories
- `fs_delete_file` - Delete files
- `fs_move_file` - Move/rename files
- `fs_get_file_info` - File metadata

**Use Cases:**
- Document management
- Log file analysis
- Configuration file updates
- Template processing
- File organization
- Data import/export

**Installation:**
```bash
npx -y @modelcontextprotocol/server-filesystem
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "workspace/,context/,tools/"
      }
    }
  }
}
```

**Security:**
- CRITICAL: Use ALLOWED_PATHS restriction
- Never allow root directory access
- Read-only for sensitive directories
- Validate all paths

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem

---

## Search & Research

### 10. Brave Search (`@modelcontextprotocol/server-brave-search`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Web search using Brave Search API

**Tools Provided:**
- `brave_web_search` - Search the web
- `brave_local_search` - Local business search
- `brave_news_search` - News articles

**Use Cases:**
- Market research
- Technology learning
- Competitive analysis
- Documentation discovery
- Trend monitoring

**Installation:**
```bash
npx -y @modelcontextprotocol/server-brave-search
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key"
      }
    }
  }
}
```

**Security:**
- API key required (free tier available)
- Rate limits apply
- Monitor usage costs

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search

---

### 11. Web Fetch (`@modelcontextprotocol/server-fetch`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Fetch content from URLs (HTML, JSON, APIs)

**Tools Provided:**
- `fetch_url` - Fetch URL content
- `fetch_html` - Fetch and parse HTML
- `fetch_json` - Fetch JSON API
- `fetch_with_headers` - Custom headers

**Use Cases:**
- API integration
- Web scraping
- Documentation retrieval
- Data collection
- RSS feed monitoring

**Installation:**
```bash
npx -y @modelcontextprotocol/server-fetch
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"],
      "env": {
        "ALLOWED_DOMAINS": "docs.anthropic.com,github.com,api.company.com"
      }
    }
  }
}
```

**Security:**
- Domain whitelist recommended
- Be aware of rate limits
- Respect robots.txt
- Handle authentication carefully

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/fetch

---

### 12. YouTube Transcript (`@kimtaeyoon83/mcp-server-youtube-transcript`)

**Status:** 🌟 Community (Kim Taeyoon)
**Last Updated:** 2024-11
**Maintenance:** Active

**Purpose:** Extract transcripts from YouTube videos

**Tools Provided:**
- `youtube_get_transcript` - Get video transcript
- `youtube_get_video_info` - Get metadata
- `youtube_search_in_transcript` - Search transcript

**Use Cases:**
- Learning from video tutorials
- Content analysis
- Educational material extraction
- Research documentation
- Tutorial summarization

**Installation:**
```bash
npx -y @kimtaeyoon83/mcp-server-youtube-transcript
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "youtube": {
      "command": "npx",
      "args": ["-y", "@kimtaeyoon83/mcp-server-youtube-transcript"]
    }
  }
}
```

**Security:**
- No API key required
- Respects YouTube terms of service
- Rate limiting built-in

**Documentation:** https://github.com/kimtaeyoon83/mcp-server-youtube-transcript

---

## AI & Memory

### 13. Memory (`@modelcontextprotocol/server-memory`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Persistent memory and context storage across sessions

**Tools Provided:**
- `memory_store` - Store information
- `memory_retrieve` - Retrieve stored info
- `memory_search` - Search memories
- `memory_delete` - Remove memories
- `memory_list` - List all memories

**Use Cases:**
- Customer preferences
- Conversation history
- Learned patterns
- Project context
- User settings
- Knowledge accumulation

**Installation:**
```bash
npx -y @modelcontextprotocol/server-memory
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_STORAGE_PATH": "workspace/.memory/storage.json"
      }
    }
  }
}
```

**Security:**
- Storage file in gitignored directory
- Encrypt sensitive memories
- Regular cleanup of old data
- User privacy considerations

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/memory

---

### 14. Embeddings (`@modelcontextprotocol/server-embeddings`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-11
**Maintenance:** Active

**Purpose:** Generate and search text embeddings for semantic search

**Tools Provided:**
- `embeddings_generate` - Generate embeddings
- `embeddings_search` - Semantic search
- `embeddings_similarity` - Calculate similarity

**Use Cases:**
- Document similarity
- Semantic search
- Content recommendation
- Knowledge base search
- Duplicate detection

**Installation:**
```bash
npx -y @modelcontextprotocol/server-embeddings
```

**Configuration Example:**
```json
{
  "mcpServers": {
    "embeddings": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-embeddings"],
      "env": {
        "ANTHROPIC_API_KEY": "your-api-key"
      }
    }
  }
}
```

**Security:**
- Requires Anthropic API key
- Monitor token usage
- Consider caching embeddings

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/embeddings

---

## Utilities & System

### 15. Time & Date (`@modelcontextprotocol/server-time`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-11
**Maintenance:** Active

**Purpose:** Time and date operations

**Tools Provided:**
- `time_current` - Current time
- `time_convert_timezone` - Timezone conversion
- `time_format` - Format datetime
- `time_calculate` - Date calculations

**Use Cases:**
- Timestamp generation
- Scheduling
- Report dating
- Time tracking
- Deadline calculations

**Installation:**
```bash
npx -y @modelcontextprotocol/server-time
```

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/time

---

### 16. Sequential Thinking (`@modelcontextprotocol/server-sequential-thinking`)

**Status:** ✅ Official (Anthropic)
**Last Updated:** 2024-12
**Maintenance:** Active

**Purpose:** Extended thinking and reasoning capabilities

**Tools Provided:**
- `think_step_by_step` - Break down complex problems
- `analyze_tradeoffs` - Evaluate options
- `plan_approach` - Create execution plans

**Use Cases:**
- Complex problem solving
- Decision making
- Strategic planning
- Risk analysis
- Troubleshooting

**Installation:**
```bash
npx -y @modelcontextprotocol/server-sequential-thinking
```

**Documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/sequential-thinking

---

## Additional Community Servers

### 17. Puppeteer (`@modelcontextprotocol/server-puppeteer`)
- **Purpose:** Browser automation and web scraping
- **Status:** ✅ Official
- **Use Cases:** Dynamic web content, screenshots, PDF generation

### 18. AWS (`@modelcontextprotocol/server-aws`)
- **Purpose:** AWS service integration
- **Status:** ✅ Official
- **Use Cases:** S3, Lambda, DynamoDB, etc.

### 19. Docker (`@modelcontextprotocol/server-docker`)
- **Purpose:** Container management
- **Status:** 🌟 Community
- **Use Cases:** Container orchestration, image management

### 20. Notion (`@makenotion/notion-mcp-server`)
- **Purpose:** Notion API integration
- **Status:** 🌟 Community
- **Use Cases:** Documentation, knowledge base, task management

---

## Evaluation Criteria

When evaluating MCP servers for recommendation, consider:

### 1. Maintenance Status
- ✅ Active: Updated within last 3 months
- ⚠️ Stable: No updates but working
- ❌ Abandoned: No updates for 6+ months

### 2. Source Trust
- ✅ Official (Anthropic)
- 🌟 Community (verified developers)
- ⚠️ Experimental (use with caution)

### 3. Documentation Quality
- ✅ Complete: Examples, API docs, troubleshooting
- ⚠️ Basic: Minimal docs, working examples
- ❌ Poor: Unclear usage

### 4. Security Audit
- ✅ Audited: Security review completed
- ⚠️ Unknown: No public audit
- ❌ Concerns: Known vulnerabilities

### 5. Community Adoption
- ✅ High: 100+ projects using
- ⚠️ Medium: 10-100 projects
- ❌ Low: <10 projects

### 6. Performance
- ✅ Fast: <100ms typical response
- ⚠️ Moderate: 100-500ms
- ❌ Slow: >500ms

### 7. API Costs
- ✅ Free: No API costs
- ⚠️ Paid: External API required
- 💰 Expensive: High cost per operation

---

## Quick Selection Guide

### For BO_KHO Agent (Procurement)
**Recommended:**
1. `@modelcontextprotocol/server-gdrive` (Google Sheets)
2. `@modelcontextprotocol/server-filesystem` (File operations)
3. `@modelcontextprotocol/server-memory` (Customer preferences)

### For BD Agent (Sales)
**Recommended:**
1. `@modelcontextprotocol/server-postgres` (Customer DB)
2. `@modelcontextprotocol/server-slack` (Notifications)
3. `@modelcontextprotocol/server-memory` (Sales context)

### For Learning System
**Recommended:**
1. `@modelcontextprotocol/server-brave-search` (Research)
2. `@kimtaeyoon83/mcp-server-youtube-transcript` (Video learning)
3. `@modelcontextprotocol/server-filesystem` (Content storage)

### For Data Analysis
**Recommended:**
1. `@modelcontextprotocol/server-postgres` or `server-sqlite` (Data storage)
2. `@modelcontextprotocol/server-gdrive` (Google Sheets)
3. `@modelcontextprotocol/server-filesystem` (Report generation)

### For Content Creation
**Recommended:**
1. `@modelcontextprotocol/server-brave-search` (Research)
2. `@modelcontextprotocol/server-github` (Version control)
3. `@modelcontextprotocol/server-filesystem` (Draft management)

---

## Resources

- **Official MCP Registry:** https://github.com/modelcontextprotocol/servers
- **MCP Protocol Docs:** https://modelcontextprotocol.io/
- **Claude Code Docs:** https://docs.claude.com/claude-code
- **Community Servers:** https://github.com/topics/mcp-server

---

**Catalog Maintenance:**
- Review monthly for new servers
- Update status and versions quarterly
- Remove deprecated servers
- Add community-voted servers

**Last Review:** 2025-01-03
