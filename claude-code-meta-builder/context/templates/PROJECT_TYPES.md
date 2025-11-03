# Claude Code Project Types & Templates

This document defines standard project types and their components for the Project Architect to use when creating new projects.

---

## 🎓 Learning System

### When to Use
- Education and skill development
- Training programs
- Knowledge acquisition
- Tutorial systems
- Study platforms

### Key Signals in Requirements
- Keywords: "learn", "study", "tutorial", "course", "training", "master", "understand"
- Goals: Skill development, knowledge retention, structured learning
- Users: Students, professionals learning new skills, self-learners

### Standard Components

#### Agents
1. **Research Agent** (required)
   - Purpose: Gather high-quality learning materials
   - Tools: Read, Grep, Glob, WebFetch, WebSearch
   - Outputs: Curated resource lists, learning materials

2. **Study Guide Generator** (required)
   - Purpose: Create structured learning paths
   - Tools: Read, Write, Grep, Glob
   - Outputs: Study guides, learning plans, exercises

3. **Quiz Generator** (optional)
   - Purpose: Create practice questions and assessments
   - Tools: Read, Write
   - Outputs: Quizzes, exercises, coding challenges

4. **Progress Tracker** (optional)
   - Purpose: Monitor learning progress
   - Tools: Read, Write
   - Outputs: Progress reports, completion status

#### Commands
- `/learn [topic] [level]` - Start new learning journey
- `/youtube [url] [destination]` - Extract video transcripts
- `/summarize [topic]` - Create quick references
- `/quiz [topic]` - Generate practice questions

#### MCP Servers (Recommended for /create-project-mcp-support)

**Primary Integrations:**

1. **Brave Search** - `@modelcontextprotocol/server-brave-search`
   - Purpose: Research topics, find learning resources
   - Tools: `brave_web_search`, `brave_news_search`
   - Use in: Research Agent
   - Setup: Requires Brave API key (free tier available)

2. **YouTube Transcript** - `@kimtaeyoon83/mcp-server-youtube-transcript`
   - Purpose: Extract video transcripts for learning
   - Tools: `youtube_get_transcript`, `youtube_get_video_info`
   - Use in: YouTube command, Research Agent
   - Setup: No API key required

3. **Filesystem** - `@modelcontextprotocol/server-filesystem`
   - Purpose: Organize learning materials, save progress
   - Tools: `fs_read_file`, `fs_write_file`, `fs_list_directory`
   - Use in: Study Guide Generator, Progress Tracker
   - Setup: Configure allowed paths (context/, workspace/)

**Optional Integrations:**

4. **Memory** - `@modelcontextprotocol/server-memory`
   - Purpose: Remember learning progress, preferences
   - Tools: `memory_store`, `memory_retrieve`, `memory_search`
   - Use in: Progress Tracker
   - Setup: Configure storage path

**Configuration Example:**
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
        "ALLOWED_PATHS": "context/research/,context/transcripts/,workspace/"
      }
    }
  }
}
```

**Benefits:**
- No custom API code needed for research/YouTube
- Standard, maintained integrations
- ~15 min setup vs ~8 hours custom code
- Automatic updates

#### Directory Structure
```
project-name/
├── context/
│   ├── research/           # Permanent learning resources
│   │   └── [topic]/
│   └── transcripts/        # Video transcripts library
│       └── [topic]/
├── workspace/
│   ├── study-guides/       # Generated study materials
│   ├── learning-notes/     # Personal notes
│   ├── quick-references/   # Cheat sheets
│   └── exercises/          # Practice problems
└── tools/
    └── scripts/
        └── youtube_transcript.py
