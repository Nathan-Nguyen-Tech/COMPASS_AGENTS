# Create Project Command

Activates the Project Architect agent to analyze your requirements and create a custom Claude Code project with optimal structure, agents, and workflows.

## Usage

```bash
/create-project [description or path-to-requirements]
```

## Parameters

- **description** (optional): Brief description of what you need, OR path to requirements file
  - If omitted, will start interactive requirements gathering
  - Can be: text description, path to meeting notes, business process doc, etc.

## Examples

### Example 1: Quick Description
```bash
/create-project "I need a system to manage customer support tickets with priority tracking"
```

### Example 2: From File
```bash
/create-project ./requirements/meeting-notes-2024-11-01.md
```

### Example 3: Interactive Mode
```bash
/create-project
```
Then answer questions about your needs.

---

## Important Note

**This command creates projects OUTSIDE the claude-code-meta-builder directory.**

The Project Architect will:
1. Ask you for the project name
2. Create the project in the parent directory (as a sibling to meta-builder)
3. Build complete project structure with all necessary files

**New project location**: `../[your-project-name]/` (same level as claude-code-meta-builder)

**Example**:
```
COMPASS_AGENTS/
├── claude-code-meta-builder/    ← You are here
└── your-new-project/            ← Project will be created here
    ├── .claude/
    ├── context/
    ├── workspace/
    └── tools/
```

---

## What This Command Does

### Phase 1: Requirements Analysis (5-10 minutes)

1. **Input Processing**
   - Reads your description or file
   - Analyzes content to understand needs
   - Identifies key requirements

2. **Clarification Questions**
   - Asks about project purpose
   - Understands core functions
   - Clarifies workflows
   - Determines data needs
   - Identifies integrations

3. **Project Type Detection**
   - Learning System
   - Data Analysis
   - Content Creation
   - Business Automation
   - Support System
   - Code Assistant
   - Custom hybrid

---

### Phase 2: Blueprint Creation (5 minutes)

Creates detailed project blueprint including:

```markdown
# Project Blueprint

## Project Type
[Identified type]

## Core Purpose
[Clear description]

## Agents Needed
1. Agent Name - Purpose
2. Agent Name - Purpose
...

## Commands
1. /command - What it does
2. /command - What it does
...

## Directory Structure
[Folder organization]

## Typical Workflow
[Step-by-step usage]

## Success Metrics
[How to measure effectiveness]
```

**Shows blueprint to you for approval before building!**

---

### Phase 3: Project Construction (10-20 minutes)

Once you approve blueprint, builds complete project:

#### 3.1 Directory Structure
```
your-project-name/
├── .claude/
│   ├── settings.json
│   ├── agents/
│   │   ├── [agent1].md
│   │   ├── [agent2].md
│   │   └── ...
│   └── commands/
│       ├── [command1].md
│       ├── [command2].md
│       └── ...
├── context/
│   ├── README.md
│   └── [project-specific folders]/
├── workspace/
│   ├── README.md
│   └── [project-specific folders]/
├── tools/
│   ├── scripts/
│   ├── SOPs/
│   └── README.md
├── CLAUDE.md          # Main AI instructions
├── README.md          # Project overview
├── .gitignore
└── USAGE_GUIDE.md     # How to use the project
```

#### 3.2 Generated Files

**CLAUDE.md**:
- Complete project context
- Agent instructions
- Workflow documentation
- Best practices
- Example usage

**Agent Definitions** (`.claude/agents/*.md`):
- Clear purpose and responsibilities
- Input/output specifications
- Example workflows
- Best practices
- Success criteria

**Command Definitions** (`.claude/commands/*.md`):
- Usage instructions
- Parameters documentation
- Examples
- Implementation details

**README.md**:
- Project overview
- Quick start guide
- Key features
- Use cases
- Getting started steps

**USAGE_GUIDE.md**:
- Detailed usage instructions
- Real-world workflows
- Tips and best practices
- Troubleshooting

---

### Phase 4: Delivery & Handoff (5 minutes)

1. **Project Tour**
   - Overview of created files
   - Explanation of structure
   - Key agents and commands

2. **Quick Start Demo**
   - Shows first workflow
   - Demonstrates key command
   - Explains common usage

