# README Update Standard Operating Procedure

## Purpose
This SOP ensures that README files in key directories (`/context`, `/workspace`, `/tools`) remain accurate and up-to-date with their contents.

## When to Execute
Update the corresponding README.md whenever you:
- Add new files to `/context`, `/workspace`, or `/tools` directories
- Remove files from these directories
- Significantly modify existing files
- Change the structure or organization of these directories

## Procedure

### Step 1: Review Directory Contents
1. Navigate to the directory requiring README updates
2. List all files and subdirectories
3. Note any new, modified, or removed files since last update

### Step 2: Gather File Information
For each file, collect:
- **Filename** - Exact name with extension
- **Purpose** - Brief description of the file's function or content
- **Last Modified** - Date of last significant change
- **Usage** - How the file is typically used (optional)

### Step 3: Update README Structure
Follow this standard format:

```markdown
# [Directory Name] Directory

Brief description of the directory's purpose.

## Inventory

- **[filename.ext]** - [Brief description] (Modified: YYYY-MM-DD)
- **[filename2.ext]** - [Brief description] (Modified: YYYY-MM-DD)

## Subdirectories (if applicable)

### `/subdirectory/`
Brief description of subdirectory purpose

## Purpose

Explanation of what this directory contains and its role in the system.

## Maintenance

When adding or modifying files in this directory, please update this README following the procedure outlined in `/tools/SOPs/update_readmes.md`.
```

### Step 4: Content Guidelines

#### File Descriptions
- Keep descriptions to 1-2 sentences
- Focus on purpose, not implementation details
- Use active voice when possible
- Be specific but concise

#### Date Format
- Use YYYY-MM-DD format consistently
- Update dates when files are significantly modified
- For new files, use creation date

#### Organization
- List files alphabetically within each section
- Group similar files together when logical
- Separate files from subdirectories

### Step 5: Quality Check
Before saving, verify:
- [ ] All files in directory are listed
- [ ] Descriptions are accurate and helpful
- [ ] Dates are current and correctly formatted
- [ ] Markdown formatting is correct
- [ ] No broken links or references
- [ ] Consistent style and tone

### Step 6: Documentation
After updating, note in your working log:
- Which README was updated
- What changes were made
- Date of update

## Examples

### Good File Entry
```markdown
- **project-creator.md** - Agent specialized in creating new Claude Code projects with optimal structure (Modified: 2025-09-19)
```

### Poor File Entry
```markdown
- **project-creator.md** - does stuff with projects (Modified: sometime)
```

## Special Cases

### New Directories
When creating new subdirectories:
1. Add entry to README under "Subdirectories" section
2. Create README.md in new subdirectory
3. Follow same structure and guidelines

### Large Directories
For directories with many files (>15):
- Group files by type or function
- Consider using subsections
- May list only key files with note about others

### Temporary Files
For `/workspace` specifically:
- Note that contents may be temporary
- Focus on describing types of content rather than specific files
- Update less frequently but ensure structure description remains accurate

## Maintenance Schedule
- **After any file changes**: Update immediately
- **Weekly review**: Check for missed updates
- **Monthly audit**: Comprehensive review of all READMEs

## Automation Considerations
While this SOP is manual, consider future automation for:
- File listing and basic structure
- Date extraction from file metadata
- Template generation for new directories

Remember: READMEs serve as navigation aids and context providers. Keep them accurate, helpful, and current.