```

### Example Projects
- Tech Learning Assistant (reference implementation)
- Language Learning System
- Professional Certification Prep
- Team Onboarding Platform

---

## 📊 Data Analysis

### When to Use
- Data processing and analysis
- Report generation
- Business intelligence
- Statistical analysis
- Data visualization

### Key Signals in Requirements
- Keywords: "analyze", "data", "report", "insights", "visualize", "metrics", "statistics"
- Goals: Extract insights, generate reports, process data
- Data: CSV files, databases, APIs, spreadsheets

### Standard Components

#### Agents
1. **Data Processor Agent** (required)
   - Purpose: Clean, transform, and prepare data
   - Tools: Read, Write, Bash, Grep
   - Outputs: Cleaned datasets, transformed data

2. **Analysis Agent** (required)
   - Purpose: Perform statistical analysis
   - Tools: Read, Write, Bash
   - Outputs: Analysis results, statistical summaries

3. **Visualization Generator** (required)
   - Purpose: Create charts and visualizations
   - Tools: Read, Write, Bash
   - Outputs: Charts, graphs, dashboards

4. **Report Generator** (required)
   - Purpose: Create formatted reports
   - Tools: Read, Write
   - Outputs: Reports, summaries, presentations

5. **Insight Extractor** (optional)
   - Purpose: Identify patterns and anomalies
   - Tools: Read, Write
   - Outputs: Key insights, recommendations

#### Commands
- `/import [source]` - Import data from source
- `/analyze [dataset]` - Perform analysis
- `/visualize [data] [type]` - Create visualization
- `/report [analysis]` - Generate report
- `/insights [dataset]` - Extract insights

#### MCP Servers (Recommended for /create-project-mcp-support)

**Primary Integrations:**

1. **Google Drive/Sheets** - `@modelcontextprotocol/server-gdrive`
   - Purpose: Read/write data from Google Sheets
   - Tools: `google_sheets_read`, `google_sheets_write`, `google_sheets_create`
   - Use in: Data Processor, Report Generator
   - Setup: Service account JSON key
   - **Replaces:** ~259 lines custom google_sheets_api.py

2. **PostgreSQL** - `@modelcontextprotocol/server-postgres`
   - Purpose: Query and analyze database data
   - Tools: `postgres_query`, `postgres_list_tables`, `postgres_describe_table`
   - Use in: Data Processor, Analysis Agent
   - Setup: Database connection string
   - **Alternative:** SQLite server for local databases

3. **Filesystem** - `@modelcontextprotocol/server-filesystem`
   - Purpose: Read/write CSV, JSON, reports
   - Tools: `fs_read_file`, `fs_write_file`, `fs_list_directory`
   - Use in: All agents
   - Setup: Configure allowed paths

**Configuration Example:**
```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"],
      "env": {
        "GDRIVE_CREDENTIALS_PATH": "config/service-account-key.json"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${POSTGRES_CONNECTION_STRING}"
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

**Benefits:**
- No custom database/sheets code needed
- Standard SQL interface
- ~20 hours saved vs custom implementation
- Production-ready authentication

#### Directory Structure
```
project-name/
├── context/
│   ├── schemas/            # Data schemas and structures
│   ├── reference-data/     # Lookup tables, standards
│   └── methodologies/      # Analysis methods
├── workspace/
│   ├── datasets/           # Input data files
│   │   ├── raw/
│   │   ├── cleaned/
│   │   └── processed/
│   ├── analysis/           # Analysis results
│   ├── visualizations/     # Generated charts
│   └── reports/            # Generated reports
└── tools/
    └── scripts/
        ├── data_cleaner.py
        ├── analyzer.py
        └── visualizer.py
```

### Example Projects
- Sales Analytics Dashboard
- Customer Behavior Analyzer
- Financial Report Generator
- Social Media Metrics Tracker

---

## ✍️ Content Creation

### When to Use
- Blog writing
- Marketing content
- Social media management
- Documentation creation
- Content marketing

### Key Signals in Requirements
- Keywords: "content", "write", "blog", "article", "post", "marketing", "copy", "documentation"
- Goals: Create, edit, publish content
- Outputs: Blog posts, articles, social media content

### Standard Components

#### Agents
1. **Research Agent** (required)
   - Purpose: Research topics and gather information
   - Tools: Read, WebFetch, WebSearch, Grep
   - Outputs: Research briefs, source materials

2. **Content Planner** (required)
   - Purpose: Create content strategies and calendars
   - Tools: Read, Write
   - Outputs: Content calendars, topic outlines

3. **Writer Agent** (required)
   - Purpose: Generate content drafts
   - Tools: Read, Write
   - Outputs: Drafts, articles, posts

4. **Editor Agent** (required)
   - Purpose: Edit and refine content
   - Tools: Read, Write
   - Outputs: Edited content, final versions

5. **SEO Optimizer** (optional)
   - Purpose: Optimize for search engines
   - Tools: Read, Write
   - Outputs: SEO-optimized content

6. **Publisher** (optional)
   - Purpose: Publish to platforms
   - Tools: Bash, WebFetch
   - Outputs: Published content

#### Commands
- `/research [topic]` - Research content topic
- `/plan [timeframe]` - Create content calendar
- `/draft [topic]` - Write content draft
- `/edit [content]` - Edit and refine
- `/optimize [content]` - SEO optimization
- `/publish [content] [platform]` - Publish content

#### MCP Servers (Recommended for /create-project-mcp-support)

**Primary Integrations:**

1. **Brave Search** - `@modelcontextprotocol/server-brave-search`
   - Purpose: Research topics and trends
   - Tools: `brave_web_search`, `brave_news_search`
   - Use in: Research Agent, Content Planner
   - Setup: Brave API key

2. **GitHub** - `@modelcontextprotocol/server-github`
   - Purpose: Version control for content, collaboration
   - Tools: `github_create_file`, `github_create_pull_request`, `github_get_file`
   - Use in: Publisher, Editor
   - Setup: GitHub token
   - **Use case:** Publish to GitHub Pages, manage content repo

3. **Google Drive** - `@modelcontextprotocol/server-gdrive`
   - Purpose: Store drafts, collaborate on Google Docs
   - Tools: `google_docs_read`, `google_docs_write`, `gdrive_list_files`
   - Use in: Writer, Editor
   - Setup: Service account JSON key

**Optional:**

4. **Filesystem** - `@modelcontextprotocol/server-filesystem`
   - Purpose: Local content storage
   - Tools: `fs_read_file`, `fs_write_file`
   - Use in: All agents

**Configuration Example:**
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
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}",
        "GITHUB_OWNER": "your-org"
      }
    }
  }
}
```

**Benefits:**
- No custom publishing code
- Built-in version control
- ~15 hours saved vs custom implementation

#### Directory Structure
```
project-name/
├── context/
│   ├── brand-guidelines/   # Brand voice, style
│   ├── style-guides/       # Writing standards
│   ├── research/           # Topic research
│   └── templates/          # Content templates
├── workspace/
│   ├── ideas/              # Content ideas
│   ├── drafts/             # Work in progress
│   ├── ready/              # Ready to publish
│   ├── published/          # Published content
│   └── content-calendar/   # Schedule and planning
└── tools/
    └── scripts/
        ├── seo_analyzer.py
        └── publisher.py
