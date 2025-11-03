"""
Calculator - Tinh toan Hoa Chat
Theo CLAUDE.md: Doc tu "Hoa Chat Chi Tiet", tra cuu QC/CALIB tu "Hoa Chat"
"""

import math
import json
from datetime import datetime
import sys
import os
import io

# Set UTF-8 encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from google_sheets_api import get_sheet_data, SPREADSHEET_ID


def calculate_hoa_chat(so_khach, goi_dv="B2B-Goi dong"):
    """
    Tinh Hoa Chat theo so khach va goi dich vu

    QUY TAC:
    1. Doc sheet "Hoa Chat Chi Tiet" de LOC danh sach
    2. Doc sheet "Hoa Chat" de TRA CUU QC/CALIB
    3. Tinh toan: Test khach + QC + CALIB
    4. Quy doi sang don vi lon (ROUNDUP)

    Args:
        so_khach: So luong khach hang
        goi_dv: Goi dich vu

    Returns:
        List of dict voi thong tin Hoa Chat da tinh
    """
    print(f"\n[CALCULATOR] Tinh Hoa Chat cho {so_khach} khach - {goi_dv}")

    # Validate input
    if so_khach <= 0:
        print("[ERROR] So khach hang phai > 0")
        return None

    valid_goi = ["B2B-Goi dong", "B2B-Goi co ban", "B2B-Goi bac"]
    if goi_dv not in valid_goi:
        print(f"[ERROR] Goi dich vu khong hop le. Chon: {', '.join(valid_goi)}")
        return None

    # ⭐ BUOC 1: Doc sheet "Hoa Chat Chi Tiet" (SHEET CHINH)
    print("[INFO] Doc du lieu tu sheet 'Hoa Chat Chi Tiet'...")
    chi_tiet_data = get_sheet_data(SPREADSHEET_ID, "Hoa Chat Chi Tiet")

    if not chi_tiet_data or len(chi_tiet_data) < 2:
        print("[ERROR] Khong co du lieu trong sheet 'Hoa Chat Chi Tiet'")
        return None

    # Map goi dich vu → column index
    col_map = {
        "B2B-Goi co ban": 13,   # Col 13: Gói cơ bản
        "B2B-Goi dong": 12,     # Col 12: Gói đồng
        "B2B-Goi bac": 14       # Col 14: Gói bạc
    }

    col_index = col_map[goi_dv]

    # ⭐ BUOC 2: Loc theo goi dich vu
    # Dieu kien: Loai = "Chạy mẫu" + Goi co "x"
    print(f"[INFO] Loc theo Loai='Chạy mẫu' va cot {col_index} (goi: {goi_dv})...")
    filtered_items = []

    for row in chi_tiet_data[1:]:  # Bo header
        if len(row) <= col_index:
            continue

        try:
            loai_hc = row[5] if len(row) > 5 else ""  # Col 5: Loại hóa chất
            goi_mark = row[col_index] if len(row) > col_index else ""

            # Dieu kien loc
            if loai_hc == "Chạy mẫu" and goi_mark == "x":
                ten = row[3] if len(row) > 3 else ""  # Col 3: Tên HC
                lo_per_hop = float(row[9]) if len(row) > 9 and row[9] else 1  # Col 9: Lọ/hộp
                test_per_lo = float(row[10]) if len(row) > 10 and row[10] else 0  # Col 10: Test/lọ

                filtered_items.append({
                    'ten': ten,
                    'lo_per_hop': lo_per_hop,
                    'test_per_lo': test_per_lo
                })
        except Exception as e:
            continue

    print(f"[SUCCESS] Tim thay {len(filtered_items)} loai Hoa Chat cho goi nay")

    if not filtered_items:
        print("[ERROR] Khong tim thay Hoa Chat nao cho goi nay")
        return None

    # ⭐ BUOC 3: Doc sheet "Hoa Chat" de tra cuu QC/CALIB
    print("[INFO] Doc du lieu tu sheet 'Hoa Chat' de tra cuu QC/CALIB...")
    hoa_chat_data = get_sheet_data(SPREADSHEET_ID, "Hoa Chat")

    # ⭐ BUOC 4: Tinh toan
    print("[INFO] Dang tinh toan...")
    results = []

    for item in filtered_items:
        try:
            ten = item['ten']
            lo_per_hop = item['lo_per_hop']
            test_per_lo = item['test_per_lo']

            # Tra cuu QC/CALIB tu sheet "Hoa Chat"
            test_qc = 2      # Mac dinh
            test_calib = 4   # Mac dinh

            if hoa_chat_data and len(hoa_chat_data) > 1:
                for qc_row in hoa_chat_data[1:]:
                    ten_qc = qc_row[1] if len(qc_row) > 1 else ""
                    if ten_qc.strip().lower() == ten.strip().lower():
                        test_qc = int(float(qc_row[16])) if len(qc_row) > 16 and qc_row[16] else 2
                        test_calib = int(float(qc_row[24])) if len(qc_row) > 24 and qc_row[24] else 4
                        break

            # Dac biet: HC khong co QC/CALIB
            keywords_no_qc = ["dung dịch", "dung dich", "wash", "tiểu", "tieu", "diluit", "lyse", "clean", "dye"]
            if any(keyword in ten.lower() for keyword in keywords_no_qc):
                test_qc = 0
                test_calib = 0

            # Tinh toan
            test_khach = so_khach
            tong_test = test_khach + test_qc + test_calib

            if test_per_lo > 0:
                so_lo = math.ceil(tong_test / test_per_lo)
                so_hop = math.ceil(so_lo / lo_per_hop)
            else:
                so_lo = 1
                so_hop = 1

            # Xac dinh don vi lon
            if "20L" in ten or "20l" in ten.lower():
                dvt_lon = "Thùng"
            elif any(k in ten.lower() for k in ["dung dịch", "dung dich", "lyse", "clean"]):
                dvt_lon = "Chai"
            else:
                dvt_lon = "Hộp"

            results.append({
                'ten': ten,
                'dvt_nho': 'lọ',
                'dvt_lon': dvt_lon,
                'ty_le_quy_doi': lo_per_hop,
                'test_per_lo': test_per_lo,
                'test_khach': test_khach,
                'test_qc': test_qc,
                'test_calib': test_calib,
                'tong_test': tong_test,
                'so_luong_nho': so_lo,
                'so_luong_lon': so_hop
            })

        except Exception as e:
            print(f"[WARNING] Loi khi xu ly {ten}: {e}")
            continue

    return results


