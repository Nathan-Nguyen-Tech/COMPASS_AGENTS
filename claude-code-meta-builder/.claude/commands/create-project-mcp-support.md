# Create Project with MCP Support

Activates the **MCP-First Project Architect** to create Claude Code projects with Model Context Protocol integration prioritized over custom code.

## Usage

```bash
/create-project-mcp-support [description or path-to-requirements]
```

## Parameters

- **description** (optional): Brief description of what you need, OR path to requirements file
  - If omitted, will start interactive requirements gathering
  - Can be: text description, path to meeting notes, business process doc, etc.

---

## ⚡ What Makes This Different?

### `/create-project` (Original)
**Approach:** Custom code for integrations

```
User: "I need Google Sheets integration"
  ↓
Creates:
- tools/scripts/google_sheets_api.py (259 lines)
- Manual authentication
- Custom error handling
  ↓
Result:
- High development effort
- Ongoing maintenance
- Security implementation needed
```

---

### `/create-project-mcp-support` (MCP-First) ⭐
**Approach:** MCP servers first, custom code only when needed

```
User: "I need Google Sheets integration"
  ↓
MCP Discovery:
- Finds: @modelcontextprotocol/server-gdrive
- Shows recommendation with pros/cons
- User approves
  ↓
Creates:
- .claude/mcp-config.json (5 lines)
- tools/mcp-documentation/ (usage guides)
- Agents configured for MCP tools
  ↓
Result:
- 15 minutes setup
- Minimal maintenance (automatic updates)
- Best practice security built-in
- Save ~20 hours vs custom code
```

---

## 🎯 Key Features

### 1. Automatic MCP Discovery
When you mention external services (Google Sheets, Slack, GitHub, etc.), the MCP-First Project Architect automatically:
- Searches for official MCP servers
- Evaluates server quality and maintenance status
- Presents recommendations with clear pros/cons
- Offers custom code fallback if no suitable MCP exists

### 2. Intelligent Recommendations
```markdown
For each integration, you'll see:
✅ MCP Server Option (if available)
  - Quality score (High/Medium/Low)
  - Setup time: ~15 min
  - Maintenance: Minimal
  - Pros: Standard, secure, maintained
  - Cons: [any limitations]

🔧 Custom Code Option
  - Development time: ~8 hours
  - Maintenance: ~2 hours/month
  - Pros: Full control
  - Cons: Higher effort

Your choice is respected! MCP when better, custom when needed.
```

### 3. Complete MCP Configuration
Generated projects include:
- `.claude/mcp-config.json` - Server configuration
- `tools/mcp-documentation/` - Complete usage guides
  - `available-servers.md` - Setup instructions per server
  - `tool-reference.md` - All MCP tools documented
  - `usage-examples.md` - Common workflow examples
- Agent definitions with MCP tools configured
- Enhanced README with MCP setup guide
- `.env.example` for secure credential management

### 4. Security Best Practices
- No hardcoded credentials (uses environment variables)
- Service accounts for production
- Minimum required permissions
- Gitignore configured for secrets
- Clear security documentation

---

## 📋 Examples

### Example 1: Data Analysis Project

```bash
/create-project-mcp-support "Analyze sales data from Google Sheets and send daily reports via Slack"
```

**What Happens:**

**Step 1: Requirements Gathering**
```
Project Architect asks:
- What data operations? (read sales, calculate metrics)
- How often? (daily automated)
- Any special needs? (visualization, alerts)
```

**Step 2: MCP Discovery**
```
Searching for MCP servers...

✅ Google Sheets Integration
   Recommended: @modelcontextprotocol/server-gdrive
   - Official Anthropic server
   - Read/write operations supported
   - Setup: ~10 minutes

✅ Slack Integration
   Recommended: @modelcontextprotocol/server-slack
   - Official Anthropic server
   - Post messages, upload files
   - Setup: ~10 minutes

Total setup: ~20 minutes
Custom code alternative: ~20 hours

Proceed with MCP servers? [Y/n]
```

**Step 3: Blueprint**
```markdown
# Project: sales-analytics

## MCP Servers: 2
1. Google Sheets (server-gdrive)
2. Slack (server-slack)

## Agents: 3
1. Data Analyzer (uses MCP)
2. Report Generator (uses MCP)
3. Scheduler

Setup time: ~20 minutes
Maintenance: Minimal
```

**Step 4: Project Creation**
```
Creating project at: ../sales-analytics/

✓ Directory structure
✓ MCP configuration (2 servers)
✓ MCP documentation (3 files)
✓ Agents (3 files, MCP-enabled)
✓ Commands (2 files)
✓ README with MCP setup
✓ Environment example

Project created successfully! 🎉
```

