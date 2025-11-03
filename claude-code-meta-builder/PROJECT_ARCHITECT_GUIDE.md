# 🏗️ Project Architect - Meta-Agent Creator Guide

> Tự động tạo Claude Code projects từ requirements của bạn

---

## 🎯 Project Architect Là Gì?

**Project Architect** là một meta-agent đặc biệt có khả năng:

1. ✅ **Phân tích** requirements từ nhiều định dạng input
2. ✅ **Thiết kế** optimal project structure
3. ✅ **Tạo tự động** complete Claude Code project
4. ✅ **Customize** based on your specific needs

### Tại Sao Cần Project Architect?

**Vấn đề**: Tạo một Claude Code project từ đầu mất nhiều thời gian
- Phải thiết kế structure
- Phải viết agents
- Phải tạo commands
- Phải document đầy đủ

**Giải pháp**: Project Architect tự động hóa toàn bộ
- ⚡ 5-10 phút thay vì vài giờ
- ✅ Structure theo best practices
- ✅ Complete documentation
- ✅ Ready to use ngay

---

## 🚀 Cách Sử Dụng

### Cách 1: Natural Language Description

```bash
/create-project "Tôi cần một hệ thống quản lý support tickets với ưu tiên và tracking"
```

**Project Architect sẽ**:
1. Hỏi thêm về requirements
2. Tạo blueprint (cho bạn approve)
3. Build complete project với:
   - Ticket analyzer agent
   - Priority manager agent
   - Tracking agent
   - Commands: /new-ticket, /assign, /track
   - Organized structure

---

### Cách 2: From Meeting Notes

```bash
/create-project ./notes/product-meeting.md
```

**File content example**:
```markdown
# Product Meeting - Nov 1, 2024

Pain points:
- Feature requests scattered across email/Slack
- Hard to prioritize
- No visibility for stakeholders

Solution needed:
- Central place for requests
- Voting system
- Auto-prioritization
- Weekly reports
```

**Project Architect sẽ**:
- Đọc và phân tích meeting notes
- Identify: Business Automation + Support System
- Create: Request tracker with voting and reporting

---

### Cách 3: From Business Process

```bash
/create-project ./processes/content-workflow.md
```

**File content**:
```markdown
# Content Creation Workflow

1. Research topic
2. Create outline
3. Write draft
4. SEO optimization
5. Get approval
6. Publish
7. Track performance

Current issues:
- Research manual and slow
- Inconsistent SEO
- No template for outlines
```

**Project Architect sẽ**:
- Map process to pipeline
- Create agent for each step
- Add commands for workflow
- Include templates and standards

---

### Cách 4: Interactive Mode

```bash
/create-project
```

Sau đó trả lời các câu hỏi:
```
What problem are you trying to solve?
→ "Automate our weekly sales reporting"

What data sources do you have?
→ "Salesforce exports, Google Analytics, internal database"

What kind of reports do you need?
→ "Executive summary, team performance, trend analysis"

...
```

**Project Architect sẽ** tạo project phù hợp với từng câu trả lời.

---

## 📝 Input Formats Hỗ Trợ

### 1. Text Description
Mô tả bằng ngôn ngữ tự nhiên về nhu cầu của bạn.

**Example**:
```
"Tôi muốn một hệ thống học TypeScript với:
- Tài liệu từ official docs
- Video tutorials
- Exercises và projects
- Quick reference sheets"
```

→ Tạo **Learning System** cho TypeScript

---

### 2. Meeting Notes/Transcripts
Paste raw notes từ meetings.

**Example**:
```
Meeting with sales team:

Current problem:
- Leads không được follow up đúng hạn
- Mất track của pipeline
- Reports thủ công mỗi tuần

What we need:
- Auto-reminder cho follow-ups
- Pipeline visibility
- Auto-generate reports
- Predict deal closure
```

→ Tạo **Business Automation + Data Analysis** system

---

### 3. Business Process Documents
SOPs, flowcharts, process documentation.

**Example**:
```
Invoice Processing SOP:

1. Receive invoice via email
2. Validate against PO
3. Check budget approval
4. Route to approver
5. Process payment
6. Update accounting system
7. Archive

Pain points:
- Manual routing
- Lost invoices
- Approval delays
```

→ Tạo **Business Automation** với approval workflow

---

### 4. Existing Prompts
Đã có prompt dài cho AI, muốn structure thành project.

**Example**:
```
"You are a sales data analyst. Analyze daily sales reports from
Salesforce, identify trends, calculate KPIs, predict next month
revenue, create executive dashboard, flag anomalies..."
```

→ Tạo **Data Analysis** system với specialized agents

---

### 5. Mixed Information
Combination của nhiều formats.

