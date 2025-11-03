# YouTube Transcript Extractor

Extract transcripts and analyze content from YouTube videos using multiple robust methods.

## Usage

```
/youtube <url> [destination] [format]
```

## Parameters

- **url** (required): YouTube video URL
- **destination** (optional): Storage location - `context`, `workspace`, or `prompt` (asks user)
- **format** (optional): Output format - `text`, `json`, `markdown`, or `save`

## Examples

```bash
# Save to context for permanent agent knowledge
/youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ context

# Save to workspace for temporary analysis
/youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ workspace

# Prompt user to choose destination
/youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ

# Get different output formats
/youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ context json
/youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ workspace markdown

# Legacy format support (defaults to workspace)
/youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ save
```

## Implementation

When this command is called, run the YouTube transcript extraction system:

```python
import subprocess
import sys
from pathlib import Path

def execute_youtube_command(url, destination="prompt", format_type="save"):
    """Execute YouTube transcript extraction with destination choice"""

    # Get project root directory
    project_root = Path.cwd()

    # Handle destination choice
    if destination == "prompt" or not destination:
        print("📥 Where should this transcript be saved?")
        print("1. context - For permanent agent knowledge")
        print("2. workspace - For temporary analysis")
        choice = input("Choose (1/2): ").strip()
        destination = "context" if choice == "1" else "workspace"

    # Set up paths based on destination
    if destination == "context":
        transcript_dir = project_root / "context" / "transcripts"
        print(f"💾 Saving to context for permanent agent knowledge...")
    else:  # workspace
        transcript_dir = project_root / "workspace" / "transcripts"
        print(f"💾 Saving to workspace for temporary analysis...")

    # Ensure transcript directory exists
    transcript_dir.mkdir(parents=True, exist_ok=True)

    # Use appropriate script
    if format_type == "save" or destination in ["context", "workspace"]:
        # Use full script to save files
        script_path = project_root / "tools" / "scripts" / "youtube_transcript.py"
        cmd = [sys.executable, str(script_path), url, str(transcript_dir)]
    else:
        # Use wrapper for other formats
        script_path = project_root / "tools" / "scripts" / "yt_extract.py"
        cmd = [sys.executable, str(script_path), url, format_type]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=project_root)

        if result.returncode == 0:
            print(result.stdout)
            if destination == "context":
                print("\n📚 Transcript saved to context - agent will have access to this knowledge.")
            else:
                print("\n🚧 Transcript saved to workspace - available for current analysis.")
        else:
            print(f"❌ Error: {result.stderr}")

    except Exception as e:
        print(f"❌ Failed to execute: {e}")

# Parse command arguments
if len(sys.argv) >= 2:
    url = sys.argv[1]
    destination = sys.argv[2] if len(sys.argv) > 2 else "prompt"
    format_type = sys.argv[3] if len(sys.argv) > 3 else "save"

    # Handle legacy format where second argument was format
    if destination in ["text", "json", "markdown", "save"]:
        format_type = destination
        destination = "workspace"  # default to workspace for legacy calls

    execute_youtube_command(url, destination, format_type)
else:
    print("🎥 YouTube Transcript Extractor")
    print("\nUsage: /youtube <url> [destination] [format]")
    print("\nDestinations:")
    print("  context   - Save to context for permanent agent knowledge")
    print("  workspace - Save to workspace for temporary analysis")
    print("  prompt    - Ask user where to save (default)")
    print("\nFormats:")
    print("  save     - Save to file with metadata (default)")
    print("  text     - Clean text output only")
    print("  json     - Full JSON data")
    print("  markdown - Formatted markdown")
```

## Methods Used

This command uses a robust multi-method approach:

1. **youtube-transcript-api** - Official transcripts (fastest)
2. **yt-dlp** - Auto-generated subtitles (most reliable)
3. **Gemini API** - AI analysis with visual context (requires API key)
4. **Direct API** - Fallback for difficult videos

## Features

- ✅ **Multiple extraction methods** with automatic fallbacks
- ✅ **Clean text formatting** with paragraph breaks
- ✅ **Comprehensive metadata** including video title and timestamps
- ✅ **File saving** with organized naming and logging
- ✅ **Error handling** with helpful troubleshooting messages

## Requirements

Run installation script first:
```bash
python scripts/install_youtube_tools.py
```

## Optional: Gemini API Setup

For enhanced video analysis with visual context:
1. Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Set environment variable: `export GEMINI_API_KEY=your_key_here`

## Storage Locations

### Context Storage (`/context/transcripts/`)
Use for:
- Videos that provide permanent knowledge for the agent
- Educational content that informs agent capabilities
- Reference material that should persist across sessions
- Domain expertise and learning materials

### Workspace Storage (`/workspace/transcripts/`)
Use for:
- Videos being analyzed for current projects
- Temporary research and analysis tasks
- Content being processed or transformed
- Work-in-progress analysis and insights

## Notes

- Works with most YouTube videos that have captions
- Automatically handles different video types and restrictions
- Creates transcript directories automatically if they don't exist
- Supports both permanent context and temporary workspace storage
- Maintains backward compatibility with legacy format calls
- Script paths updated to use `/tools/scripts/` directory structure