def display_hoa_chat_results(results, so_khach, goi_dv):
    """
    Hien thi ket qua tinh Hoa Chat
    """
    if not results:
        return

    print("\n" + "="*110)
    print(f"[SUCCESS] Da tinh Hoa Chat cho {so_khach} khach - {goi_dv}")
    print("="*110)

    # Header
    header_fmt = "{:<5} {:<40} {:<12} {:<8} {:<8} {:<10} {:<8} {:<8} {:<10}"
    print(header_fmt.format("STT", "Tên Hóa Chất", "Test/lọ", "Test KH", "QC", "Calib", "Tổng", "Lọ", "DVT lớn"))
    print("-"*110)

    # Data
    for idx, item in enumerate(results, 1):
        ten = item['ten'][:38]
        row_str = "{:<5} {:<40} {:<12.0f} {:<8} {:<8} {:<10} {:<8} {:<8} {:<10}".format(
            idx,
            ten,
            item['test_per_lo'],
            item['test_khach'],
            item['test_qc'],
            item['test_calib'],
            item['tong_test'],
            item['so_luong_nho'],
            f"{item['so_luong_lon']} {item['dvt_lon']}"
        )
        print(row_str)

    print("-"*110)
    print(f"[INFO] Tong: {len(results)} loai Hoa Chat")

    # Luu ket qua
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"workspace/calculations/hoa_chat_{timestamp}.json"

    output_data = {
        'type': 'HOA_CHAT',
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

    print("\n" + "="*110)
    print("Buoc tiep theo:")
    print("- Chay /so-sanh-kho [file_path] de so sanh voi ton kho")
    print("="*110 + "\n")


# CLI
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calculate_chemicals.py <so_khach> [goi_dv]")
        print("Vi du: python calculate_chemicals.py 100")
        print("Vi du: python calculate_chemicals.py 150 'B2B-Goi co ban'")
        sys.exit(1)

    so_khach = int(sys.argv[1])
    goi_dv = sys.argv[2] if len(sys.argv) > 2 else "B2B-Goi dong"

    results = calculate_hoa_chat(so_khach, goi_dv)

    if results:
        display_hoa_chat_results(results, so_khach, goi_dv)
    else:
        print("\n[ERROR] Khong the tinh toan Hoa Chat")
        sys.exit(1)
