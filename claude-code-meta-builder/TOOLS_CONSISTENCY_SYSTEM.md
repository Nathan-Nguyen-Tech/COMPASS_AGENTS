# Tools & Scripts Consistency System

## 🎯 Vấn Đề Đã Giải Quyết

### Vấn Đề Trước Đây
Khi user clone project về và chạy agents:
- ❌ Agent tự viết lại code/scripts thay vì dùng tools có sẵn
- ❌ Agent không biết có scripts Python trong tools/scripts/
- ❌ Mỗi lần chạy lại tạo ra code mới, không consistent
- ❌ Workspace đầy code trùng lặp

### Giải Pháp
Hệ thống **Tools & Scripts Consistency** đảm bảo:
- ✅ Agents LUÔN biết về tools/scripts có sẵn
- ✅ Agents LUÔN dùng scripts thay vì tự viết
- ✅ Consistency được baked in ngay từ lúc tạo project
- ✅ User clone về là dùng được ngay

---

## 🏗️ Kiến Trúc Hệ Thống

### 1. Master Guide (Template)
**File:** `context/templates/TOOLS_SCRIPTS_CONSISTENCY_GUIDE.md`

**Nội dung:**
- 📋 Mandatory components cho mọi project
- 🔄 Project creation workflow
- ✅ Checklist chi tiết
- 📝 Templates cho mọi file type
- 🎓 Best practices & anti-patterns

**Vai trò:** Blueprint cho MỌI project mới

---

### 2. Project Creation Agents (Updated)
**Files:**
- `.claude/agents/project-creator.md` - Updated với consistency requirements
- `.claude/agents/project-architect.md` - Updated với consistency requirements

**Changes:**
- ⭐ Added "CRITICAL: Tools & Scripts Consistency" section at top
- 📋 Added mandatory checklist
- 🔄 Updated workflow to create tools docs FIRST
- 📖 Added references to templates and examples

**Vai trò:** Enforce consistency khi tạo projects mới

---

### 3. Quick Reference (For Humans)
**File:** `PROJECT_CREATION_CHECKLIST.md`

**Nội dung:**
- ✅ Copy-paste checklist
- 🚀 Quick start guide
- ⚠️ Common mistakes
- 💡 Pro tips

**Vai trò:** Reference nhanh cho developers

---

### 4. Example Implementation
**Project:** `BO_KHO_MUA_HANG_THEO_TARGET/`

**Demonstrates:**
- ✅ Complete tools/SCRIPTS_GUIDE.md
- ✅ CLAUDE.md with tools section
- ✅ All commands with script references
- ✅ All agents with script instructions
- ✅ context/tools/ documentation

**Vai trò:** Working example để copy from

---

## 📋 Mandatory Components trong Mọi Project

### 1. tools/SCRIPTS_GUIDE.md ⭐
**Purpose:** Master list of ALL scripts

**Structure:**
```markdown
# Scripts Guide
## 🎯 MỤC ĐÍCH
## ⭐ CANONICAL SCRIPTS
## ❌ DEPRECATED SCRIPTS
## 🔄 WORKFLOW
## 📝 BEST PRACTICES
```

**Created:** FIRST, before any other files

---

### 2. CLAUDE.md with Tools Section ⭐
**Purpose:** Agent sees tools immediately when entering project

**Section:**
```markdown
## 🛠️ AVAILABLE TOOLS & SCRIPTS
**⚠️ CRITICAL RULE: PROJECT ĐÃ CÓ SCRIPTS SẴN!**

> LUÔN SỬ DỤNG CÁC SCRIPTS CÓ SẴN!
> KHÔNG TỰ VIẾT LẠI LOGIC!

### ⭐ Canonical Scripts
[Table listing all scripts]

### 🔄 Workflow
[How to use scripts together]
```

**Location:** Right after "MỤC ĐÍCH" section

---

### 3. context/tools/ Directory ⭐
**Purpose:** Additional context about tools for agents

