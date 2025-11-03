# Claude Code Meta-Builder

A comprehensive system for creating and optimizing Claude Code AI agent projects with proper structure, documentation, and functionality.

## Overview

The Meta-Builder is your development environment for creating well-structured Claude Code projects. It provides:

- **Proven project structures** that follow Claude Code best practices
- **Specialized agents** for project creation and research
- **Standard components** that every project should include
- **Documentation tools** for maintaining organized projects
- **Best practices** accumulated from successful implementations

## Quick Start

### Creating a New Project

1. Use the project-creator agent:
   ```bash
   /new-project [project-type] [project-name]
   ```

2. The system will:
   - Ask about your project requirements
   - Create the standard directory structure
   - Include research agent and YouTube command
   - Set up security permissions
   - Generate documentation templates

3. Customize for your specific needs:
   - Modify workspace structure
   - Add domain-specific agents
   - Create custom commands
   - Organize context materials

## 🆕 MCP-First Project Creation (Experimental - Branch: dev_labs)

### Two Approaches to Project Creation

#### `/create-project` (Original)
**Standard approach** - Creates projects with custom code for integrations

**Best for:**
- Proprietary/internal systems
- Highly customized logic
- Full control requirements

#### `/create-project-mcp-support` (MCP-First) ⭐ NEW
**Modern approach** - Prioritizes Model Context Protocol (MCP) servers over custom code

**Best for:**
- Standard services (Google Sheets, Slack, GitHub, etc.)
- Faster development (minutes vs hours)
- Lower maintenance (automatic updates)
- Security best practices built-in

### What is MCP?

Model Context Protocol (MCP) provides standardized integrations for external services:
- **Official servers** maintained by Anthropic
- **Community servers** for popular services
- **No custom code needed** for standard operations
- **Automatic updates** via `npx`

### Example: Google Sheets Integration

**Original Approach (`/create-project`):**
```
Creates: tools/scripts/google_sheets_api.py (259 lines)
- Manual authentication
- Custom error handling
- Ongoing maintenance required
Development time: ~8 hours
Maintenance: ~2 hours/month
```

**MCP-First Approach (`/create-project-mcp-support`):**
```
Creates: .claude/mcp-config.json (5 lines)
- @modelcontextprotocol/server-gdrive
- Automatic authentication
- Best practice security
- Community maintained
Setup time: ~15 minutes
Maintenance: Minimal (auto-updates)
```

**Time saved: ~8 hours development + ongoing maintenance!**

### How It Works

1. **Describe your project:**
   ```bash
   /create-project-mcp-support "Analyze sales data from Google Sheets and send daily reports via Slack"
   ```

2. **MCP Discovery runs automatically:**
   ```
   Searching for MCP servers...
   ✅ Google Sheets → @modelcontextprotocol/server-gdrive
   ✅ Slack → @modelcontextprotocol/server-slack

   Proceed with MCP servers? [Y/n]
   ```

3. **Project generated with MCP integration:**
   ```
   Creates:
   - .claude/mcp-config.json (server configuration)
   - tools/mcp-documentation/ (usage guides)
   - Agents configured for MCP tools
   - Setup instructions
   ```

### MCP Knowledge Base

The meta-builder includes comprehensive MCP documentation:
- **MCP Server Catalog** - 20+ official & community servers
- **Integration Patterns** - Best practices & security
- **Decision Framework** - When to use MCP vs custom code

Location: `context/mcp-knowledge/`

### Supported Integrations

**Data & Storage:**
- Google Sheets/Drive, PostgreSQL, SQLite, Filesystem

**Communication:**
- Slack, Email (SMTP)

**Development:**
- GitHub, GitLab

**Search & Research:**
- Brave Search, YouTube Transcripts, Web Fetch

**AI & Memory:**
- Memory (persistent context), Embeddings

[See full catalog →](context/mcp-knowledge/MCP_SERVER_CATALOG.md)

### When to Use Which?