```

### Example Projects
- Blog Content Pipeline
- Social Media Manager
- Technical Documentation System
- Marketing Campaign Creator

---

## ⚙️ Business Automation

### When to Use
- Workflow automation
- Task management
- Process optimization
- Business operations
- Productivity tools

### Key Signals in Requirements
- Keywords: "automate", "workflow", "process", "task", "manage", "track", "execute"
- Goals: Automate manual work, streamline processes
- Focus: Efficiency, consistency, automation

### Standard Components

#### Agents
1. **Task Analyzer** (required)
   - Purpose: Analyze and categorize tasks
   - Tools: Read, Write, Grep
   - Outputs: Task breakdowns, categorization

2. **Workflow Executor** (required)
   - Purpose: Execute automated workflows
   - Tools: Read, Write, Bash
   - Outputs: Workflow results, completion status

3. **Notification Agent** (optional)
   - Purpose: Send alerts and updates
   - Tools: Bash, WebFetch
   - Outputs: Notifications, reminders

4. **Report Generator** (required)
   - Purpose: Generate status reports
   - Tools: Read, Write
   - Outputs: Progress reports, summaries

5. **Process Optimizer** (optional)
   - Purpose: Identify optimization opportunities
   - Tools: Read, Write
   - Outputs: Optimization suggestions

#### Commands
- `/analyze [process]` - Analyze business process
- `/execute [workflow]` - Run automated workflow
- `/schedule [task] [time]` - Schedule automation
- `/report [period]` - Generate status report
- `/optimize [process]` - Suggest optimizations

#### MCP Servers (Recommended for /create-project-mcp-support)

**Primary Integrations:**

1. **Slack** - `@modelcontextprotocol/server-slack`
   - Purpose: Send notifications, status updates
   - Tools: `slack_post_message`, `slack_upload_file`, `slack_list_channels`
   - Use in: Notification Agent, Report Generator
   - Setup: Slack bot token
   - **Use case:** Automated alerts, workflow completion notifications

2. **Email (SMTP)** - `@modelcontextprotocol/server-smtp`
   - Purpose: Send reports, notifications via email
   - Tools: `smtp_send_email`, `smtp_send_html_email`
   - Use in: Report Generator, Notification Agent
   - Setup: SMTP credentials

3. **Filesystem** - `@modelcontextprotocol/server-filesystem`
   - Purpose: File operations, template management
   - Tools: `fs_read_file`, `fs_write_file`, `fs_move_file`
   - Use in: Task Analyzer, Workflow Executor
   - Setup: Configure allowed paths

**Optional:**

4. **Memory** - `@modelcontextprotocol/server-memory`
   - Purpose: Remember workflow states, preferences
   - Tools: `memory_store`, `memory_retrieve`
   - Use in: Workflow Executor

5. **PostgreSQL/SQLite** - Database for task tracking
   - Use in: Task Analyzer, Report Generator

**Configuration Example:**
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "DEFAULT_CHANNEL": "#automation-alerts"
      }
    },
    "smtp": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-smtp"],
      "env": {
        "SMTP_HOST": "smtp.gmail.com",
        "SMTP_PORT": "587",
        "SMTP_USER": "${SMTP_USER}",
        "SMTP_PASS": "${SMTP_APP_PASSWORD}"
      }
    }
  }
}
```

