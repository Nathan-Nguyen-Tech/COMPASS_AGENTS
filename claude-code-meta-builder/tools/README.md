# Tools Directory

This directory contains utilities, scripts, and standard operating procedures for the Meta Builder system.

## Structure

### `/scripts/`
Executable scripts for automation and utilities:
- **youtube_transcript.py** - YouTube video transcript extraction script (Modified: 2025-09-19)
- **yt_extract.py** - Quick YouTube transcript analysis wrapper (Modified: 2025-09-19)
- **install_youtube_tools.py** - Installation script for YouTube tools dependencies (Modified: 2025-09-19)
- **Various utility scripts** - Additional automation and processing scripts

### `/SOPs/`
Standard Operating Procedures for common tasks:
- **update_readmes.md** - Procedure for updating README files in key directories (Modified: 2025-09-19)

## Purpose

The tools directory provides:

- **Scripts**: Automation tools and utilities for common tasks
- **SOPs**: Standardized procedures for maintaining the system
- **Utilities**: Helper functions and reusable components
- **Automation**: Tools for streamlining repetitive tasks

## Usage

### Scripts
Scripts can be executed directly:
```bash
python tools/scripts/youtube_transcript.py <video_url>
```

### SOPs
Standard Operating Procedures provide step-by-step instructions for:
- System maintenance
- Content management
- Quality assurance
- Documentation updates

## Maintenance

When adding or modifying files in this directory, please update this README following the procedure outlined in `/tools/SOPs/update_readmes.md`.

Scripts should include proper documentation headers with:
- Purpose and functionality
- Usage instructions
- Dependencies
- Examples