**Files:**
- `available-scripts.md` - Quick reference
- `script-usage-examples.md` - Detailed examples

**Content:** Real-world usage examples and workflows

---

### 4. Command Files with Script References ⭐
**Purpose:** Every command knows which script to use

**Required Section:**
```markdown
## 🛠️ SCRIPT AVAILABLE

**⚠️ CRITICAL: Đã có script Python sẵn!**
**LUÔN SỬ DỤNG SCRIPT CÓ SẴN!**

\`\`\`bash
python tools/scripts/[script_name].py
\`\`\`

📖 [tools/SCRIPTS_GUIDE.md](../tools/SCRIPTS_GUIDE.md)
```

**Location:** Near top of every command file

---

### 5. Agent Files with Script Instructions ⭐
**Purpose:** Agents know HOW to use scripts

**Required Section:**
```markdown
## 🛠️ TOOLS & SCRIPTS

**⚠️ CRITICAL: LUÔN SỬ DỤNG SCRIPT CÓ SẴN!**

### How to Use in Agent
STEP 1: Check if script exists
STEP 2: Run the script (DO NOT reimplement!)
STEP 3: Parse and display results

### ❌ NEVER DO THIS:
- Reimplement logic yourself
- Write new code without checking

### ✅ ALWAYS DO THIS:
- Check tools/scripts/ first
- Use canonical scripts
- Follow script I/O format
```

**Location:** In every agent file

---

## 🔄 Workflow: Creating New Project

### Phase 1: Tools Documentation (DO FIRST!)
```bash
1. Create tools/SCRIPTS_GUIDE.md
2. Create tools/scripts/_deprecated/README.md
3. Create context/tools/available-scripts.md
4. Create context/tools/script-usage-examples.md
```

### Phase 2: CLAUDE.md with Tools
```markdown
# Project Name
## 🎯 MỤC ĐÍCH
[Purpose]

---

## 🛠️ AVAILABLE TOOLS & SCRIPTS
[Full tools section from template]

---

## [Rest of CLAUDE.md]
```

### Phase 3: Commands with Script References
```markdown
# Command: /command-name

## 🛠️ SCRIPT AVAILABLE
[Script reference section]

## [Rest of command]
```

### Phase 4: Agents with Script Instructions
```markdown
## 🛠️ TOOLS & SCRIPTS
[Script instructions section]

## [Rest of agent]
```

### Phase 5: Verification
- [ ] Run through checklist
- [ ] All files have required sections
- [ ] Consistency across all files
- [ ] Links work

---

## ✅ Success Criteria

Project is COMPLETE when:

### Documentation
- [ ] tools/SCRIPTS_GUIDE.md exists
- [ ] context/tools/ docs exist
- [ ] CLAUDE.md has tools section

### Commands
- [ ] ALL commands have script references
- [ ] ALL commands link to SCRIPTS_GUIDE.md
- [ ] ALL commands have warnings

### Agents
- [ ] ALL agents have tools section
- [ ] ALL agents have STEP 1/2/3
- [ ] ALL agents have NEVER/ALWAYS lists

### Consistency
- [ ] Same terminology everywhere
- [ ] Same warnings everywhere
- [ ] All links work

---

## 🎓 How It Works

### For New Projects
1. User runs `/create-project`
2. Project Architect agent reads consistency guide
3. Creates tools docs FIRST
4. Creates CLAUDE.md WITH tools section
5. Creates commands WITH script references
6. Creates agents WITH script instructions
7. Verifies using checklist
8. Delivers complete project

### For Existing Projects (Retrofit)
1. Read `TOOLS_CONSISTENCY_SYSTEM.md` (this file)
2. Follow same steps as new project
3. Add tools docs to existing structure
4. Update CLAUDE.md, commands, agents
5. Verify using checklist

---

## 📖 Files Reference

