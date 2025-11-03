"""
Calculator - Tinh toan VTTH va Hoa Chat
FIXED: Phu hop voi cau truc sheet thuc te
"""

import math
import json
from datetime import datetime
import sys
import os
import re

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from google_sheets_api import get_sheet_data, SPREADSHEET_ID


def parse_qty_from_string(s):
    """
    Parse so luong tu string
    VD: "100 lo" -> 100, "102 mieng" -> 102
    """
    if not s:
        return 1

    # Tim so dau tien trong string
    match = re.search(r'(\d+)', str(s))
    if match:
        return int(match.group(1))
    return 1


def calculate_vtth(so_khach, goi_dv="B2B-Goi dong"):
    """
    Tinh VTTH theo so khach va goi dich vu

    CAU TRUC SHEET THUC TE:
    - Col 1: Ten VTTH
    - Col 3: Don vi tinh (DVT lon: Bich, Hop, etc.)
    - Col 4: So luong trong 1 don vi (VD: "100 lo", "102 mieng")
    - Col 7: So luong cho Goi co ban
    - Col 9: So luong cho Goi dong
    - Col 11: So luong cho Goi bac

    Args:
        so_khach: So luong khach hang
        goi_dv: Goi dich vu

    Returns:
        List of dict voi thong tin VTTH da tinh
    """
    print(f"\n[CALCULATOR] Tinh VTTH cho {so_khach} khach - {goi_dv}")

    # Validate input
    if so_khach <= 0:
        print("[ERROR] So khach hang phai > 0")
        return None

    valid_goi = ["B2B-Goi dong", "B2B-Goi co ban", "B2B-Goi bac"]
    if goi_dv not in valid_goi:
        print(f"[ERROR] Goi dich vu khong hop le. Chon: {', '.join(valid_goi)}")
        return None

    # Doc du lieu tu Google Sheets
    print("[INFO] Doc du lieu tu sheet 'VTTH'...")
    data = get_sheet_data(SPREADSHEET_ID, "VTTH")

    if not data or len(data) < 2:
        print("[ERROR] Khong co du lieu trong sheet 'VTTH'")
        return None

    # Map goi dich vu → column index (SO LUONG)
    col_map = {
        "B2B-Goi co ban": 7,   # Col 7: So luong Goi co ban
        "B2B-Goi dong": 9,     # Col 9: So luong Goi dong
        "B2B-Goi bac": 11      # Col 11: So luong Goi bac
    }

    col_index = col_map[goi_dv]

    # Loc theo goi dich vu (so luong > 0)
    print(f"[INFO] Loc theo cot {col_index} (goi: {goi_dv})...")
    filtered_items = []

    for row in data[1:]:  # Bo header
        if len(row) <= col_index:
            continue

        try:
            so_luong = float(row[col_index]) if row[col_index] else 0
            if so_luong > 0:
                filtered_items.append(row)
        except:
            continue

    print(f"[SUCCESS] Tim thay {len(filtered_items)} loai VTTH cho goi nay")

    if not filtered_items:
        print("[ERROR] Khong tim thay VTTH nao cho goi nay")
        return None

    # Tinh toan
    print("[INFO] Dang tinh toan...")
    results = []

    for row in filtered_items:
        try:
            ten = row[1] if len(row) > 1 else "Unknown"

            # So luong VTTH dung cho 1 khach (dinh muc)
            dinh_muc = float(row[col_index]) if len(row) > col_index and row[col_index] else 0

            # Don vi tinh (DVT lon)
            dvt_lon = row[3] if len(row) > 3 else "Hop"

            # Ty le quy doi (parse tu string "100 lo", "102 mieng")
            ty_le_str = row[4] if len(row) > 4 else "1"
            ty_le_quy_doi = parse_qty_from_string(ty_le_str)

            # Determine DVT nho
            if 'lo' in str(ty_le_str).lower():
                dvt_nho = 'lo'
            elif 'mieng' in str(ty_le_str).lower():
                dvt_nho = 'mieng'
            elif 'ml' in str(ty_le_str).lower():
                dvt_nho = 'ml'
            else:
                dvt_nho = 'cai'

            # ⭐ Tinh nhu cau don vi nho
            # DINH MUC = DON VI NHO (lo/khach, mieng/khach, cai/khach)
            # Nhu cau (lo) = So khach × Dinh muc
            # VD: 100 khach × 1.0 lo/khach = 100 lo
            nhu_cau_nho = so_khach * dinh_muc

            # ⭐ Quy doi sang don vi lon (ROUNDUP)
            # So Bich = ROUNDUP(100 lo / 100 lo/Bich) = 1 Bich
            so_luong_lon = math.ceil(nhu_cau_nho / ty_le_quy_doi) if ty_le_quy_doi > 0 else int(nhu_cau_nho)

            results.append({
                'ten': ten,
                'dinh_muc': dinh_muc,
                'dvt_nho': dvt_nho,
                'dvt_lon': dvt_lon,
                'ty_le_quy_doi': ty_le_quy_doi,
                'so_luong_nho': nhu_cau_nho,
                'so_luong_lon': int(so_luong_lon)
            })

        except Exception as e:
            print(f"[WARNING] Loi khi xu ly row {row[1] if len(row) > 1 else 'Unknown'}: {e}")
            continue

    return results