| Use `/create-project-mcp-support` when: | Use `/create-project` when: |
|----------------------------------------|----------------------------|
| ✅ Standard services (Google, Slack, GitHub) | 🔧 Internal/proprietary systems |
| ✅ Want fast development | 🔧 Highly customized logic |
| ✅ Prefer low maintenance | 🔧 Need full control |
| ✅ Security best practices important | 🔧 No suitable MCP exists |

**Not sure?** Start with `/create-project-mcp-support` - it will recommend custom code when appropriate!

### Try It Now

```bash
# From meta-builder directory
cd claude-code-meta-builder
claude

# Create MCP-first project
/create-project-mcp-support
```

**Note:** This feature is experimental and available on the `dev_labs` branch for testing and feedback.

## Standard Project Structure

Every Claude Code project created includes:

```
[project-name]/
├── CLAUDE.md                    # Main context and instructions
├── README.md                    # Project overview
├── .gitignore                   # Version control exclusions
├── .claude/
│   ├── settings.json           # Permissions and configurations
│   ├── agents/                 # Specialized agents
│   │   ├── research.md         # Research agent (always included)
│   │   └── [custom-agents]
│   └── commands/               # Custom commands
│       ├── youtube.md          # YouTube extraction (always included)
│       └── [custom-commands]
├── context/                    # Knowledge base
│   ├── README.md              # Auto-updating inventory
│   └── transcripts/           # YouTube transcripts for context
├── workspace/                  # Domain-specific work area
│   ├── README.md              # Auto-updating inventory
│   └── [customizable structure]
└── tools/                     # Utilities and procedures
    ├── scripts/               # Executable scripts
    ├── SOPs/                  # Standard Operating Procedures
    │   └── update_readmes.md  # README maintenance procedure
    └── README.md              # Auto-updating inventory
```

## Always-Included Components

### Research Agent
- **Purpose**: Context gathering and multi-source analysis
- **Capabilities**: Reads multiple sources, synthesizes findings, provides research briefs
- **Pattern**: Read many → Analyze → Report concise findings

### YouTube Command
- **Purpose**: Video transcript extraction and analysis
- **Features**: Context vs workspace storage, interactive destination selection
- **Integration**: Works seamlessly with research workflows

### README Maintenance
- **SOP**: Procedure for updating README files in key directories
- **Automation**: Guidelines for keeping documentation current
- **Organization**: Structured approach to file inventory management

## Project Types & Patterns

### Content Creation
- **Use for**: Blogs, marketing, social media, documentation
- **Workspace**: drafts/, published/, ideas/, transcripts/
- **Agents**: Content planner, style enforcer, audience analyzer
- **Commands**: /draft, /review, /publish

### Research & Analysis
- **Use for**: Market research, competitive analysis, academic research
- **Workspace**: sources/, analysis/, reports/, transcripts/
- **Agents**: Data analyst, source validator, report generator
- **Commands**: /gather-sources, /analyze-data, /generate-report

### Code Assistant
- **Use for**: Code review, documentation, development assistance
- **Workspace**: reviews/, snippets/, documentation/, transcripts/
- **Agents**: Code reviewer, documentation generator, pattern recognizer
- **Commands**: /review-code, /generate-docs, /suggest-improvements

### Data Analysis
- **Use for**: Data processing, visualization, reporting
- **Workspace**: datasets/, analysis/, visualizations/, transcripts/
- **Agents**: Statistical analyzer, visualization creator, report generator
- **Commands**: /process-data, /create-visualization, /run-analysis

## Key Features

### 🏗️ **Structured Approach**
- Consistent project organization
- Proven directory structures
- Clear separation of concerns
- Scalable architecture patterns

### 🤖 **Intelligent Agents**
- Research specialist for context gathering
- Project creator for new project setup
- Domain-specific specialists as needed
- Collaborative agent patterns

### 📝 **Documentation First**
- Auto-updating README files
- Maintenance procedures and SOPs
- Clear usage instructions
- Structured knowledge organization

