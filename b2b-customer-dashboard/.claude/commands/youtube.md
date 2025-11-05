# YouTube Transcript Command

Extract and save transcripts from YouTube videos for research and documentation purposes.

## Usage

```bash
/youtube [video-url] [destination]
```

## Parameters

- `video-url`: YouTube video URL (required)
- `destination`: Where to save transcript
  - `context` - Save to context/ folder (default)
  - `workspace` - Save to workspace/ folder
  - Custom path - Save to specific location

## Examples

### Extract transcript to context folder
```bash
/youtube https://www.youtube.com/watch?v=VIDEO_ID
```

### Extract transcript to workspace
```bash
/youtube https://www.youtube.com/watch?v=VIDEO_ID workspace
```

### Extract to custom path
```bash
/youtube https://www.youtube.com/watch?v=VIDEO_ID context/research/video_transcript.md
```

## What This Command Does

1. **Activates Research Agent**
   - Switches to research agent
   - Agent will handle transcript extraction

2. **Extracts Transcript**
   - Fetches video transcript from YouTube
   - Includes timestamps
   - Preserves formatting

3. **Saves to Destination**
   - Saves transcript as markdown file
   - Includes video metadata (title, channel, date)
   - Updates relevant README if saving to tracked folder

## Use Cases

### Research on Dashboard Best Practices
```bash
/youtube https://www.youtube.com/watch?v=dashboard-design-video context
```

### Learning Plotly.js Techniques
```bash
/youtube https://www.youtube.com/watch?v=plotly-tutorial workspace
```

### Sales Strategy Insights
```bash
/youtube https://www.youtube.com/watch?v=b2b-sales-tips context/research
```

## Output Format

```markdown
# [Video Title]

**Channel**: [Channel Name]
**Published**: [Date]
**URL**: [Video URL]
**Extracted**: [Extraction Date]

---

## Transcript

[00:00] Introduction text here...

[00:15] More content...

[00:30] Continued transcript...

---

## Notes

Add your notes and insights here.
```

## Tips

1. **Choose destination wisely**:
   - `context/` for reference material
   - `workspace/` for active research

2. **Organize by topic**:
   - Create subdirectories for different topics
   - Use descriptive filenames

3. **Add notes**:
   - Edit transcript file after extraction
   - Add key insights and action items

## Related Commands

None - this is a standalone utility command

---

**Extract knowledge from videos with `/youtube`!** 📹
