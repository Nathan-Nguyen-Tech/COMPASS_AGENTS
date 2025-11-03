# Summarize Command

Create concise summaries and quick reference guides from your collected learning materials. Perfect for review sessions and creating cheat sheets.

## Usage

```
/summarize [topic] [format]
```

## Parameters

- **topic** (required): The topic to summarize
  - Can be a technology, concept, or specific feature
  - Examples: "React Hooks", "Docker commands", "TypeScript types"
- **format** (optional): Output format
  - `quick-ref` - Cheat sheet format (default)
  - `summary` - Concise text summary
  - `comparison` - Side-by-side comparison table
  - `flowchart` - Decision tree or workflow

## Examples

```bash
# Create quick reference for React Hooks
/summarize "React Hooks"

# Create summary of all Docker materials
/summarize "Docker" summary

# Compare state management approaches
/summarize "React state management" comparison
```

## What This Command Does

1. **Scans Materials**: Reviews all collected resources for the topic
   - Research materials in `context/research/`
   - Video transcripts in `context/transcripts/`
   - Your notes in `workspace/learning-notes/`

2. **Extracts Key Information**:
   - Core concepts and APIs
   - Common patterns and examples
   - Best practices and gotchas
   - Important syntax and commands

3. **Creates Formatted Output**:
   - Quick reference with code examples
   - Common use cases
   - Decision guides
   - Troubleshooting tips

## Output Formats

### Quick Reference (Default)
```markdown
# [Topic] Quick Reference

## Core Concepts
- [Concept 1]: [Brief explanation]
- [Concept 2]: [Brief explanation]

## Common Operations
\`\`\`javascript
// Most frequent code patterns
\`\`\`

## Gotchas
- ❌ [Common mistake]
- ✅ [Correct approach]
```

### Summary
Concise 1-2 page overview with key takeaways

### Comparison
Side-by-side comparison tables for different approaches

### Flowchart
Decision trees for "when to use what"

## Use Cases

### Quick Review Before Interview
```
/summarize "JavaScript promises" quick-ref
```
Get a one-page cheat sheet of everything important.

### Creating Study Notes
```
/summarize "Vue.js lifecycle" summary
```
Get concise notes from all your research.

### Making Decisions
```
/summarize "CSS frameworks" comparison
```
Get a comparison table to choose the best option.

## Saves To

- `workspace/quick-references/[topic]-reference.md`
- Automatically formatted and ready to use
- Can be printed or kept as digital reference

Remember: This command synthesizes everything you've learned into actionable reference materials!