def display_vtth_results(results, so_khach, goi_dv):
    """
    Hien thi ket qua tinh VTTH
    """
    if not results:
        return

    print("\n" + "="*90)
    print(f"[SUCCESS] Da tinh VTTH cho {so_khach} khach - {goi_dv}")
    print("="*90)

    # Header
    header_fmt = "{:<5} {:<35} {:<12} {:<18} {:<12} {:<10}"
    print(header_fmt.format("STT", "Ten San Pham", "Dinh muc", "Nhu cau (don vi nho)", "So luong", "DVT"))
    print("-"*90)

    # Data
    for idx, item in enumerate(results, 1):
        ten = item['ten'][:33]  # Truncate if too long
        # Encode to ASCII to avoid encoding issues on Windows console
        ten_safe = ten.encode('ascii', 'ignore').decode('ascii')
        if not ten_safe:
            ten_safe = f"Item-{idx}"

        # Sanitize DVT too
        dvt_lon_safe = item['dvt_lon'].encode('ascii', 'ignore').decode('ascii')
        if not dvt_lon_safe:
            dvt_lon_safe = "Unit"

        dvt_display = f"({item['dvt_nho']})"
        row_str = "{:<5} {:<35} {:<12.1f} {:<18.0f} {:<12} {:<10}".format(
            idx,
            ten_safe,
            item['dinh_muc'],
            item['so_luong_nho'],
            item['so_luong_lon'],
            dvt_lon_safe
        )
        print(row_str)

    print("-"*90)
    print(f"[INFO] Tong: {len(results)} loai VTTH")

    # Luu ket qua
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"workspace/calculations/vtth_{timestamp}.json"

    output_data = {
        'type': 'VTTH',
        'so_khach': so_khach,
        'goi_dv': goi_dv,
        'timestamp': timestamp,
        'results': results
    }

    try:
        os.makedirs('workspace/calculations', exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        print(f"[INFO] Da luu vao: {output_file}")
    except Exception as e:
        print(f"[WARNING] Khong the luu file: {e}")

    print("\n" + "="*90)
    print("Buoc tiep theo:")
    print("- Chay /so-sanh-kho [file_path] de so sanh voi ton kho")
    print("- Hoac chay /tinh-hoa-chat de tinh hoa chat")
    print("="*90 + "\n")


# CLI
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calculator.py <so_khach> [goi_dv]")
        print("Vi du: python calculator.py 100")
        print("Vi du: python calculator.py 150 'B2B-Goi co ban'")
        sys.exit(1)

    so_khach = int(sys.argv[1])
    goi_dv = sys.argv[2] if len(sys.argv) > 2 else "B2B-Goi dong"

    results = calculate_vtth(so_khach, goi_dv)

    if results:
        display_vtth_results(results, so_khach, goi_dv)
    else:
        print("\n[ERROR] Khong the tinh toan VTTH")
        sys.exit(1)
