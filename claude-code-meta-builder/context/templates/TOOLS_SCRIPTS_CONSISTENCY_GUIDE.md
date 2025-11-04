# Tools & Scripts Consistency Guide for New Projects

## 🎯 MỤC ĐÍCH

Hướng dẫn này đảm bảo **MỌI PROJECT MỚI** đều có consistency về tools/scripts ngay từ đầu.

**⚠️ CRITICAL:** Áp dụng guide này cho TẤT CẢ projects tạo bởi:
- `/create-project`
- `/new-project`
- `/create-project-mcp-support`
- Bất kỳ project creation command nào

---

## 📋 MANDATORY COMPONENTS

Mỗi project MỚI phải có:

### 1. **tools/SCRIPTS_GUIDE.md** ⭐
**Location:** `{project_root}/tools/SCRIPTS_GUIDE.md`

**Template:** [Xem BO_KHO example](../../BO_KHO_MUA_HANG_THEO_TARGET/tools/SCRIPTS_GUIDE.md)

**Nội dung:**
```markdown
# Scripts Guide - Hướng Dẫn Sử Dụng Scripts

## 🎯 MỤC ĐÍCH
Tài liệu này liệt kê TẤT CẢ scripts Python/Shell có sẵn trong project.

**⚠️ QUY TẮC QUAN TRỌNG:**
> LUÔN SỬ DỤNG CÁC SCRIPTS CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!

## ⭐ CANONICAL SCRIPTS (LUÔN DÙNG)
[List canonical scripts here]

## ❌ DEPRECATED SCRIPTS (KHÔNG DÙNG)
[List deprecated scripts if any]

## 🔄 WORKFLOW
[Complete workflow using scripts]

## 📝 BEST PRACTICES
[Best practices for using scripts]
```

---

### 2. **CLAUDE.md with Tools Section** ⭐
**Location:** `{project_root}/CLAUDE.md`

**Thêm section này ngay sau phần MỤC ĐÍCH:**
```markdown
---

## 🛠️ AVAILABLE TOOLS & SCRIPTS

**⚠️ CRITICAL RULE: PROJECT NÀY ĐÃ CÓ SCRIPTS SẴN!**

### 📋 QUY TẮC BẮT BUỘC

> **LUÔN SỬ DỤNG CÁC SCRIPTS CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!**
>
> **KHÔNG BAO GIỜ TỰ VIẾT LẠI LOGIC ĐÃ CÓ TRONG SCRIPTS!**

### 📚 Tài Liệu Scripts

📖 **Xem chi tiết đầy đủ:** [tools/SCRIPTS_GUIDE.md](tools/SCRIPTS_GUIDE.md)

### ⭐ Canonical Scripts (LUÔN DÙNG)

| Script | Mục Đích | Cách Chạy |
|--------|----------|-----------|
| **script1.py** | [Purpose] | `python tools/scripts/script1.py` |
| **script2.py** | [Purpose] | `python tools/scripts/script2.py` |

### 🔄 Workflow Sử Dụng Scripts

\`\`\`bash
# Step 1: [Description]
python tools/scripts/script1.py

# Step 2: [Description]
python tools/scripts/script2.py
\`\`\`

### 💡 Khi Nào Dùng Scripts

**✅ LUÔN LUÔN dùng scripts khi:**
- [Scenario 1]
- [Scenario 2]

**❌ KHÔNG BAO GIỜ:**
- Tự viết lại logic đã có trong scripts
- Bỏ qua scripts và tự implement từ đầu

---
```

---

### 3. **Context Files for Tools** ⭐
**Location:** `{project_root}/context/tools/`

**Required files:**
- `available-scripts.md` - Quick reference
- `script-usage-examples.md` - Detailed examples

**Template:**

**a) available-scripts.md:**
```markdown
# Available Scripts - Quick Reference

## 📋 CRITICAL RULE
**ALWAYS use existing scripts before writing new code!**

## ⭐ Active Scripts

### 1. script_name.py
**Purpose:** [Description]
**Run:** `python tools/scripts/script_name.py`
**Output:** [Output description]

---

## 📖 Full Documentation
See: [tools/SCRIPTS_GUIDE.md](../../tools/SCRIPTS_GUIDE.md)
```

**b) script-usage-examples.md:**
```markdown
# Script Usage Examples

## Example 1: [Task Name]

\`\`\`bash
cd {PROJECT_ROOT}
python tools/scripts/script_name.py
\`\`\`

**Interactive prompts:**
\`\`\`
[Prompt 1]: [Input]
[Prompt 2]: [Input]
\`\`\`

**Output:**
- File: `workspace/output/file_YYYYMMDD.json`
- Contains: [Description]

---

## Example 2: Complete Workflow
[Step by step workflow]
```

---

### 4. **Command Files with Script References** ⭐
**Location:** `{project_root}/.claude/commands/*.md`

