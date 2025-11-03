# Workspace Directory

This is your active learning workspace - temporary materials for current learning sessions, generated study guides, and personal notes.

## Structure

### 📖 `/study-guides/`
Generated study guides and learning paths.

**What's stored here**:
- Complete study guides created by Study Guide Generator
- Learning paths (30-day plans, etc.)
- Module-based learning materials
- Exercise collections

**Example**:
```
study-guides/
├── react-hooks-complete-guide.md
├── typescript-30-day-plan.md
├── docker-beginner-to-advanced.md
└── graphql-study-guide.md
```

### 📝 `/learning-notes/`
Your personal learning notes and annotations.

**What to store here**:
- Notes from current learning session
- Questions and answers
- Code experiments
- "Aha!" moments and insights
- Temporary research materials

**Example**:
```
learning-notes/
├── react/
│   ├── hooks-experiments.md
│   ├── questions-about-useEffect.md
│   └── my-notes-2024-01.md
└── typescript/
    └── type-challenges-solutions.md
```

### ⚡ `/quick-references/`
Cheat sheets and quick reference materials.

**What's stored here**:
- Generated quick references from `/summarize`
- Syntax cheat sheets
- Command references
- Comparison tables
- Decision flowcharts

**Example**:
```
quick-references/
├── react-hooks-cheatsheet.md
├── docker-commands-reference.md
├── typescript-types-quickref.md
└── css-flexbox-grid-comparison.md
```

## Workspace vs Context

| Workspace | Context |
|-----------|---------|
| ✏️ Temporary, current work | 📚 Permanent knowledge base |
| 🚧 Draft materials | ✅ Finalized materials |
| 📝 Personal notes | 📖 Reference documentation |
| 🔄 Changes frequently | 💎 Long-term value |
| 🧪 Experiments | 🎯 Best practices |

## Typical Workflow

1. **Start learning**: Research Agent gathers materials
2. **Active learning**: Take notes in `learning-notes/`
3. **Generate guides**: Study Guide Generator creates in `study-guides/`
4. **Create references**: Use `/summarize` to create `quick-references/`
5. **Review & refine**: Edit and improve materials
6. **Promote to context**: Move finalized materials to `context/` if valuable long-term

## Auto-Updated Inventory

_This section will be automatically updated as files are added to this directory._

**Last updated**: 2024-01-01

### Current Contents:
- **Study Guides**: 0 guides
- **Learning Notes**: 0 notes
- **Quick References**: 0 references

Ready to start learning!

## Usage by Agents

**Study Guide Generator** uses this folder to:
- Save generated study guides
- Store learning path plans
- Create structured learning materials

**You** use this folder to:
- Take notes during learning
- Store generated references
- Organize current learning work

## Best Practices

### Organization
- Create subfolders by technology/topic
- Use dates in filenames for notes: `react-notes-2024-01-15.md`
- Keep related materials together

### File Naming
- Study guides: `[tech]-study-guide.md` or `[tech]-[timeframe]-plan.md`
- Notes: `[tech]-notes-[date].md` or `[topic]-experiments.md`
- References: `[tech]-[topic]-reference.md` or `[tech]-cheatsheet.md`

### Cleanup
- Archive completed study guides periodically
- Move valuable notes to `context/` for permanent storage
- Delete obsolete experiments and drafts
- Keep workspace focused on current learning

### Git Strategy
- **Commit**: Study guides and useful references
- **Don't commit**: Temporary notes and experiments (optional)
- See `.gitignore` for configuration

## Quick Tips

💡 **After finishing a learning session**: Review what you created and decide what to keep vs delete

💡 **Before starting new topic**: Clean up workspace from previous topic

💡 **Found a great study guide?**: Consider sharing it or moving to `context/` for future reference

💡 **Quick references are gold**: Spend time making these good - you'll use them constantly

---

**Remember**: This is your working space. Keep it organized but don't be afraid to experiment and make a mess while learning!