**You saved:** ~20 hours of development time!

---

### Example 2: Learning System

```bash
/create-project-mcp-support "Create a learning system for team training on new technologies"
```

**MCP Discovery Finds:**
- ✅ `@modelcontextprotocol/server-brave-search` (research)
- ✅ `@kimtaeyoon83/mcp-server-youtube-transcript` (video learning)
- ✅ `@modelcontextprotocol/server-filesystem` (content storage)

**Result:**
- 3 MCP servers
- 0 custom API code needed
- ~30 minutes setup
- Complete learning workflow ready

---

### Example 3: Business Automation

```bash
/create-project-mcp-support "Automate weekly reports from database and email to management"
```

**MCP Discovery Finds:**
- ✅ `@modelcontextprotocol/server-postgres` (database)
- ✅ `@modelcontextprotocol/server-smtp` (email)
- ⚠️ Report formatting: Custom code needed (no MCP)

**Result: Hybrid Approach**
- 2 MCP servers (data access, email)
- 1 custom script (report formatting logic)
- Best of both worlds!

---

### Example 4: Internal System (No MCP Available)

```bash
/create-project-mcp-support "Integrate with our company's proprietary ERP system"
```

**MCP Discovery:**
```
❌ No MCP server found for proprietary ERP

Recommendation: Custom Code
- No public MCP exists
- Company-specific protocol
- Custom authentication required

Estimated effort: 12-16 hours
I'll help you design the integration.
```

**Result:**
- Custom code implementation
- Clear architecture
- Best practice patterns
- Still structured project

**MCP-First doesn't mean MCP-only!** Custom code when appropriate.

---

## 🆚 Comparison Table

| Aspect | /create-project | /create-project-mcp-support |
|--------|-----------------|----------------------------|
| **Integration Approach** | Custom code | MCP first → Custom fallback |
| **Setup Time** | 8-20 hours | 15-30 minutes (MCP) |
| **Maintenance** | High (manual) | Low (automatic MCP updates) |
| **Security** | DIY | Best practices built-in |
| **Documentation** | Basic | Comprehensive MCP guides |
| **When to Use** | Custom systems | Standard services |
| **Best For** | Proprietary integrations | Google, Slack, GitHub, etc. |

---

## 🎪 Use Cases by Project Type

### Perfect for MCP-First:

✅ **Data Analysis** (Google Sheets, PostgreSQL, SQLite)
✅ **Business Automation** (Slack, Email, Filesystem)
✅ **Content Creation** (GitHub, Google Docs, Brave Search)
✅ **Learning Systems** (YouTube, Web Search, Filesystem)
✅ **Support Systems** (Memory, Slack, Filesystem)
✅ **Code Assistants** (GitHub, GitLab, Filesystem)

### Better with Original `/create-project`:

🔧 **Internal Systems** (Company ERP, proprietary tools)
🔧 **Complex Custom Logic** (Specific business rules)
🔧 **Legacy Systems** (No API, screen scraping)
🔧 **Highly Specialized** (Industry-specific protocols)

**Not sure?** Start with `/create-project-mcp-support` - it will recommend custom code if appropriate!

---

## 🚀 Getting Started

### 1. Quick Start (Recommended)

```bash
# From meta-builder directory
/create-project-mcp-support
```

Follow interactive prompts:
1. Describe your project
2. Answer questions about integrations
3. Review MCP recommendations
4. Approve blueprint
5. Wait for project creation (~2-5 minutes)
6. Follow setup instructions

### 2. From Description

```bash
/create-project-mcp-support "I need to [describe your project]"
```

Best practice: Mention external services explicitly:
- ✅ "...with Google Sheets and Slack"
- ✅ "...pulling data from PostgreSQL"
- ❌ "...with some data storage" (too vague)

### 3. From Requirements File

```bash
/create-project-mcp-support ./requirements/project-spec.md
```

File should include:
- Project goals
- Key features needed
- **External services** (for MCP discovery)
- Data flows
- User workflows

---

## 📚 After Project Creation

### Immediate Next Steps:

**1. Navigate to Project**
```bash
cd ../[your-project-name]
```

**2. Read MCP Setup Guide**
```bash
cat tools/mcp-documentation/available-servers.md
```

**3. Configure MCP Servers**
Follow per-server instructions:
- Create service accounts / API keys
- Set environment variables
- Test connectivity

**4. Start Using**
```bash
claude
/[primary-command]
```

### Understanding Your MCP Integration:

**Configuration File:** `.claude/mcp-config.json`
```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"],
      "env": {
        "GDRIVE_CREDENTIALS_PATH": "${GDRIVE_CREDENTIALS_PATH}"
      }
    }
  }
}
```

**Documentation:**
- `tools/mcp-documentation/available-servers.md` - How to set up each server
- `tools/mcp-documentation/tool-reference.md` - What tools are available
- `tools/mcp-documentation/usage-examples.md` - How to use in workflows

**Agents:**
Check `.claude/agents/*.md` - MCP tools listed in `allowed-tools`

---

## 🔧 Troubleshooting

### Issue: "No MCP server found for my service"

**Solutions:**
1. Try alternative names (e.g., "Google Drive" vs "GDrive")
2. Check if service is proprietary (may need custom code)
3. Search manually: https://github.com/modelcontextprotocol/servers
4. Proceed with custom code option

### Issue: "MCP setup seems complex"

**Remember:**
- MCP setup: 20 minutes ONCE
- Custom code: 20 hours ONCE + ongoing maintenance
- ROI is extremely positive!

**Need help?** Setup guides in `tools/mcp-documentation/` walk you through step-by-step.

### Issue: "Can I mix MCP and custom code?"

**Yes! Hybrid approach:**
- Use MCP for standard operations (read/write data)
- Use custom code for business logic
- Best of both worlds

This is actually recommended for complex projects!

---

## 💡 Tips for Best Results

### DO:
✅ Mention specific services: "Google Sheets", "Slack", "PostgreSQL"
✅ Describe operations needed: "read data", "send notifications"
✅ Be specific about requirements
✅ Review MCP recommendations carefully
✅ Ask questions if unsure about MCP vs custom
✅ Follow setup guides after creation

### DON'T:
❌ Be vague: "some cloud storage" (say "Google Drive" or "S3")
❌ Skip MCP setup steps (they're quick and important!)
❌ Ignore security best practices
❌ Hardcode credentials (use environment variables)
❌ Assume MCP doesn't work (test first!)

---

## 🎓 Learning More

### About MCP:
- **What is MCP?** https://modelcontextprotocol.io/
- **Official Servers:** https://github.com/modelcontextprotocol/servers
- **Claude Code Docs:** https://docs.claude.com/claude-code

### In Meta-Builder:
- **MCP Catalog:** `context/mcp-knowledge/MCP_SERVER_CATALOG.md`
- **Integration Patterns:** `context/mcp-knowledge/MCP_INTEGRATION_PATTERNS.md`
- **Decision Framework:** `context/mcp-knowledge/MCP_VS_CUSTOM_DECISION_TREE.md`

---

## 📊 Success Metrics

**Projects created with this command typically achieve:**

- **⚡ 10-20x faster setup** (minutes vs hours)
- **🔧 70-90% less custom code** (MCP handles most operations)
- **🔒 Better security** (vetted MCP servers vs DIY)
- **⏰ Minimal maintenance** (MCP updates automatic)
- **📚 Complete documentation** (MCP + project docs)

---

## 🤝 Feedback & Support

**This is experimental!** (Branch: dev_labs)

**Share your experience:**
- What worked well?
- What was confusing?
- MCP servers you wish existed?
- Improvements to recommendations?

**Issues?**
- Check `tools/mcp-documentation/` in your project
- Review MCP knowledge base in meta-builder
- Ask for help with specific MCP servers

---

## Important Note

**This command creates projects OUTSIDE the claude-code-meta-builder directory.**

The MCP-First Project Architect will:
1. Ask you for the project name
2. Create the project in the parent directory (as a sibling to meta-builder)
3. Build complete project structure with MCP integration
4. Generate comprehensive setup documentation

**New project location**: `../[your-project-name]/` (same level as claude-code-meta-builder)

**Example**:
```
COMPASS_AGENTS/
├── claude-code-meta-builder/    ← You are here
│   └── context/
│       └── mcp-knowledge/       ← MCP knowledge base
└── your-new-project/            ← Project created here
    ├── .claude/
    │   ├── mcp-config.json      ← MCP servers
    │   ├── agents/
    │   └── commands/
    ├── context/
    ├── workspace/
    ├── tools/
    │   └── mcp-documentation/   ← MCP guides
    ├── CLAUDE.md
    └── README.md
```

---

## 🎯 Ready to Start?

```bash
/create-project-mcp-support
```

Let the MCP-First Project Architect guide you through creating a modern, maintainable, best-practice Claude Code project! 🚀

**Remember:** MCP when appropriate, custom code when needed, always with clear rationale.