Có thể paste:
- Notes + requirements
- Process + pain points
- Goals + constraints
- Examples + specifications

Project Architect sẽ extract và organize.

---

## 🎨 Project Types Được Hỗ Trợ

### 1. 🎓 Learning System
**Use when**: Education, training, skill development

**Auto-creates**:
- Research agent
- YouTube transcript extractor
- Study guide generator
- Progress tracker

**Example**: Tech Learning Assistant (đã demo)

---

### 2. 📊 Data Analysis
**Use when**: Data processing, analytics, reporting

**Auto-creates**:
- Data processor
- Statistical analyzer
- Visualization generator
- Report generator

**Example**: Sales Dashboard, Customer Analytics

---

### 3. ✍️ Content Creation
**Use when**: Writing, blogging, marketing

**Auto-creates**:
- Research agent
- Content planner
- Writer/editor
- SEO optimizer
- Publisher

**Example**: Blog Pipeline, Social Media Manager

---

### 4. ⚙️ Business Automation
**Use when**: Workflow automation, task management

**Auto-creates**:
- Task analyzer
- Workflow executor
- Notification agent
- Report generator

**Example**: Approval System, Task Manager

---

### 5. 🎧 Support System
**Use when**: Customer support, help desk, tickets

**Auto-creates**:
- Ticket analyzer
- Knowledge base search
- Response generator
- Escalation handler

**Example**: Support Portal, Bug Tracker

---

### 6. 💻 Code Assistant
**Use when**: Development, code review, documentation

**Auto-creates**:
- Code reviewer
- Documentation generator
- Pattern recognizer
- Test generator

**Example**: Code Review Bot, Doc Generator

---

### 7. 🎨 Custom/Hybrid
**Use when**: Không fit vào template chuẩn

**Approach**: Blend multiple templates + custom agents

**Example**:
- Learning + Automation (Team training platform)
- Data + Content (Data-driven content creation)
- Support + Learning (Self-service with tutorials)

---

## 🔍 Process Workflow

### Phase 1: Requirements Gathering (5-10 min)

**Project Architect sẽ hỏi**:

```
1. PROJECT PURPOSE
   - What problem does this solve?
   - Who are the users?
   - What's the main goal?

2. CORE FUNCTIONS
   - What are the 3-5 main tasks?
   - What inputs will it receive?
   - What outputs should it produce?

3. WORKFLOW
   - What's the typical usage flow?
   - Any recurring patterns?
   - What's automated vs manual?

4. DATA & CONTEXT
   - What information does it need?
   - What's stored permanently?
   - What's temporary?

5. INTEGRATIONS
   - External APIs or tools?
   - File formats to support?
   - Special requirements?

6. SCALE
   - Simple or complex?
   - Single user or team?
   - Frequency of use?
```

**Đừng skip bước này!** Câu trả lời tốt = Project design tốt.

---

### Phase 2: Blueprint Presentation (5 min)

Project Architect tạo và show blueprint:

```markdown
# Project Blueprint: Sales Dashboard

## Project Type
Data Analysis + Business Automation

## Core Purpose
Automate weekly sales reporting with trend analysis and forecasting

## Agents Needed
1. **Data Importer** - Import from Salesforce, GA, internal DB
2. **Trend Analyzer** - Identify patterns and trends
3. **Forecaster** - Predict next month revenue
4. **Report Generator** - Create executive dashboard
5. **Notification Agent** - Send reports to stakeholders

## Commands
1. /import [source] - Import data
2. /analyze [dataset] - Run analysis
3. /forecast [period] - Generate forecast
4. /report [type] - Create report
5. /send [report] [recipients] - Distribute report

## Directory Structure
```
sales-dashboard/
├── context/
│   ├── schemas/
│   └── reference-data/
├── workspace/
│   ├── datasets/
│   ├── analysis/
│   └── reports/
└── tools/
    └── scripts/
```

## Workflow Example
1. Monday: /import all → /analyze → /forecast
2. Generate: /report executive
3. Distribute: /send report stakeholders@company.com
```

**Bạn review và approve hoặc request changes.**

---

### Phase 3: Project Construction (10-20 min)

Once approved, Project Architect tạo:

#### ✅ Complete Directory Structure
```
your-project-name/
├── .claude/
│   ├── settings.json          # Permissions
│   ├── agents/                # Agent definitions
│   │   ├── agent1.md
│   │   ├── agent2.md
│   │   └── ...
│   └── commands/              # Command definitions
│       ├── command1.md
│       ├── command2.md
│       └── ...
├── context/                   # Permanent knowledge
│   ├── README.md
│   └── [project-specific]/
├── workspace/                 # Active work
│   ├── README.md
│   └── [project-specific]/
├── tools/                     # Scripts & SOPs
│   ├── scripts/
│   ├── SOPs/
│   └── README.md
├── CLAUDE.md                  # Main AI instructions
├── README.md                  # Project overview
├── USAGE_GUIDE.md            # Detailed guide
└── .gitignore                # Security
```