3. **Next Steps**
   - How to customize
   - How to add more agents
   - How to extend functionality

---

## Input Formats Supported

### 1. Natural Language Description

```bash
/create-project "I want to automate our weekly reporting process. We collect data from 3 sources, analyze trends, and send summary to management."
```

**Project Architect will**:
- Identify: Business Automation + Data Analysis
- Ask about: Data sources, analysis types, report format
- Create: Data collector, Analyzer, Report generator agents

---

### 2. Meeting Notes

```bash
/create-project ./notes/product-meeting-2024-11-01.md
```

**Content example**:
```markdown
# Product Team Meeting - Nov 1, 2024

## Discussed
- Current issue tracking in spreadsheet is messy
- Need better way to prioritize feature requests
- Want customer voting system
- Weekly reports for stakeholders
- Slack integration for notifications

## Decisions
- Build custom system using Claude Code
- Launch in 2 weeks
```

**Project Architect will**:
- Extract requirements from notes
- Identify: Support System + Business Automation
- Design: Request tracker, Voting system, Reporter, Notifier

---

### 3. Business Process Document

```bash
/create-project ./processes/content-workflow.md
```

**Content example**:
```markdown
# Content Creation Process

1. Research topic and keywords
2. Create content outline
3. Write first draft
4. Edit for SEO and clarity
5. Get stakeholder approval
6. Publish to blog
7. Share on social media
8. Track performance

## Pain Points
- Research takes too long
- Outline creation is manual
- SEO optimization is inconsistent
```

**Project Architect will**:
- Map process to agents
- Create: Researcher, Planner, Writer, SEO Editor, Publisher
- Design workflow commands for each step

---

### 4. Existing Prompt/Instructions

```bash
/create-project "Convert this prompt into a project: [long prompt about analyzing sales data...]"
```

**Project Architect will**:
- Analyze prompt's purpose
- Extract required capabilities
- Structure into organized project
- Create specialized agents for each function

---

### 5. Mixed Information

```bash
/create-project
```

Then paste:
```
We need help with our sales team.

Current situation:
- 50 sales reps
- Leads come from 5 sources
- Manual lead scoring
- Lost track of follow-ups
- No visibility into pipeline

What we want:
- Auto-score leads
- Remind reps about follow-ups
- Generate pipeline reports
- Predict deal closure
```

**Project Architect will**:
- Identify: Business Automation + Data Analysis
- Create: Lead scorer, Follow-up tracker, Reporter, Predictor
- Design CRM-like workflow

---

## Project Templates Used

The Project Architect has access to these battle-tested templates:

### 🎓 Learning System Template
**Use when**: Education, skill development, training

**Includes**:
- Research agent
- YouTube transcript extractor
- Study guide generator
- Quiz/exercise creator
- Progress tracker

**Folders**: research/, transcripts/, study-guides/, learning-notes/

---

### 📊 Data Analysis Template
**Use when**: Data processing, analytics, reporting

**Includes**:
- Data processor agent
- Statistical analyzer
- Visualization generator
- Report generator
- Insight extractor

**Folders**: datasets/, analysis/, reports/, visualizations/

---

### ✍️ Content Creation Template
**Use when**: Writing, blogging, marketing

**Includes**:
- Research agent
- Content planner
- Writer/editor
- SEO optimizer
- Publisher

**Folders**: research/, drafts/, published/, ideas/, content-calendar/

---

### ⚙️ Business Automation Template
**Use when**: Workflow automation, task management

**Includes**:
- Task analyzer
- Workflow executor
- Notification agent
- Report generator
- Process optimizer

**Folders**: processes/, templates/, active-tasks/, completed/, reports/

---

### 🎧 Support System Template
**Use when**: Customer support, help desk, FAQs

**Includes**:
- Ticket analyzer
- Knowledge base searcher
- Response generator
- Escalation handler
- Satisfaction tracker

**Folders**: knowledge-base/, tickets/, responses/, analytics/

---

### 💻 Code Assistant Template
**Use when**: Development, code review, documentation

**Includes**:
- Code reviewer
- Documentation generator
- Pattern recognizer
- Test generator
- Refactoring suggester

