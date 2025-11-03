# YouTube Tutorial Extractor

Extract transcripts from YouTube tutorial videos and save them to your learning knowledge base. Perfect for capturing content from courses, conference talks, and technical tutorials.

## Usage

```
/youtube <url> [destination]
```

## Parameters

- **url** (required): YouTube video URL
- **destination** (optional): Where to save the transcript
  - `context` - Save to permanent knowledge base (courses, important talks)
  - `workspace` - Save for current learning session (temporary analysis)
  - If omitted, will ask you where to save

## Examples

```bash
# Save a complete course video to permanent knowledge base
/youtube https://www.youtube.com/watch?v=xyz context

# Save tutorial for current learning session
/youtube https://www.youtube.com/watch?v=abc workspace

# Will prompt where to save
/youtube https://www.youtube.com/watch?v=def
```

## When to Use Each Destination

### Context (`context/transcripts/`)
Save here for:
- ✅ Complete course videos you'll reference long-term
- ✅ Conference talks with important concepts
- ✅ Expert explanations of complex topics
- ✅ Official tutorial series
- ✅ Foundational learning materials

**Example**: "React Hooks Complete Course" by official React team

### Workspace (`workspace/learning-notes/`)
Save here for:
- ✅ Videos you're currently analyzing
- ✅ Quick tutorials for specific problems
- ✅ Comparisons and reviews
- ✅ Content you might not need later
- ✅ Experimental learning materials

**Example**: "Quick fix for useState issue" tutorial

## Implementation

This command extracts YouTube transcripts using multiple methods for reliability:

1. **YouTube Transcript API** - Fast, official transcripts
2. **yt-dlp** - Auto-generated subtitles fallback
3. **Direct API** - Additional fallback method

The transcript is saved with:
- Video title and URL
- Timestamps for reference
- Clean formatting with paragraphs
- Metadata (duration, channel, etc.)

## Workflow Integration

### Typical Learning Workflow

1. **Research phase**: Use Research Agent to find good video tutorials
2. **Extract content**: Use `/youtube` command to save transcripts
3. **Synthesize**: Use Study Guide Generator to incorporate video content
4. **Reference**: Transcripts available for future questions and review

### Example Session

```
User: I want to learn React Server Components

Assistant (Research Agent):
- Found official Next.js documentation
- Recommended video: "React Server Components Explained" by Vercel
- Should I extract the transcript?

User: /youtube https://youtube.com/watch?v=... context