**Benefits:**
- No custom Slack/email code
- Reliable notification delivery
- ~10 hours saved vs custom implementation
- Production-tested integrations

#### Directory Structure
```
project-name/
├── context/
│   ├── processes/          # Business process docs
│   ├── templates/          # Document templates
│   ├── rules/              # Business rules
│   └── workflows/          # Workflow definitions
├── workspace/
│   ├── active-tasks/       # Current tasks
│   ├── completed/          # Finished tasks
│   ├── scheduled/          # Scheduled tasks
│   └── reports/            # Generated reports
└── tools/
    ├── scripts/
    │   ├── task_executor.py
    │   └── notifier.py
    └── SOPs/
        └── process-documentation.md
```

### Example Projects
- Task Management System
- Report Automation Tool
- Approval Workflow Manager
- Invoice Processing System

---

## 🎧 Support System

### When to Use
- Customer support
- Help desk
- Ticket management
- FAQ systems
- Knowledge bases

### Key Signals in Requirements
- Keywords: "support", "ticket", "customer", "help", "issue", "request", "FAQ"
- Goals: Handle support requests, resolve issues
- Users: Support teams, customers

### Standard Components

#### Agents
1. **Ticket Analyzer** (required)
   - Purpose: Categorize and prioritize tickets
   - Tools: Read, Write, Grep
   - Outputs: Categorized tickets, priority levels

2. **Knowledge Base Search** (required)
   - Purpose: Find relevant solutions
   - Tools: Read, Grep, Glob
   - Outputs: Related articles, solutions

3. **Response Generator** (required)
   - Purpose: Draft responses to tickets
   - Tools: Read, Write
   - Outputs: Response drafts, templates

4. **Escalation Handler** (optional)
   - Purpose: Manage escalations
   - Tools: Read, Write
   - Outputs: Escalation reports, assignments

5. **Satisfaction Tracker** (optional)
   - Purpose: Track customer satisfaction
   - Tools: Read, Write
   - Outputs: CSAT reports, trends

#### Commands
- `/new-ticket [description]` - Create new ticket
- `/analyze [ticket]` - Analyze ticket priority
- `/search [query]` - Search knowledge base
- `/respond [ticket]` - Generate response
- `/escalate [ticket]` - Escalate to manager
- `/report [period]` - Generate support metrics

#### MCP Servers (Recommended for /create-project-mcp-support)

**Primary Integrations:**

1. **Memory** - `@modelcontextprotocol/server-memory`
   - Purpose: Knowledge base storage, ticket history
   - Tools: `memory_store`, `memory_retrieve`, `memory_search`
   - Use in: Knowledge Base Search, Ticket Analyzer
   - Setup: Configure storage path
   - **Use case:** Store support articles, search solutions

2. **Slack** - `@modelcontextprotocol/server-slack`
   - Purpose: Team communication, escalations
   - Tools: `slack_post_message`, `slack_send_dm`
   - Use in: Escalation Handler, Notification Agent
   - Setup: Slack bot token

