# Available Scripts - Quick Reference

## 📋 CRITICAL RULE

**ALWAYS use existing Python scripts before writing new code!**

Scripts are located in: `tools/scripts/`

## ⭐ Active Scripts (Use These)

### 1. calculator.py
**Purpose:** Calculate VTTH (materials) requirements

**Run:**
```bash
python tools/scripts/calculator.py
```

**Output:** `workspace/calculations/vtth_YYYYMMDD_HHMMSS.json`

---

### 2. calculate_chemicals.py
**Purpose:** Calculate chemicals requirements (including QC/CALIB)

**Run:**
```bash
python tools/scripts/calculate_chemicals.py
```

**Output:** `workspace/calculations/hoa_chat_YYYYMMDD_HHMMSS.json`

---

### 3. inventory_comparator.py ⭐
**Purpose:** Compare requirements with current inventory

**Run:**
```bash
python tools/scripts/inventory_comparator.py
```

**Output:** `workspace/calculations/comparison_YYYYMMDD_HHMMSS.json`

**CRITICAL:** Always compare using small units (bottles, pieces, ml)!

---

### 4. create_purchase_order.py ⭐
**Purpose:** Create purchase order in Google Sheets

**Run:**
```bash
python tools/scripts/create_purchase_order.py
```

**Output:** Google Sheet "Phiếu_YYYYMMDD_HHMMSS"

---

### 5. google_sheets_api.py
**Purpose:** API wrapper for Google Sheets operations

**Usage:** Imported by other scripts (not run directly)

---

## ❌ Deprecated Scripts (Do Not Use)

Located in: `tools/scripts/_deprecated/`

- ❌ `inventory_comparison.py` - Use `inventory_comparator.py` instead
- ❌ `purchase_order_creator.py` - Use `create_purchase_order.py` instead
- ❌ `debug_sheet.py` - Dev tool only

---

## 🔄 Complete Workflow

```bash
# Step 1: Calculate
python tools/scripts/calculator.py
# OR
python tools/scripts/calculate_chemicals.py

# Step 2: Compare
python tools/scripts/inventory_comparator.py

# Step 3: Create PO
python tools/scripts/create_purchase_order.py
```

---

## 📖 Full Documentation

See: [tools/SCRIPTS_GUIDE.md](../../tools/SCRIPTS_GUIDE.md)
