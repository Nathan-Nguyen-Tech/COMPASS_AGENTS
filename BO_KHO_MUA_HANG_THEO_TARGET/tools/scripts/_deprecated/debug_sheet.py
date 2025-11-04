"""
Debug Google Sheet
"""

from google_sheets_api import get_sheet_data, SPREADSHEET_ID
import json

data = get_sheet_data(SPREADSHEET_ID, 'VTTH')

if data:
    print(f"[INFO] Total rows: {len(data)}")
    print(f"[INFO] Total columns in header: {len(data[0])}")

    # Header
    print("\n[INFO] Column names (index: name):")
    for i, col in enumerate(data[0]):
        # Encode to ASCII to avoid encoding issues
        try:
            col_safe = col.encode('ascii', 'ignore').decode('ascii')
        except:
            col_safe = f"<non-ascii-{i}>"
        print(f"  {i}: {col_safe}")

    # Check for "x" in various columns
    print("\n[INFO] Checking for 'x' marks in data rows...")
    for row_idx in range(1, min(len(data), 6)):  # Check first 5 data rows
        row = data[row_idx]
        print(f"\nRow {row_idx}:")
        for col_idx in [11, 12, 13, 14, 15]:  # Check columns around 12
            val = row[col_idx] if col_idx < len(row) else "N/A"
            print(f"  Col {col_idx}: '{val}'")

    # Save to file for inspection
    with open('workspace/debug_vtth.json', 'w', encoding='utf-8') as f:
        json.dump({
            'total_rows': len(data),
            'header': data[0],
            'first_5_rows': data[1:6]
        }, f, ensure_ascii=False, indent=2)

    print("\n[SUCCESS] Saved full data to workspace/debug_vtth.json")
else:
    print("[ERROR] No data")