**Every command file MUST include:**
```markdown
# Command: /command-name

[Description]

## 🛠️ SCRIPT AVAILABLE

**⚠️ CRITICAL: Đã có script Python sẵn để chạy command này!**

**LUÔN SỬ DỤNG SCRIPT CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!**

\`\`\`bash
cd {PROJECT_ROOT}
python tools/scripts/[script_name].py
\`\`\`

📖 **Chi tiết:** [tools/SCRIPTS_GUIDE.md](../tools/SCRIPTS_GUIDE.md#section)

## Mô Tả
[Rest of command documentation]
```

---

### 5. **Agent Definitions with Script Instructions** ⭐
**Location:** `{project_root}/.claude/agents/*.md`

**Every agent file MUST include:**
```markdown
## 🛠️ TOOLS & SCRIPTS

**⚠️ CRITICAL: LUÔN SỬ DỤNG SCRIPT CÓ SẴN!**

### Primary Script

**script_name.py** - Canonical script cho [task]

**Cách chạy:**
\`\`\`bash
cd {PROJECT_ROOT}
python tools/scripts/script_name.py
\`\`\`

**Input:** [Input description]
**Output:** [Output description]

### How to Use in Agent

**STEP 1: Always check if script exists**
\`\`\`bash
ls tools/scripts/script_name.py
\`\`\`

**STEP 2: Run the script (DO NOT reimplement!)**
\`\`\`bash
python tools/scripts/script_name.py
\`\`\`

**STEP 3: Parse and display results**
\`\`\`python
import json
with open('workspace/output/file.json') as f:
    results = json.load(f)
    # Display results to user
\`\`\`

### ❌ NEVER DO THIS:
- ❌ Reimplement [task] logic yourself
- ❌ Write new [task] code without checking for existing scripts first

### ✅ ALWAYS DO THIS:
- ✅ Check tools/scripts/ directory first
- ✅ Use script_name.py for [task]
- ✅ Follow the script's input/output format
```

---

### 6. **tools/scripts/_deprecated/ Directory** ⭐
**Location:** `{project_root}/tools/scripts/_deprecated/`

**Purpose:** Archive old scripts to avoid confusion

**Required file:**
```markdown
# Deprecated Scripts

These scripts are **NO LONGER USED** and have been replaced.

**DO NOT USE THESE SCRIPTS!**

## Deprecated Files
[List with reasons and replacements]
```

---

## 🔄 PROJECT CREATION WORKFLOW

### Phase 1: Initial Setup (Project Architect Agent)

```markdown
1. Ask user for project requirements
2. Design project structure
3. **CREATE tools/SCRIPTS_GUIDE.md FIRST**
4. Create CLAUDE.md WITH tools section
5. Create context/tools/ documentation
6. Create .claude/commands/ WITH script references
7. Create .claude/agents/ WITH script instructions
```

### Phase 2: Script Development (If Applicable)

```markdown
1. Implement scripts in tools/scripts/
2. Update SCRIPTS_GUIDE.md with new scripts
3. Update CLAUDE.md tools section
4. Update context/tools/available-scripts.md
5. Add examples to script-usage-examples.md
6. Update relevant command files
7. Update relevant agent files
```

### Phase 3: Documentation Review

```markdown
1. Verify SCRIPTS_GUIDE.md is complete
2. Verify CLAUDE.md has tools section
3. Verify all commands reference scripts
4. Verify all agents have script instructions
5. Verify context/tools/ is complete
```

---

## ✅ CHECKLIST FOR NEW PROJECTS

Copy this checklist when creating new projects:

### Documentation Files
- [ ] `tools/SCRIPTS_GUIDE.md` exists and is complete
- [ ] `CLAUDE.md` has "AVAILABLE TOOLS & SCRIPTS" section
- [ ] `context/tools/available-scripts.md` exists
- [ ] `context/tools/script-usage-examples.md` exists
- [ ] `tools/scripts/_deprecated/README.md` exists (if applicable)

### Command Files
- [ ] All command files have "🛠️ SCRIPT AVAILABLE" section
- [ ] All commands reference specific scripts
- [ ] All commands link to SCRIPTS_GUIDE.md

### Agent Files
- [ ] All agent files have "🛠️ TOOLS & SCRIPTS" section
- [ ] All agents have "How to Use in Agent" instructions
- [ ] All agents have "❌ NEVER DO THIS" warnings
- [ ] All agents have "✅ ALWAYS DO THIS" guidelines

### Scripts Organization
- [ ] Canonical scripts clearly identified
- [ ] Deprecated scripts archived (if any)
- [ ] Script naming is consistent
- [ ] Script purposes are documented

### Consistency
- [ ] Same terminology used across all files
- [ ] Same script references across all files
- [ ] Same warnings and guidelines everywhere
- [ ] Links between files are correct

---

## 📝 TEMPLATES

