# Learn Command

Start a comprehensive learning journey for a new technology or concept. This command initiates research, sets up your workspace, and creates a personalized learning path.

## Usage

```
/learn [technology] [level]
```

## Parameters

- **technology** (required): The technology, framework, or concept you want to learn
  - Examples: "React", "TypeScript", "Docker", "GraphQL"
- **level** (optional): Your current skill level
  - `beginner` - New to this technology
  - `intermediate` - Have some experience
  - `advanced` - Want to master advanced topics
  - If omitted, will assess your level through questions

## Examples

```bash
# Start learning React from scratch
/learn "React" beginner

# Learn TypeScript at intermediate level
/learn "TypeScript" intermediate

# Learn Next.js (will ask about your level)
/learn "Next.js"
```

## What This Command Does

### 1. Discovery Phase
- Activates Research Agent to gather materials
- Finds official documentation
- Locates best tutorials and courses
- Identifies video content to extract
- Collects best practices and gotchas

### 2. Workspace Setup
Creates organized structure:
```
context/research/[technology]/     # Permanent resources
context/transcripts/[technology]/  # Video transcripts
workspace/study-guides/[technology]/ # Your study materials
workspace/learning-notes/[technology]/ # Your notes
```

### 3. Learning Path Creation
- Assesses your goals and timeline
- Activates Study Guide Generator
- Creates personalized study plan
- Designs exercises and projects
- Sets up milestone checkpoints

### 4. Resource Collection
- Asks which videos to extract transcripts from
- Downloads code examples if needed
- Sets up quick reference materials
- Prepares exercise templates

## Workflow Example

```
User: /learn "React Hooks" intermediate