### Template System Files
```
claude-code-meta-builder/
├── context/templates/
│   └── TOOLS_SCRIPTS_CONSISTENCY_GUIDE.md  # Master guide
├── PROJECT_CREATION_CHECKLIST.md           # Quick reference
├── TOOLS_CONSISTENCY_SYSTEM.md            # This file (overview)
└── .claude/agents/
    ├── project-creator.md                 # Updated
    └── project-architect.md               # Updated
```

### Example Implementation
```
BO_KHO_MUA_HANG_THEO_TARGET/
├── tools/
│   ├── SCRIPTS_GUIDE.md                  # ⭐ Reference this!
│   └── scripts/
│       ├── calculator.py
│       ├── inventory_comparator.py
│       └── _deprecated/
├── context/tools/
│   ├── available-scripts.md              # ⭐ Reference this!
│   └── script-usage-examples.md          # ⭐ Reference this!
├── CLAUDE.md                             # ⭐ Has tools section!
├── .claude/commands/                     # ⭐ All have script refs!
└── .claude/agents/                       # ⭐ All have instructions!
```

---

## 🚀 Quick Start

### For Project Creation Agents
1. Read: `context/templates/TOOLS_SCRIPTS_CONSISTENCY_GUIDE.md`
2. Use: `PROJECT_CREATION_CHECKLIST.md`
3. Copy from: `BO_KHO_MUA_HANG_THEO_TARGET/`

### For Developers
1. Read this file (overview)
2. Check: `PROJECT_CREATION_CHECKLIST.md`
3. Reference: `BO_KHO_MUA_HANG_THEO_TARGET/`

### For Users (Testing)
1. Clone project
2. Run agent
3. Verify agent uses existing scripts (not rewrite)

---

## 💡 Key Insights

### Why This Works
1. **Visibility** - Tools docs in multiple places (CLAUDE.md, commands, agents, context/)
2. **Consistency** - Same warnings everywhere, impossible to miss
3. **Examples** - Real usage examples, not just API docs
4. **Enforcement** - Agents can't complete without checklist items
5. **Templates** - Easy to copy-paste, no thinking required

### Why Previous Approach Failed
1. ❌ Scripts existed but not documented
2. ❌ Commands didn't mention scripts
3. ❌ Agents didn't know to check tools/
4. ❌ No examples of how to use

### Success Metrics
- ✅ Agents check tools/ directory first
- ✅ Agents use existing scripts
- ✅ No duplicate code generation
- ✅ Consistent behavior across machines

---

## 🔧 Maintenance

### Adding New Script to Existing Project
1. Add script to `tools/scripts/`
2. Update `tools/SCRIPTS_GUIDE.md`
3. Update CLAUDE.md tools section
4. Update relevant commands
5. Update relevant agents
6. Add example to `context/tools/script-usage-examples.md`

### Deprecating Old Script
1. Move to `tools/scripts/_deprecated/`
2. Update `_deprecated/README.md` with reason
3. Update `tools/SCRIPTS_GUIDE.md` (move to deprecated section)
4. Update CLAUDE.md (remove from canonical list)
5. Update commands (point to new script)
6. Update agents (point to new script)

---

## 📊 Impact

### Before System
- ❌ Projects had hidden scripts
- ❌ Agents rewrote code every time
- ❌ Inconsistent behavior
- ❌ Wasted time

### After System
- ✅ Scripts visible everywhere
- ✅ Agents use existing code
- ✅ Consistent behavior
- ✅ Time saved

---

## 🎯 Next Steps

### For New Projects
- System is ready to use!
- Just run `/create-project` and agents will follow the guide

### For Existing Projects (Optional)
- Can retrofit using same approach
- Follow checklist to add tools consistency
- Reference BO_KHO as example

---

**Remember: Consistency must be built in from Day 1, not added later!**

**Version:** 1.0.0
**Created:** 2025-01-04
**Author:** Compass Coding Team
**Based on:** BO_KHO_MUA_HANG_THEO_TARGET fixes
