# Deprecated Scripts

These scripts are **NO LONGER USED** and have been replaced by newer versions.

**DO NOT USE THESE SCRIPTS!**

## Deprecated Files

### 1. `inventory_comparison.py` - DEPRECATED
**Replaced by:** `inventory_comparator.py`

**Why deprecated:**
- Uses older JSON structure
- Fuzzy matching logic is less reliable
- Not compatible with current workflow
- Missing features present in newer version

**Migration:**
Use `inventory_comparator.py` instead.

---

### 2. `purchase_order_creator.py` - DEPRECATED
**Replaced by:** `create_purchase_order.py`

**Why deprecated:**
- Lacks metadata tracking to "Phiếu Mua Hàng" sheet
- Doesn't save to "Chi Tiết Phiếu Mua Hàng" sheet
- Simpler functionality
- Less comprehensive error handling

**Migration:**
Use `create_purchase_order.py` instead.

---

### 3. `debug_sheet.py` - DEPRECATED
**Status:** Development utility only

**Why deprecated:**
- Was only used during development for debugging
- Not needed in production workflow
- Kept for reference only

**Migration:**
No replacement needed. This was a dev tool only.

---

## Do Not Use

These scripts are kept for historical reference only. They may be deleted in future versions.

**Always use the canonical scripts documented in:** [../SCRIPTS_GUIDE.md](../SCRIPTS_GUIDE.md)