3. **Filesystem** - `@modelcontextprotocol/server-filesystem`
   - Purpose: Ticket storage, response templates
   - Tools: `fs_read_file`, `fs_write_file`
   - Use in: All agents
   - Setup: Configure allowed paths

**Optional:**

4. **PostgreSQL/SQLite** - Ticket tracking database
   - Purpose: Store ticket data, analytics
   - Use in: Satisfaction Tracker, Report Generator

**Configuration Example:**
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_STORAGE_PATH": "workspace/.memory/support-kb.json"
      }
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
      }
    }
  }
}
```

**Benefits:**
- Persistent knowledge base via Memory server
- No custom Slack integration code
- ~12 hours saved vs custom implementation
- Scalable ticket storage

#### Directory Structure
```
project-name/
├── context/
│   ├── knowledge-base/     # Support articles
│   ├── common-issues/      # Known issues
│   ├── response-templates/ # Response templates
│   └── escalation-rules/   # Escalation criteria
├── workspace/
│   ├── active-tickets/     # Open tickets
│   ├── resolved/           # Closed tickets
│   ├── escalated/          # Escalated issues
│   └── reports/            # Support metrics
└── tools/
    └── scripts/
        └── ticket_analyzer.py
```

### Example Projects
- Customer Support Portal
- IT Help Desk System
- Feature Request Tracker
- Bug Report Manager

---

## 💻 Code Assistant

### When to Use
- Code review
- Documentation generation
- Development assistance
- Code quality
- Technical guidance

### Key Signals in Requirements
- Keywords: "code", "review", "development", "documentation", "refactor", "test", "debug"
- Goals: Improve code quality, generate docs, assist development
- Users: Developers, development teams

### Standard Components

#### Agents
1. **Code Reviewer** (required)
   - Purpose: Review code for quality and issues
   - Tools: Read, Grep, Glob
   - Outputs: Review comments, suggestions

2. **Documentation Generator** (required)
   - Purpose: Generate code documentation
   - Tools: Read, Write, Grep
   - Outputs: API docs, code comments, guides

3. **Pattern Recognizer** (required)
   - Purpose: Identify code patterns and anti-patterns
   - Tools: Read, Grep, Glob
   - Outputs: Pattern analysis, recommendations

4. **Test Generator** (optional)
   - Purpose: Generate unit tests
   - Tools: Read, Write
   - Outputs: Test files, test cases

5. **Refactoring Suggester** (optional)
   - Purpose: Suggest code improvements
   - Tools: Read, Write, Grep
   - Outputs: Refactoring suggestions

#### Commands
- `/review [file or directory]` - Code review
- `/document [file]` - Generate documentation
- `/analyze-patterns [directory]` - Find patterns
- `/generate-tests [file]` - Create tests
- `/suggest-refactoring [file]` - Refactoring ideas

#### MCP Servers (Recommended for /create-project-mcp-support)

**Primary Integrations:**

1. **GitHub** - `@modelcontextprotocol/server-github`
   - Purpose: Repository access, PR reviews, issues
   - Tools: `github_get_file`, `github_create_pull_request`, `github_create_issue`, `github_search_code`
   - Use in: Code Reviewer, Documentation Generator
   - Setup: GitHub token with repo access
   - **Use case:** Automated code reviews, documentation PRs

2. **Filesystem** - `@modelcontextprotocol/server-filesystem`
   - Purpose: Read/write code files, generate docs
   - Tools: `fs_read_file`, `fs_write_file`, `fs_list_directory`
   - Use in: All agents
   - Setup: Configure allowed paths (project directory)

**Optional:**

3. **GitLab** - `@modelcontextprotocol/server-gitlab` (alternative to GitHub)
   - Purpose: GitLab repository operations
   - Use in: Same as GitHub server

**Configuration Example:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}",
        "GITHUB_OWNER": "your-org",
        "GITHUB_REPO": "your-repo"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "${PROJECT_ROOT}"
      }
    }
  }
}
```

**Benefits:**
- Direct GitHub/GitLab integration
- Automated PR creation for documentation
- No custom git wrapper code
- ~8 hours saved vs custom implementation
- Code search across repos

