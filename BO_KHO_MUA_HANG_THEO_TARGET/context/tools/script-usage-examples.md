# Script Usage Examples

## Example 1: Calculate VTTH for 300 customers

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/calculator.py
```

**Interactive prompts:**
```
Nhập số lượng khách: 300
Chọn gói dịch vụ:
1. B2B-Goi dong
2. B2B-Goi co ban
3. B2B-Goi bac
Chọn (1-3): 1
```

**Output:**
- File: `workspace/calculations/vtth_20250104_143022.json`
- Contains: 25 items with calculated quantities

---

## Example 2: Calculate Chemicals for 300 customers

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/calculate_chemicals.py
```

**Interactive prompts:**
```
Nhập số lượng khách: 300
Chọn gói dịch vụ:
1. dong
2. co ban
3. bac
Chọn (1-3): 1
```

**Output:**
- File: `workspace/calculations/hoa_chat_20250104_143530.json`
- Contains: ~21 items with QC/CALIB calculations

---

## Example 3: Compare with Inventory

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/inventory_comparator.py
```

**Interactive prompts:**
```
Chọn file tính toán (VTTH hoặc Hóa Chất):
1. workspace/calculations/vtth_20250104_143022.json
2. workspace/calculations/hoa_chat_20250104_143530.json
Chọn: 1

Nhập đường dẫn file tồn kho (Excel hoặc CSV):
> ton_kho_thang_1.xlsx
```

**Output:**
- File: `workspace/calculations/comparison_20250104_144500.json`
- Contains: `can_mua` and `du_kho` arrays

**Sample Output Structure:**
```json
{
  "so_khach": 300,
  "goi_dv": "B2B-Goi dong",
  "timestamp": "20250104_144500",
  "can_mua": [
    {
      "ten": "Lammen",
      "can_nho": 150,
      "ton_kho_nho": 0,
      "can_mua_nho": 150,
      "can_mua_lon": 2,
      "trang_thai": "HẾT KHO"
    }
  ],
  "du_kho": [...]
}
```

---

## Example 4: Create Purchase Order

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/create_purchase_order.py
```

**Interactive prompts:**
```
Chọn file so sánh:
1. workspace/calculations/comparison_20250104_144500.json
Chọn: 1

Nhập tên người yêu cầu: Nguyen Van A
Nhập nội dung yêu cầu: Mua VTTH cho 300 khách gói đông
```

**Output:**
- Google Sheet: "Phiếu_20250104_145000"
- Metadata saved to "Phiếu Mua Hàng" sheet
- Details saved to "Chi Tiết Phiếu Mua Hàng" sheet
- JSON file: `workspace/purchase_orders/phieu_20250104_145000.json`

---

## Example 5: Full Workflow

```bash
cd BO_KHO_MUA_HANG_THEO_TARGET

# Step 1: Calculate VTTH
python tools/scripts/calculator.py
# Enter: 300 khách, gói đông

# Step 2: Compare with inventory
python tools/scripts/inventory_comparator.py
# Choose: vtth file
# Enter: ton_kho.xlsx

# Step 3: Create purchase order
python tools/scripts/create_purchase_order.py
# Choose: comparison file
# Enter: requester info
```

**Result:** Complete purchase order in Google Sheets ready for review!

---

## Common Use Cases

### Use Case 1: Quick VTTH Calculation
```bash
# For weekly standard orders (300 customers, gói đông)
python tools/scripts/calculator.py
# → 300
# → 1 (gói đông)
```

### Use Case 2: Monthly Chemicals Stock Check
```bash
# Calculate chemicals for monthly forecast
python tools/scripts/calculate_chemicals.py
# → 1200 (300 * 4 weeks)
# → 1 (gói đông)

# Compare with current inventory
python tools/scripts/inventory_comparator.py
# → Choose hoa_chat file
# → Enter monthly inventory file
```

### Use Case 3: Emergency Restock
```bash
# User reports running low on specific items
python tools/scripts/inventory_comparator.py
# → Use latest calculation
# → Enter current inventory snapshot

# Immediately create PO for items needed
python tools/scripts/create_purchase_order.py
```

---

## Tips

### Tip 1: File Naming
Scripts automatically use timestamps for output files:
- `vtth_20250104_143022.json`
- `comparison_20250104_144500.json`
- `Phiếu_20250104_145000`

This prevents overwrites and provides audit trail.

### Tip 2: Inventory File Format
Your inventory Excel/CSV file should have:
- Column "Tên sản phẩm": Product names
- Column "Tồn kho": Current stock (in large units like boxes)
- Header row usually at row 3 (auto-detected)

### Tip 3: Re-running Calculations
You can re-run any step:
```bash
# Re-calculate with different customer count
python tools/scripts/calculator.py

# Re-compare with updated inventory
python tools/scripts/inventory_comparator.py
```

### Tip 4: Checking Outputs
All calculation files are saved in `workspace/calculations/`
```bash
# List all calculations
ls workspace/calculations/

# View latest calculation
cat workspace/calculations/vtth_$(ls -t workspace/calculations/ | grep vtth | head -1)
```

---

## Troubleshooting

### Issue: "File not found"
```bash
# Make sure you're in the right directory
cd BO_KHO_MUA_HANG_THEO_TARGET
pwd  # Should show: .../COMPASS_AGENTS/BO_KHO_MUA_HANG_THEO_TARGET
```

### Issue: "ModuleNotFoundError"
```bash
# Install requirements
pip install -r requirements.txt
```

### Issue: "credentials.json not found"
```bash
# Ensure credentials file exists
ls credentials.json

# If missing, download from Google Cloud Console
```

### Issue: "Sheet not found"
```bash
# Verify spreadsheet ID in scripts
# Should be: 1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800
```

---

## References

- [SCRIPTS_GUIDE.md](../../tools/SCRIPTS_GUIDE.md) - Full documentation
- [available-scripts.md](available-scripts.md) - Quick reference
- [CLAUDE.md](../../CLAUDE.md) - Main instructions
