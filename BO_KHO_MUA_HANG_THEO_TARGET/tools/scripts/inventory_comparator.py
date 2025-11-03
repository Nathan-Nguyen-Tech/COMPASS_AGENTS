"""
Inventory Comparator - So sanh ton kho
"""

import pandas as pd
import json
import math
import os
import sys
from datetime import datetime
import glob


def normalize_name(name):
    """
    Chuan hoa ten san pham de matching
    - Lowercase
    - Strip whitespace
    - Remove special chars
    """
    if not name:
        return ""

    # Lowercase and strip
    name = str(name).lower().strip()

    # Remove extra spaces
    name = " ".join(name.split())

    return name


def find_latest_calculation():
    """
    Tim file tinh toan moi nhat trong workspace/calculations/
    """
    pattern = "workspace/calculations/vtth_*.json"
    files = glob.glob(pattern)

    if not files:
        return None

    # Sort by modification time, newest first
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]


def load_calculation_results(file_path=None):
    """
    Doc ket qua tinh toan tu file JSON
    """
    if not file_path:
        file_path = find_latest_calculation()
        if not file_path:
            print("[ERROR] Khong tim thay file ket qua tinh toan")
            print("[HELP] Chay /tinh-vtth hoac /tinh-hoa-chat truoc")
            return None

    if not os.path.exists(file_path):
        print(f"[ERROR] File khong ton tai: {file_path}")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"[INFO] Doc ket qua tinh toan tu: {file_path}")
        print(f"[INFO] Loai: {data.get('type', 'N/A')}")
        print(f"[INFO] So khach: {data.get('so_khach', 'N/A')}")
        print(f"[INFO] Goi DV: {data.get('goi_dv', 'N/A')}")
        print(f"[INFO] So items: {len(data.get('results', []))}")

        return data
    except Exception as e:
        print(f"[ERROR] Loi khi doc file: {e}")
        return None


