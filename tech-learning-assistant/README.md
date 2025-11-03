# Tech Learning Assistant

> Your AI-powered system for mastering new technologies efficiently through intelligent research, content extraction, and personalized study guides.

## 🎯 What Is This?

Tech Learning Assistant is a Claude Code AI agent project designed to accelerate your technical learning by:

- 📚 **Gathering** high-quality learning materials from multiple sources
- 🎥 **Extracting** knowledge from video tutorials and courses
- 📝 **Synthesizing** information into structured study guides
- 🗺️ **Creating** personalized learning paths based on your goals

## ✨ Key Features

### 🔍 Research Agent
Automatically finds and evaluates the best learning resources:
- Official documentation and guides
- High-quality tutorials and articles
- Code examples and repositories
- Best practices and common pitfalls

### 🎥 YouTube Transcript Extraction
Capture content from video tutorials without watching hours of content:
- Extract transcripts from courses and talks
- Save to permanent knowledge base or temporary workspace
- Reference specific timestamps
- Build searchable video content library

### 📖 Study Guide Generator
Transform raw materials into actionable learning plans:
- Progressive learning paths (beginner → advanced)
- Practical exercises and projects
- Quick reference sheets and cheat sheets
- Time estimates and milestones

## 🚀 Quick Start

### Example 1: Learning React Hooks

```bash
# Start learning journey
/learn "React Hooks" intermediate

# Research Agent gathers:
# ✓ Official React documentation
# ✓ Top 5 tutorials
# ✓ Best practices articles
# ✓ Video course recommendations

# Extract recommended video
/youtube https://youtube.com/watch?v=xyz context

# Generate study guide
"Create a comprehensive study guide for React Hooks"

# Create quick reference
/summarize "React Hooks"
```

**Result**: Complete learning system with docs, video transcripts, structured study guide, and quick reference - all organized and ready to use.

### Example 2: Quick Concept Deep Dive

```bash
# Research specific concept
"Research useCallback vs useMemo - I'm confused about when to use each"

# Research Agent:
# ✓ Finds 3 excellent explanations
# ✓ Locates comparison articles
# ✓ Identifies best video explanation

# Extract video
/youtube [recommended video URL] workspace

# Get summary
/summarize "useCallback vs useMemo" comparison
```

**Result**: Clear understanding with comparison table, examples, and decision guide.

## 📁 Project Structure

```
tech-learning-assistant/
├── .claude/
│   ├── agents/
│   │   ├── research.md              # 🔍 Finds learning materials
│   │   └── study-guide-generator.md # 📖 Creates study guides
│   └── commands/
│       ├── youtube.md                # 🎥 Extract video transcripts
│       ├── learn.md                  # 🚀 Start learning journey
│       └── summarize.md              # 📄 Create quick references
├── context/
│   ├── research/                     # Permanent learning resources
│   │   └── [technology]/
│   └── transcripts/                  # Video transcript library
│       └── [technology]/
└── workspace/
    ├── study-guides/                 # Generated study materials
    ├── learning-notes/               # Your personal notes
    └── quick-references/             # Cheat sheets
```

## 💡 Why This Demonstrates Research + YouTube Power

### Problem: Learning New Tech is Overwhelming
- Too many resources, don't know which are good
- Video courses take hours to watch
- Hard to organize and retain information
- No personalized learning path

### Solution: Automated Knowledge Gathering & Synthesis

**Research Agent** solves:
- ✅ Finds best resources automatically (saves hours of searching)
- ✅ Evaluates quality and relevance
- ✅ Cross-references multiple sources
- ✅ Identifies best practices and gotchas

**YouTube Command** solves:
- ✅ Extract knowledge from videos without watching
- ✅ Search transcript text (faster than scrubbing video)
- ✅ Reference specific parts quickly
- ✅ Build permanent knowledge base from courses

**Together**: Complete learning system that would take days to build manually.

## 🎓 Real-World Use Cases

### Use Case 1: Job Interview Prep
```
Goal: Master React for upcoming interview

1. /learn "React" intermediate
   → Research Agent finds top interview resources

2. Extract 3 key interview prep videos
   → /youtube [url] context (for each)

3. Generate interview study guide
   → "Create interview prep guide for React"

4. Create quick reference
   → /summarize "React interview questions"

Result: Complete interview prep package in 30 minutes vs 3 days of manual work
```

### Use Case 2: Learning New Framework for Project
```
Goal: Learn Next.js 14 for new project

1. Research official docs and best tutorials
   → Research Agent gathers comprehensive materials

2. Extract official course
   → /youtube [Next.js course] context

3. Generate project-based learning path
   → "Create Next.js study guide with project ideas"

4. As you learn, create references
   → /summarize "Next.js App Router"
   → /summarize "Next.js Server Components"

Result: Structured learning path with all materials organized
```

### Use Case 3: Quick Skill Gap Fill
```
Goal: Understand one specific concept quickly

1. "Research GraphQL subscriptions - I don't understand them"
   → Research Agent finds 3 best explanations

2. /youtube [best explanation video] workspace

3. /summarize "GraphQL subscriptions" quick-ref

Result: Clear understanding in 20 minutes with reference sheet
```

## 🔧 Available Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `/learn [tech] [level]` | Start comprehensive learning journey | `/learn "Docker" beginner` |
| `/youtube [url] [dest]` | Extract video transcript | `/youtube https://... context` |
| `/summarize [topic]` | Create quick reference | `/summarize "TypeScript"` |

## 🤖 Available Agents

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **Research Agent** | Find and evaluate learning materials | Starting new topic, need resources |
| **Study Guide Generator** | Create structured learning paths | Have materials, need organization |

## 📊 Success Metrics

You're learning efficiently when:
- ✅ Can find best resources in minutes, not hours
- ✅ Video knowledge extracted without watching hours of content
- ✅ Clear learning path from beginner to advanced
- ✅ Quick references available for instant lookup
- ✅ All materials organized in one place

## 🎯 Perfect For

- 👨‍💻 **Developers** learning new frameworks and languages
- 🎓 **Students** studying programming concepts
- 💼 **Professionals** preparing for interviews
- 🚀 **Teams** onboarding to new tech stacks
- 📚 **Self-learners** wanting structured learning paths

## 🌟 Why This Project Shows Value

This project perfectly demonstrates why **Research Agent + YouTube Command are essential**:

1. **Research Agent**: Transforms "I want to learn X" into curated, high-quality resource list
2. **YouTube Command**: Turns hours of video content into searchable, referenceable text
3. **Together**: Creates a complete learning system that would take weeks to build manually

Without these components, you'd need to:
- ❌ Manually search and evaluate resources (hours)
- ❌ Watch entire video courses to find key points (days)
- ❌ Take notes and organize materials yourself (tedious)
- ❌ Figure out learning progression (confusing)

With this system:
- ✅ Automated resource discovery (minutes)
- ✅ Instant video knowledge extraction (seconds)
- ✅ Organized, structured learning paths (automatic)
- ✅ Searchable knowledge base (persistent)

## 🚦 Getting Started

1. **Clone this project**
2. **Try the Quick Start example** (React Hooks)
3. **Explore with your own learning goal**
4. **Build your knowledge base** over time

## 📖 Learn More

- [CLAUDE.md](CLAUDE.md) - Full system instructions and workflows
- [.claude/agents/](.claude/agents/) - Agent definitions and capabilities
- [.claude/commands/](.claude/commands/) - Command documentation

---

**Built with**: Claude Code AI Agents
**Philosophy**: Automate knowledge gathering, focus on learning
**Result**: Master new technologies faster than ever before