#### ✅ CLAUDE.md - Complete Instructions
- Project purpose and context
- Agent descriptions and usage
- Command documentation
- Workflow examples
- Best practices

#### ✅ Agent Files (.claude/agents/*.md)
Mỗi agent có:
- Clear purpose
- Allowed tools
- Responsibilities
- Input/output specs
- Examples
- Best practices
- Success criteria

#### ✅ Command Files (.claude/commands/*.md)
Mỗi command có:
- Usage syntax
- Parameters docs
- Examples
- Implementation guide
- Error handling

#### ✅ Documentation
- README.md - Overview & quick start
- USAGE_GUIDE.md - Detailed instructions
- Context/Workspace READMEs
- .gitignore for security

---

### Phase 4: Delivery & Handoff (5 min)

**Project Tour**:
- Overview of structure
- Key agents explained
- Important commands shown
- Quick start demo

**Next Steps Provided**:
- How to customize
- How to add more agents
- How to extend functionality
- Where to get help

---

## 💡 Real-World Examples

### Example 1: Support Ticket System

**Input**:
```
/create-project "Support team cần tool quản lý tickets.
Nhận 100+ tickets/day qua email và chat. Cần categorize,
prioritize, assign, và track resolution time."
```

**Output**: Complete support system
```
Agents:
- Ticket Analyzer (auto-categorize và prioritize)
- Assignment Agent (route to right person)
- Response Generator (draft replies from KB)
- Tracker (monitor SLA và resolution time)

Commands:
- /new-ticket [description] - Create ticket
- /assign [ticket] [person] - Assign
- /respond [ticket] - Generate response
- /close [ticket] - Mark resolved
- /report [period] - Generate metrics

Structure:
context/knowledge-base/ - Solutions
context/response-templates/ - Templates
workspace/active-tickets/ - Open
workspace/resolved/ - Closed
workspace/reports/ - Metrics
```

---

### Example 2: Content Marketing Pipeline

**Input**: Meeting notes về content workflow

**Output**: Content system
```
Agents:
- Researcher (gather info on topics)
- Planner (content calendar)
- Writer (generate drafts)
- SEO Optimizer (search optimization)
- Publisher (post to blog/social)

Commands:
- /research [topic] - Research topic
- /plan [month] - Create calendar
- /draft [topic] - Write draft
- /optimize [content] - SEO optimize
- /publish [content] [platform] - Publish

Structure:
context/brand-guidelines/ - Voice/style
context/research/ - Topic research
workspace/ideas/ - Content ideas
workspace/drafts/ - WIP
workspace/ready/ - Ready to publish
workspace/published/ - Published
```

---

### Example 3: Data Analysis Dashboard

**Input**:
```
"Phân tích sales data từ Salesforce. Identify trends,
predict revenue, tạo weekly executive reports."
```

**Output**: Analytics system
```
Agents:
- Data Importer (read Salesforce CSV)
- Trend Analyzer (find patterns)
- Revenue Predictor (forecasting)
- Report Generator (executive summaries)
- Insight Extractor (actionable insights)

Commands:
- /import [source] - Import data
- /analyze [dataset] - Run analysis
- /forecast [period] - Predict revenue
- /insights [data] - Extract insights
- /report [type] - Generate report

Structure:
context/schemas/ - Data structures
context/reference-data/ - Benchmarks
workspace/datasets/ - Data files
workspace/analysis/ - Results
workspace/reports/ - Generated reports
workspace/visualizations/ - Charts
```

---

## 🎯 Tips for Best Results

### ✅ DO

**Be Specific**:
```
✓ "Quản lý support tickets với SLA tracking và auto-routing"
✗ "Cần giúp với customers"
```

**Describe Workflow**:
```
✓ Include step-by-step process
✓ Mention pain points
✓ Explain current manual steps
```

**Mention Integrations**:
```
✓ "Export from Salesforce CSV"
✓ "Send notifications via Slack"
✓ "Publish to WordPress API"
```

**Share Context**:
```
✓ Team size (1 person vs 50 people)
✓ Frequency (daily vs monthly)
✓ Data sensitivity (public vs confidential)
```

---

### ❌ DON'T

**Be Vague**:
```
✗ "Làm cái gì đó useful"
✗ "Tool cho team"
```

**Skip Questions**:
```
✗ Không trả lời clarifying questions
→ Answering questions = better project!
```

**Expect Mind Reading**:
```
✗ Assume agent biết exact requirements
→ Provide details!
```

---

## 🔧 Customization After Creation

Project được tạo ra có thể customize:

### Add More Agents
```
"Add một email notification agent vào project này"
```

### Add More Commands
```
"Tạo /export command để export data to CSV"
```

### Modify Structure
```
"Thêm templates/ folder vào workspace"
```

### Add Integrations
```
"Integrate với Slack API để send notifications"
```

### Extend Functionality
```
"Add khả năng schedule automatic reports"
```

---

## ✅ Quality Guarantees

Mọi project được tạo đều có:

### Complete Documentation
- [x] CLAUDE.md với full instructions
- [x] README.md với overview
- [x] USAGE_GUIDE.md với examples
- [x] README trong mọi folder chính

### Working Agents
- [x] Clear purpose và responsibilities
- [x] Documented inputs/outputs
- [x] Example workflows
- [x] Best practices included

### Useful Commands
- [x] Intuitive names
- [x] Documented parameters
- [x] Real examples
- [x] Error handling guidance

### Organized Structure
- [x] Logical folder organization
- [x] Separation of concerns (context vs workspace)
- [x] Scalable architecture
- [x] Easy to extend

### Security
- [x] Appropriate permissions (settings.json)
- [x] .gitignore for sensitive files
- [x] Security best practices documented

---

## 🚀 Getting Started Now

### Step 1: Chuẩn Bị Input

Chọn một trong:
- [ ] Text description của nhu cầu
- [ ] Meeting notes file
- [ ] Business process document
- [ ] Existing prompts/requirements
- [ ] Interactive Q&A mode

### Step 2: Run Command

```bash
# Di chuyển vào claude-code-meta-builder
cd claude-code-meta-builder

# Chạy command
/create-project [your-input]
```

### Step 3: Review Blueprint

- Đọc kỹ blueprint được generate
- Check agents có đúng không
- Verify commands có sense không
- Approve hoặc request changes

### Step 4: Get Your Project

- Project được tạo tự động
- Complete với documentation
- Ready to use ngay
- Có thể customize thêm

---

## 📊 Time Savings

| Task | Manual | With Project Architect | Saved |
|------|--------|----------------------|-------|
| Design structure | 1-2 hours | 5 minutes | 95% |
| Create agents | 2-4 hours | Auto-generated | 100% |
| Write commands | 1-2 hours | Auto-generated | 100% |
| Documentation | 2-3 hours | Auto-generated | 100% |
| Testing & refinement | 2-3 hours | 10-20 minutes | 90% |
| **TOTAL** | **8-14 hours** | **15-30 minutes** | **~95%** |

---

## 🎓 Advanced Usage

### Pattern 1: Iterative Refinement
```
1. Create initial project
2. Use it for a day
3. Request modifications: "Add X agent"
4. Refine based on usage
5. Repeat until perfect
```

### Pattern 2: Template Reuse
```
1. Create great project for use case A
2. Use as template for similar use case B
3. Request: "Create project like X but for Y"
4. Saves even more time
```

### Pattern 3: Team Standardization
```
1. Create company-standard project
2. All teams use same structure
3. Easy knowledge sharing
4. Consistent practices
```

---

## ❓ FAQ

**Q: Tôi có requirements rất specific, có work không?**
A: Yes! Project Architect có thể handle từ simple đến very complex requirements. Càng specific càng tốt.

**Q: Tôi muốn blend nhiều project types?**
A: Hoàn toàn được! Mention requirements từ multiple domains, agent sẽ tạo hybrid project.

**Q: Project không hoàn hảo ngay, phải làm sao?**
A: Normal! Request modifications: "Add X", "Change Y", "Improve Z". Iteration is expected.

**Q: Tôi có thể xem example trước khi tạo?**
A: Yes! Check `tech-learning-assistant/` as reference implementation.

**Q: Time estimate có accurate không?**
A: For simple projects: 15-20 min. Complex: 30-45 min. Still 90%+ faster than manual!

---

## 📚 Resources

**Reference Implementations**:
- `tech-learning-assistant/` - Learning System example
- More examples coming soon

**Templates**:
- `context/templates/PROJECT_TYPES.md` - All project types

**Agent Definition**:
- `.claude/agents/project-architect.md` - Full agent instructions

**Command Documentation**:
- `.claude/commands/create-project.md` - Command details

---

## 🎉 Ready to Create?

Project Architect đang chờ để tạo project cho bạn!

```bash
# Simply run:
/create-project "Describe what you need here..."

# Or interactive:
/create-project

# Or from file:
/create-project ./your-requirements.md
```

**Remember**: Càng nhiều details càng tốt. Project Architect sẽ hỏi clarifying questions để ensure project perfect cho needs của bạn.

**Good luck! 🚀**

---

**Created by**: Claude Code Meta-Builder
**Version**: 1.0.0
**Last Updated**: November 2025