#### Directory Structure
```
project-name/
├── context/
│   ├── coding-standards/   # Style guides, standards
│   ├── patterns/           # Design patterns
│   ├── best-practices/     # Best practices docs
│   └── anti-patterns/      # Common mistakes
├── workspace/
│   ├── reviews/            # Code review results
│   ├── documentation/      # Generated docs
│   ├── test-coverage/      # Test reports
│   └── refactoring-suggestions/
└── tools/
    └── scripts/
        ├── code_analyzer.py
        └── doc_generator.py
```

### Example Projects
- Code Review Assistant
- API Documentation Generator
- Test Coverage Analyzer
- Refactoring Recommender

---

## 🎨 Custom/Hybrid Projects

### When to Use
- Requirements don't fit standard templates
- Need combination of templates
- Unique workflows
- Specialized domains

### Approach

1. **Identify Primary Template** (60-80% fit)
2. **Identify Secondary Templates** (20-40% fit each)
3. **Blend Components** from both templates
4. **Add Custom Agents** for unique requirements
5. **Design Custom Structure** as needed

### Example Hybrids

#### Learning + Business Automation
**Use case**: Team training platform with progress tracking
- Learning agents (research, study guides)
- Automation agents (progress tracking, reporting)
- Blended structure

#### Data Analysis + Content Creation
**Use case**: Data-driven content creation
- Analysis agents (process data, extract insights)
- Content agents (write articles based on data)
- Integrated workflow

#### Support + Learning
**Use case**: Self-service support with tutorials
- Support agents (ticket handling, knowledge base)
- Learning agents (tutorial creation, guides)
- Cross-referenced structure

---

## 📋 Selection Guide for Project Architect

### Decision Tree

```
1. Does it involve learning/education?
   YES → Learning System (potentially + others)
   NO → Continue

2. Does it involve data analysis/reporting?
   YES → Data Analysis (potentially + others)
   NO → Continue

3. Does it involve content creation/writing?
   YES → Content Creation (potentially + others)
   NO → Continue

4. Does it involve workflow/task automation?
   YES → Business Automation (potentially + others)
   NO → Continue

5. Does it involve customer/support tickets?
   YES → Support System (potentially + others)
   NO → Continue

6. Does it involve code/development?
   YES → Code Assistant (potentially + others)
   NO → Continue

7. Multiple categories or none fit perfectly?
   → Custom/Hybrid Project
```

### Keyword Mapping

| Keywords | Primary Template | Notes |
|----------|-----------------|-------|
| learn, study, tutorial, train | Learning System | Education focus |
| analyze, data, report, metrics | Data Analysis | Data processing |
| write, content, blog, post | Content Creation | Content production |
| automate, workflow, task, process | Business Automation | Process optimization |
| support, ticket, customer, help | Support System | Support operations |
| code, review, document, test | Code Assistant | Development help |

### Multi-Template Indicators

If requirements mention items from 2+ templates:
- Identify primary purpose (60%+ of requirements)
- Identify secondary purposes
- Create hybrid project
- Include agents from all relevant templates

---

## 🎯 Quality Standards for All Templates

Every project, regardless of type, must include:

### Documentation
- [ ] CLAUDE.md with complete instructions
- [ ] README.md with overview and quick start
- [ ] USAGE_GUIDE.md with detailed examples
- [ ] README.md in context/ and workspace/

### Agents
- [ ] Clear purpose statement
- [ ] Defined input/output contracts
- [ ] Example workflows
- [ ] Best practices section
- [ ] Success criteria

### Commands
- [ ] Usage documentation
- [ ] Parameter descriptions
- [ ] Multiple examples
- [ ] Implementation guidance

### Structure
- [ ] Logical folder organization
- [ ] Clear separation (context vs workspace)
- [ ] Scalable architecture
- [ ] Extensible design

### Security
- [ ] settings.json with appropriate permissions
- [ ] .gitignore for sensitive files
- [ ] Security best practices documented

---

## 🚀 Next Steps After Template Selection

1. **Customize for specific requirements**
   - Adjust agents for domain
   - Modify commands for workflow
   - Adapt structure for data types

2. **Add domain-specific elements**
   - Industry terminology
   - Specialized tools
   - Custom integrations

3. **Optimize for user**
   - Match user's technical level
   - Consider team size
   - Adapt to frequency of use

4. **Validate design**
   - Review with user
   - Get blueprint approval
   - Iterate if needed

---

This template library ensures consistency while allowing flexibility for Project Architect to create optimal projects for any requirement.