### 🔒 **Security by Default**
- Standard permission configurations
- Sensitive file protection
- Credential security patterns
- Access control best practices

### 🔧 **Extensible Tools**
- YouTube transcript extraction
- Custom command frameworks
- Script organization patterns
- Integration-ready structure

## Meta-Builder Structure

The Meta-Builder itself follows the same structure it creates:

```
Meta Builder/
├── CLAUDE.md                    # Meta-Builder context and instructions
├── README.md                    # This file
├── .gitignore                   # Version control exclusions
├── .claude/
│   ├── settings.json           # Meta-Builder permissions
│   ├── agents/                 # Meta-Builder agents
│   │   ├── project-creator.md  # Creates new Claude Code projects
│   │   └── research.md         # Research specialist template
│   └── commands/               # Meta-Builder commands
│       ├── new-project.md      # Project creation command
│       └── youtube.md          # YouTube extraction command
├── context/                    # Meta-Builder knowledge base
│   ├── README.md              # Knowledge inventory
│   ├── CLAUDE_CODE_PROJECT_GUIDE.md  # Project creation guide
│   ├── BEST_PRACTICES.md      # Proven patterns and practices
│   ├── PATTERNS.md            # Design patterns for projects
│   └── [other knowledge files]
├── workspace/                  # Meta-Builder work area
│   ├── README.md              # Work inventory
│   └── [research and development files]
└── tools/                     # Meta-Builder utilities
    ├── scripts/               # Automation scripts
    │   └── youtube_transcript.py  # YouTube extraction script
    ├── SOPs/                  # Standard procedures
    │   └── update_readmes.md  # README maintenance procedure
    └── README.md              # Tools inventory
```

## Getting Started

### Prerequisites
- Claude Code installed and configured
- Basic understanding of agent and command concepts
- Familiarity with directory structures and documentation

### Setup
1. Clone or download the Meta-Builder
2. Review the project structure and documentation
3. Explore the included agents and commands
4. Read the project creation guide

### First Project
1. Identify your project type and requirements
2. Use `/new-project` to create your first project
3. Customize the generated structure as needed
4. Test agents and commands
5. Begin developing your specific functionality

## Best Practices

### Project Organization
- Follow the standard directory structure
- Keep context and workspace clearly separated
- Use meaningful names for agents and commands
- Maintain documentation currency

### Agent Development
- Focus agents on single, clear purposes
- Provide comprehensive instructions and examples
- Test agent interactions and workflows
- Document capabilities and limitations

### Documentation Maintenance
- Update README files when adding/modifying files
- Follow the SOP for consistent formatting
- Include modification dates and descriptions
- Keep usage instructions current

### Security Considerations
- Use standard permission configurations
- Protect sensitive files and credentials
- Validate scripts and automated workflows
- Document security decisions

## Support & Resources

### Documentation
- `/context/CLAUDE_CODE_PROJECT_GUIDE.md` - Comprehensive project creation guide
- `/context/BEST_PRACTICES.md` - Proven patterns and practices
- `/context/PATTERNS.md` - Design patterns and templates
- `/tools/SOPs/update_readmes.md` - README maintenance procedure

### Getting Help
1. Check the knowledge base in `/context/`
2. Review existing agents and commands for examples
3. Use the research agent to investigate specific questions
4. Consult Claude Code official documentation

### Contributing
- Follow the established structure and patterns
- Document any new approaches or discoveries
- Update knowledge base with lessons learned
- Share successful patterns with the community

## Philosophy

The Meta-Builder embodies the principle of **Structure Over Complexity**:

- **Clear organization** enables effective collaboration
- **Proven patterns** reduce development time and errors
- **Comprehensive documentation** supports long-term maintainability
- **Standardized approaches** facilitate knowledge sharing
- **Extensible design** accommodates diverse use cases

By providing structure, patterns, and tools, the Meta-Builder helps you create Claude Code projects that are not just functional, but maintainable, scalable, and valuable.

---

*Create structured, effective Claude Code projects with confidence.*