**Folders**: reviews/, documentation/, patterns/, refactoring-suggestions/

---

## Customization Options

After project creation, you can request:

### Add More Agents
```
"Add an email notification agent to this project"
```

### Add More Commands
```
"Create a /export command that exports data to CSV"
```

### Modify Structure
```
"Add a 'templates/' folder to workspace for reusable content"
```

### Add Integrations
```
"Integrate with Slack for notifications"
```

---

## Quality Guarantees

Every project created includes:

✅ **Complete Documentation**
- CLAUDE.md with full instructions
- README.md with overview
- USAGE_GUIDE.md with examples
- README in every major folder

✅ **Working Agents**
- Clear purpose and responsibilities
- Documented inputs/outputs
- Example workflows
- Best practices

✅ **Useful Commands**
- Intuitive names
- Documented parameters
- Real examples
- Error handling guidance

✅ **Organized Structure**
- Logical folder organization
- Separation of concerns (context vs workspace)
- Scalable architecture
- Ready for growth

✅ **Security**
- Appropriate permissions in settings.json
- .gitignore for sensitive files
- Best practice recommendations

---

## Real-World Examples

### Example 1: Customer Support Ticket System

**Input**:
```
/create-project "Our support team needs a better way to handle customer tickets. We get 100+ tickets/day via email and chat. Need to categorize, prioritize, assign, and track resolution."
```

**Output**: Complete support system with:
- Ticket analyzer agent (categorizes and prioritizes)
- Assignment agent (routes to right team member)
- Response generator (draft replies based on knowledge base)
- Tracker agent (monitors resolution time)
- Commands: /new-ticket, /assign, /respond, /close, /report

---

### Example 2: Content Marketing Pipeline

**Input**: Meeting notes file describing content workflow

**Output**: Content system with:
- Researcher (gathers info on topics)
- Planner (creates content calendar)
- Writer (generates drafts)
- SEO optimizer (improves for search)
- Publisher (posts to blog and social)
- Commands: /research, /plan, /draft, /optimize, /publish

---

### Example 3: Sales Data Analyzer

**Input**:
```
/create-project "Analyze sales data from Salesforce exports. Need to identify trends, predict revenue, and create weekly executive reports."
```

**Output**: Data analysis system with:
- Data importer (reads Salesforce CSV)
- Trend analyzer (finds patterns)
- Revenue predictor (forecasting model)
- Report generator (executive summaries)
- Commands: /import, /analyze, /forecast, /report

---

## Tips for Best Results

### ✅ DO

**Be specific about your needs**:
- "Manage customer support tickets with SLA tracking" ✓
- "I need help with customers" ✗

**Describe your workflow**:
- Include step-by-step processes
- Mention pain points
- Explain current manual steps

**Mention integrations**:
- External tools you use
- APIs you need
- File formats you work with

**Share constraints**:
- Team size
- Frequency of use
- Data sensitivity

### ❌ DON'T

**Be too vague**:
- "Make me something useful" won't work well

**Skip clarifying questions**:
- Answer the questions! They ensure great design

**Expect mind reading**:
- Project Architect is smart but not psychic
- Provide details about your specific needs

---

## Troubleshooting

### "Project doesn't quite fit my needs"

→ Provide more specific requirements
→ Mention what's missing
→ Request customization

### "Too complex for my simple need"

→ Mention you want something simple
→ Specify just core functionality needed
→ Request minimal version

### "Missing a key feature"

→ Easy to add after creation
→ Just request: "Add [feature] to this project"

---

## After Project Creation

### Immediate Next Steps

1. **Explore the project**
   - Read README.md
   - Read CLAUDE.md
   - Check out agent definitions

2. **Try first workflow**
   - Follow Quick Start in README
   - Use the simplest command first
   - Test with sample data

3. **Customize**
   - Adjust agent instructions
   - Modify folder structure
   - Add your specific context

4. **Use it!**
   - Start with real work
   - Gather feedback
   - Iterate and improve

---

## Support

If you need help:
- Check USAGE_GUIDE.md in the project
- Review agent documentation
- Ask for specific customizations
- Request additional examples

---

**Remember**: The Project Architect is designed to create projects you'll actually use. Take time with requirements gathering for best results! 🚀
