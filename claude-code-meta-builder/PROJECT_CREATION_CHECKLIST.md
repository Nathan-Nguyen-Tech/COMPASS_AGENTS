# Project Creation Checklist - Tools & Scripts Consistency

## 📋 Quick Checklist

Copy this for every new project creation:

```
## Phase 1: Tools Documentation (DO FIRST! ⭐)
- [ ] Create tools/SCRIPTS_GUIDE.md
- [ ] Create tools/scripts/ directory
- [ ] Create tools/scripts/_deprecated/README.md
- [ ] Create context/tools/available-scripts.md
- [ ] Create context/tools/script-usage-examples.md

## Phase 2: CLAUDE.md
- [ ] Add "🛠️ AVAILABLE TOOLS & SCRIPTS" section
- [ ] Add "QUY TẮC BẮT BUỘC" block
- [ ] Add canonical scripts table
- [ ] Add workflow examples
- [ ] Add "Khi Nào Dùng Scripts" section

## Phase 3: Command Files
- [ ] Every command has "🛠️ SCRIPT AVAILABLE" section
- [ ] Every command references specific script
- [ ] Every command links to SCRIPTS_GUIDE.md
- [ ] Every command has "LUÔN SỬ DỤNG SCRIPT" warning

## Phase 4: Agent Files
- [ ] Every agent has "🛠️ TOOLS & SCRIPTS" section
- [ ] Every agent has "Primary Script" subsection
- [ ] Every agent has "How to Use in Agent" (STEP 1/2/3)
- [ ] Every agent has "❌ NEVER DO THIS" list
- [ ] Every agent has "✅ ALWAYS DO THIS" list

## Phase 5: Verification
- [ ] All files exist
- [ ] Terminology consistent everywhere
- [ ] Warnings consistent everywhere
- [ ] All links work
- [ ] No missing sections

## Final Check
- [ ] Read through entire project
- [ ] Verify consistency guide was followed
- [ ] Test example workflows
- [ ] Project is ready for user
```

---

## 🚀 Quick Start for Project Creation Agents

### Step 1: Read Guide
```bash
Read: context/templates/TOOLS_SCRIPTS_CONSISTENCY_GUIDE.md
```

### Step 2: Create Core Files FIRST
```bash
1. tools/SCRIPTS_GUIDE.md (use template)
2. tools/scripts/_deprecated/README.md
3. context/tools/available-scripts.md
4. context/tools/script-usage-examples.md
```

### Step 3: Create CLAUDE.md WITH Tools Section
```markdown
# [Project Name]
## 🎯 MỤC ĐÍCH
[Purpose]

---

## 🛠️ AVAILABLE TOOLS & SCRIPTS
**⚠️ CRITICAL RULE: PROJECT NÀY ĐÃ CÓ SCRIPTS SẴN!**
[Full section from template]

---
```

### Step 4: Create Commands & Agents WITH Script References
Every file must have tools/scripts sections!

### Step 5: Run Checklist
Verify all items checked before delivery.

---

## ⚠️ Common Mistakes to Avoid

### ❌ Mistake 1: Creating project without tools/scripts documentation
**Fix:** ALWAYS create tools/SCRIPTS_GUIDE.md FIRST

### ❌ Mistake 2: Forgetting to add tools section to CLAUDE.md
**Fix:** Use template from consistency guide

### ❌ Mistake 3: Some commands have script references, some don't
**Fix:** ALL commands must have "🛠️ SCRIPT AVAILABLE" section

### ❌ Mistake 4: Agents don't have "How to Use" instructions
**Fix:** ALL agents must have STEP 1/2/3 instructions

### ❌ Mistake 5: No examples
**Fix:** Create script-usage-examples.md with real workflows

---

## 📖 Templates Location

**Master Guide:**
- `context/templates/TOOLS_SCRIPTS_CONSISTENCY_GUIDE.md`

**Example Project:**
- `BO_KHO_MUA_HANG_THEO_TARGET/`

**Quick Copy Templates:**
1. SCRIPTS_GUIDE.md structure
2. Command file with script reference
3. Agent file with script instructions

---

## 🎯 Success Criteria

A project is ONLY complete when:

✅ **Documentation Exists:**
- tools/SCRIPTS_GUIDE.md ✓
- context/tools/available-scripts.md ✓
- context/tools/script-usage-examples.md ✓

✅ **CLAUDE.md Has Tools Section:**
- "AVAILABLE TOOLS & SCRIPTS" present ✓
- QUY TẮC BẮT BUỘC block present ✓
- Canonical scripts table present ✓

✅ **ALL Commands Reference Scripts:**
- Every command has tools section ✓
- Every command links to SCRIPTS_GUIDE.md ✓
- Every command has warnings ✓

✅ **ALL Agents Have Instructions:**
- Every agent has tools section ✓
- Every agent has STEP 1/2/3 ✓
- Every agent has NEVER/ALWAYS lists ✓

✅ **Consistency Verified:**
- Same terminology everywhere ✓
- Same structure everywhere ✓
- All links work ✓

---

## 💡 Pro Tips

1. **Start with tools/SCRIPTS_GUIDE.md** - It's the foundation
2. **Copy from BO_KHO example** - Don't reinvent the wheel
3. **Use same warnings everywhere** - Consistency is key
4. **Include examples** - Show, don't just tell
5. **Test the checklist** - Walk through it yourself

---

**Remember: The goal is to make scripts SO OBVIOUS that agents can't miss them!**