### Template 1: SCRIPTS_GUIDE.md Structure

```markdown
# Scripts Guide - [Project Name]

## 🎯 MỤC ĐÍCH
[Purpose]

**⚠️ QUY TẮC QUAN TRỌNG:**
> LUÔN SỬ DỤNG CÁC SCRIPTS CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!

## ⭐ CANONICAL SCRIPTS

### 1. script1.py
**Mục đích:** [Purpose]
**Cách chạy:** `python tools/scripts/script1.py`
**Output:** [Output]

---

## ❌ DEPRECATED SCRIPTS
[List if any]

---

## 🔄 WORKFLOW HOÀN CHỈNH
[Complete workflow]

---

## 📝 BEST PRACTICES
[Best practices]
```

### Template 2: Command File with Script Reference

```markdown
# Command: /command-name

[Description]

## 🛠️ SCRIPT AVAILABLE

**⚠️ CRITICAL: Đã có script Python sẵn!**

\`\`\`bash
python tools/scripts/script_name.py
\`\`\`

📖 [tools/SCRIPTS_GUIDE.md](../tools/SCRIPTS_GUIDE.md)

## [Rest of documentation]
```

### Template 3: Agent File with Script Instructions

```markdown
## 🛠️ TOOLS & SCRIPTS

**⚠️ CRITICAL: LUÔN SỬ DỤNG SCRIPT CÓ SẴN!**

### Primary Script: script_name.py
**Cách chạy:** `python tools/scripts/script_name.py`

### How to Use
STEP 1: Check script exists
STEP 2: Run script
STEP 3: Parse results

### ❌ NEVER: [List]
### ✅ ALWAYS: [List]
```

---

## 🎓 BEST PRACTICES

### 1. Script Discovery
- **Make scripts VISIBLE** - Document everywhere
- **Make scripts OBVIOUS** - Clear names and purposes
- **Make scripts EASY** - Simple commands to run

### 2. Script Naming
- **Descriptive names**: `calculate_vtth.py` not `calc.py`
- **Consistent naming**: Use underscores, not hyphens
- **Canonical suffix**: Mark canonical as `*_canonical.py` if needed

### 3. Script Organization
- **One script per task**: Don't create monolithic scripts
- **Clear dependencies**: Document what imports what
- **Archive old versions**: Move to _deprecated/, don't delete

### 4. Documentation
- **Document BEFORE coding**: Write SCRIPTS_GUIDE.md first
- **Document EVERYWHERE**: CLAUDE.md, commands, agents, context
- **Document EXAMPLES**: Real use cases, not just syntax

### 5. Consistency
- **Same warnings everywhere**: Copy-paste is OK for consistency
- **Same terminology**: "canonical" vs "preferred" - pick one
- **Same structure**: All agent files have same sections

---

## 🚫 ANTI-PATTERNS TO AVOID

### ❌ Anti-Pattern 1: Hidden Scripts
**Problem:** Scripts exist but agents don't know about them

**Solution:** Document in SCRIPTS_GUIDE.md + CLAUDE.md + commands + agents

---

### ❌ Anti-Pattern 2: Ambiguous Scripts
**Problem:** Multiple scripts do similar things, unclear which to use

**Solution:** Mark ONE as canonical, archive others in _deprecated/

---

### ❌ Anti-Pattern 3: No Examples
**Problem:** Scripts documented but no usage examples

**Solution:** Create script-usage-examples.md with real workflows

---

### ❌ Anti-Pattern 4: Inconsistent References
**Problem:** Some commands mention scripts, some don't

**Solution:** Use checklist to verify ALL commands/agents updated

---

### ❌ Anti-Pattern 5: Missing "How To"
**Problem:** Scripts listed but no instructions on when/how to use

**Solution:** Add "How to Use in Agent" section with STEP 1/2/3

---

## 📖 REFERENCES

### Example Projects
- **BO_KHO_MUA_HANG_THEO_TARGET** - Perfect example of scripts consistency
  - [tools/SCRIPTS_GUIDE.md](../../BO_KHO_MUA_HANG_THEO_TARGET/tools/SCRIPTS_GUIDE.md)
  - [CLAUDE.md](../../BO_KHO_MUA_HANG_THEO_TARGET/CLAUDE.md) (with tools section)
  - [.claude/commands/](../../BO_KHO_MUA_HANG_THEO_TARGET/.claude/commands/)
  - [.claude/agents/](../../BO_KHO_MUA_HANG_THEO_TARGET/.claude/agents/)

### Templates
- This file serves as the master template
- Copy sections as needed for new projects

---

## 🔄 VERSION HISTORY

**Version:** 1.0.0
**Created:** 2025-01-04
**Based on:** BO_KHO_MUA_HANG_THEO_TARGET fixes
**Author:** Compass Coding Team

---

**Remember: Scripts consistency MUST be built in from Day 1, not added later!**