def load_inventory_file(file_path):
    """
    Doc file ton kho (Excel hoac CSV)

    Cau truc file:
    Row 0: "Kho: KHO VAN PHONG NVL, Thang X nam YYYY"
    Row 1: (Blank)
    Row 2: Ten kho | Ma hang | Ten hang | DVT | Cuoi ky  (HEADER)
    Row 3:                                    | So luong  (Sub-header)
    Row 4+: Data
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] File ton kho khong ton tai: {file_path}")
        return None

    try:
        # Doc file
        if file_path.endswith('.xlsx'):
            # Skip row 0, 1 va doc row 2 lam header
            df = pd.read_excel(file_path, header=2)
            print(f"[INFO] Doc file Excel: {file_path}")
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path, header=2)
            print(f"[INFO] Doc file CSV: {file_path}")
        else:
            print(f"[ERROR] File phai la .xlsx hoac .csv")
            return None

        print(f"[DEBUG] Num columns: {len(df.columns)}")
        print(f"[DEBUG] Num rows: {len(df)}")

        # Skip row 3 (sub-header "So luong")
        # Row 3 sau khi skip 2 rows se la row 0 trong df
        df = df.iloc[1:].reset_index(drop=True)

        # Rename columns de chuan hoa
        # Columns: Ten kho | Ma hang | Ten hang | DVT | Cuoi ky
        # → Rename: Unnamed -> readable names

        # Neu columns la Unnamed, rename
        df.columns = ['Ten kho', 'Ma hang', 'Ten hang', 'DVT', 'So luong']

        # Kiem tra cot
        if 'Ten hang' not in df.columns or 'So luong' not in df.columns:
            print(f"[ERROR] File khong dung cau truc")
            print(f"[INFO] Columns: {list(df.columns)}")
            return None

        # Loc bo rows trong (NaN)
        df = df.dropna(subset=['Ten hang', 'So luong'])

        # Chuan hoa ten
        df['ten_chuan'] = df['Ten hang'].apply(normalize_name)

        # Convert So luong sang float
        df['So luong'] = pd.to_numeric(df['So luong'], errors='coerce').fillna(0)

        print(f"[INFO] Doc duoc {len(df)} dong tu file ton kho")

        return df

    except Exception as e:
        print(f"[ERROR] Loi khi doc file: {e}")
        import traceback
        traceback.print_exc()
        return None


def compare_inventory(calculated_data, inventory_df):
    """
    So sanh ket qua tinh toan voi ton kho

    QUY TAC VANG: LUON so sanh bang don vi nho!
    """
    print("\n[INFO] Bat dau so sanh ton kho...")

    results = calculated_data['results']
    so_khach = calculated_data['so_khach']
    goi_dv = calculated_data['goi_dv']

    comparison_results = []

    for item in results:
        ten_chuan = normalize_name(item['ten'])
        can_nho = item['so_luong_nho']  # Don vi nho (lo, mieng, ml)
        ty_le_quy_doi = item['ty_le_quy_doi']

        # Tim ton kho
        ton_kho_row = inventory_df[inventory_df['ten_chuan'] == ten_chuan]

        if not ton_kho_row.empty:
            ton_kho_value = float(ton_kho_row.iloc[0]['So luong'])
            dvt_ton_kho = str(ton_kho_row.iloc[0]['DVT']).strip().lower() if 'DVT' in ton_kho_row.iloc[0] else ''

            # ⭐ KIEM TRA DVT de xac dinh don vi ton kho
            # Neu DVT trong file = dvt_lon → Ton kho luu theo don vi LON
            # Neu DVT trong file = dvt_nho → Ton kho luu theo don vi NHO
            dvt_lon_chuan = normalize_name(item['dvt_lon'])
            dvt_nho_chuan = normalize_name(item['dvt_nho'])

            if dvt_ton_kho == dvt_lon_chuan:
                # Ton kho dang luu theo DON VI LON (VD: Can, Thung)
                # Can NHAN voi ty le quy doi
                ton_kho_lon = ton_kho_value
                ton_kho_nho = ton_kho_value * ty_le_quy_doi
            else:
                # Ton kho dang luu theo DON VI NHO (Lo, Cai, Mieng) - TRUONG HOP PHO BIEN
                ton_kho_nho = ton_kho_value
                ton_kho_lon = ton_kho_value / ty_le_quy_doi if ty_le_quy_doi > 0 else 0
        else:
            # Khong tim thay trong ton kho
            ton_kho_nho = 0
            ton_kho_lon = 0

        # ⭐ SO SANH BANG DON VI NHO
        can_mua_nho = max(0, can_nho - ton_kho_nho)

        # ⭐ QUY DOI SANG DON VI LON (ROUNDUP)
        can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi) if ty_le_quy_doi > 0 else 0

        # Xac dinh trang thai
        if ton_kho_nho >= can_nho:
            trang_thai = "DU KHO"
        elif ton_kho_nho == 0:
            trang_thai = "HET KHO"
        else:
            trang_thai = "CAN MUA"

        # Luu ket qua
        comparison_results.append({
            'ten': item['ten'],
            'dvt_nho': item['dvt_nho'],
            'dvt_lon': item['dvt_lon'],
            'ty_le_quy_doi': ty_le_quy_doi,
            'can_nho': can_nho,
            'ton_kho_nho': ton_kho_nho,
            'ton_kho_lon': ton_kho_lon,
            'can_mua_nho': can_mua_nho,
            'can_mua_lon': can_mua_lon,
            'trang_thai': trang_thai
        })

    return comparison_results


def display_comparison_results(results):
    """
    Hien thi ket qua so sanh
    """
    # Phan loai
    can_mua = [r for r in results if r['trang_thai'] != 'DU KHO']
    du_kho = [r for r in results if r['trang_thai'] == 'DU KHO']

    print("\n" + "="*100)
    print("[SUCCESS] Da so sanh voi ton kho!")
    print("="*100)

    # Bang CAN MUA
    print(f"\n## CAN MUA ({len(can_mua)} loai)")
    print("-"*100)

    if can_mua:
        header = "{:<5} {:<30} {:<12} {:<12} {:<12} {:<12} {:<15}"
        print(header.format("STT", "Ten SP", "Can (nho)", "Ton (nho)", "Mua (nho)", "Mua (lon)", "Trang thai"))
        print("-"*100)

        for idx, item in enumerate(can_mua, 1):
            # Sanitize for console
            ten_safe = item['ten'][:28].encode('ascii', 'ignore').decode('ascii')
            if not ten_safe:
                ten_safe = f"Item-{idx}"

            row = "{:<5} {:<30} {:<12.0f} {:<12.0f} {:<12.0f} {:<12} {:<15}".format(
                idx,
                ten_safe,
                item['can_nho'],
                item['ton_kho_nho'],
                item['can_mua_nho'],
                item['can_mua_lon'],
                item['trang_thai']
            )
            print(row)
    else:
        print("[INFO] Tat ca deu DU KHO!")

    # Bang DU KHO
    print(f"\n## DU KHO ({len(du_kho)} loai)")
    print("-"*100)

    if du_kho:
        header = "{:<5} {:<30} {:<12} {:<12} {:<15}"
        print(header.format("STT", "Ten SP", "Can (nho)", "Ton (nho)", "Trang thai"))
        print("-"*100)

        for idx, item in enumerate(du_kho, 1):
            ten_safe = item['ten'][:28].encode('ascii', 'ignore').decode('ascii')
            if not ten_safe:
                ten_safe = f"Item-{idx}"

            row = "{:<5} {:<30} {:<12.0f} {:<12.0f} {:<15}".format(
                idx,
                ten_safe,
                item['can_nho'],
                item['ton_kho_nho'],
                item['trang_thai']
            )
            print(row)

    # Tong ket
    print("\n" + "="*100)
    print(f"[INFO] Tong ket:")
    print(f"  - Tong loai: {len(results)}")
    print(f"  - CAN MUA: {len(can_mua)} loai")
    print(f"  - DU KHO: {len(du_kho)} loai")
    print("="*100)

    # Luu ket qua
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Tao folder neu chua ton tai (relative to project root)
    project_root = os.path.join(os.path.dirname(__file__), '../..')
    calc_folder = os.path.join(project_root, 'workspace/calculations')
    os.makedirs(calc_folder, exist_ok=True)

    output_file = os.path.join(calc_folder, f"comparison_{timestamp}.json")

    output_data = {
        'timestamp': timestamp,
        'can_mua': can_mua,
        'du_kho': du_kho,
        'summary': {
            'tong_loai': len(results),
            'can_mua': len(can_mua),
            'du_kho': len(du_kho)
        }
    }

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        print(f"\n[INFO] Da luu ket qua vao: {output_file}")
    except Exception as e:
        print(f"[WARNING] Khong the luu file: {e}")

    print("\n" + "="*100)
    print("Buoc tiep theo:")
    print("- Chay /tao-phieu de tao phieu mua hang tu dong")
    print("="*100 + "\n")

    return output_data


# CLI
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inventory_comparator.py <ton_kho_file> [calculation_file]")
        print("")
        print("Vi du:")
        print("  python inventory_comparator.py workspace/inventory-files/ton-kho.csv")
        print("  python inventory_comparator.py ton-kho.xlsx workspace/calculations/vtth_xxx.json")
        print("")
        print("Neu khong chi dinh calculation_file, se dung file moi nhat")
        sys.exit(1)

    ton_kho_file = sys.argv[1]
    calc_file = sys.argv[2] if len(sys.argv) > 2 else None

    # Load ket qua tinh toan
    calc_data = load_calculation_results(calc_file)
    if not calc_data:
        sys.exit(1)

    # Load file ton kho
    inventory_df = load_inventory_file(ton_kho_file)
    if inventory_df is None:
        sys.exit(1)

    # So sanh
    comparison = compare_inventory(calc_data, inventory_df)

    # Hien thi
    display_comparison_results(comparison)
