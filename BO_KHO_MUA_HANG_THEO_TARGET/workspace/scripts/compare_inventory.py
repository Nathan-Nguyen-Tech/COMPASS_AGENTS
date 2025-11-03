# -*- coding: utf-8 -*-
"""
So sánh tồn kho với kết quả VTTH đã tính toán
⭐ CRITICAL: LUÔN so sánh bằng đơn vị nhỏ!
"""

import pandas as pd
import json
import math
from datetime import datetime
import re

def normalize_name(name):
    """Chuẩn hóa tên sản phẩm để matching"""
    if pd.isna(name) or name is None:
        return ""

    name = str(name).strip().lower()
    # Loại bỏ khoảng trắng thừa
    name = re.sub(r'\s+', ' ', name)
    return name

def find_inventory(ten_sp, df_ton_kho):
    """
    Tìm tồn kho của sản phẩm
    Returns: (ton_kho_value, dvt) hoặc (0, "")
    """
    ten_chuan = normalize_name(ten_sp)

    # Tìm kiếm exact match
    for idx, row in df_ton_kho.iterrows():
        ten_kho = normalize_name(row.get('Tên hàng', ''))
        if ten_kho and ten_kho == ten_chuan:
            ton_kho = row.get('Cuối kỳ', 0)
            dvt = row.get('ĐVT', '')
            try:
                ton_kho_float = float(ton_kho) if not pd.isna(ton_kho) else 0
                return (ton_kho_float, str(dvt) if not pd.isna(dvt) else "")
            except:
                return (0, "")

    # Tìm kiếm partial match (chứa từ khóa)
    for idx, row in df_ton_kho.iterrows():
        ten_kho = normalize_name(row.get('Tên hàng', ''))
        if ten_kho and (ten_chuan in ten_kho or ten_kho in ten_chuan):
            ton_kho = row.get('Cuối kỳ', 0)
            dvt = row.get('ĐVT', '')
            try:
                ton_kho_float = float(ton_kho) if not pd.isna(ton_kho) else 0
                return (ton_kho_float, str(dvt) if not pd.isna(dvt) else "")
            except:
                return (0, "")

    return (0, "")

def compare_inventory(vtth_file, inventory_file):
    """
    So sánh tồn kho với kết quả VTTH

    ⭐ CRITICAL RULE:
    - SO SÁNH: LUÔN dùng đơn vị nhỏ
    - PHIẾU MUA: Dùng đơn vị lớn (ROUNDUP)
    """

    print("=" * 80)
    print("BAT DAU SO SANH TON KHO")
    print("=" * 80)

    # 1. Doc file VTTH da tinh
    print(f"\n1. Doc file VTTH: {vtth_file}")
    with open(vtth_file, 'r', encoding='utf-8') as f:
        vtth_data = json.load(f)

    so_khach = vtth_data.get('so_khach', 0)
    goi_dv = vtth_data.get('goi_dv', '')
    vtth_items = vtth_data.get('results', [])

    print(f"   - So khach: {so_khach}")
    print(f"   - Goi dich vu: {goi_dv}")
    print(f"   - So loai VTTH: {len(vtth_items)}")

    # 2. Đọc file tồn kho
    print(f"\n2. Doc file ton kho: {inventory_file}")

    # Đọc Excel - header ở row 2, data từ row 4
    df = pd.read_excel(inventory_file, skiprows=2)

    # Kiểm tra cột
    print(f"   - Columns: {df.columns.tolist()}")

    # Xác định tên cột chính xác
    col_mapping = {}
    for col in df.columns:
        col_lower = str(col).lower().strip()
        if 'tên hàng' in col_lower or 'ten hang' in col_lower:
            col_mapping['Tên hàng'] = col
        elif 'đvt' in col_lower or 'dvt' in col_lower:
            col_mapping['ĐVT'] = col
        elif 'cuối kỳ' in col_lower or 'cuoi ky' in col_lower or 'số lượng' in col_lower:
            col_mapping['Cuối kỳ'] = col

    print(f"   - Column mapping: {col_mapping}")

    # Rename columns
    df.rename(columns={v: k for k, v in col_mapping.items()}, inplace=True)

    # Lọc bỏ rows rỗng
    if 'Tên hàng' in df.columns:
        df = df[df['Tên hàng'].notna()]
    else:
        print("   ⚠️ Khong tim thay cot 'Ten hang', su dung cot dau tien")
        df.columns = ['Tên kho', 'Mã hàng', 'Tên hàng', 'ĐVT', 'Cuối kỳ']
        df = df[df['Tên hàng'].notna()]

    print(f"   - So dong co data: {len(df)}")
    print(f"   - Sample data:")
    for idx in range(min(3, len(df))):
        row = df.iloc[idx]
        print(f"     + {row.get('Tên hàng', 'N/A')} | DVT: {row.get('ĐVT', 'N/A')} | Ton: {row.get('Cuối kỳ', 'N/A')}")

    # 3. So sanh tung item
    print(f"\n3. Bat dau so sanh...")
    results = []

    can_mua_count = 0
    het_kho_count = 0
    du_kho_count = 0

    for item in vtth_items:
        ten = item['ten']
        can_nho = float(item['so_luong_nho'])
        dvt_nho = item['dvt_nho']
        dvt_lon = item['dvt_lon']
        ty_le = float(item['ty_le_quy_doi'])

        # Tìm tồn kho
        ton_kho_lon, dvt_kho = find_inventory(ten, df)

        # ⭐ QUY TẮC #1: CHUYỂN TỒN KHO SANG ĐƠN VỊ NHỎ
        ton_kho_nho = ton_kho_lon * ty_le

        # ⭐ QUY TẮC #2: SO SÁNH BẰNG ĐƠN VỊ NHỎ
        can_mua_nho = max(0, can_nho - ton_kho_nho)

        # ⭐ QUY TẮC #3: QUY ĐỔI SANG ĐƠN VỊ LỚN (ROUNDUP) CHO PHIẾU
        if ty_le > 0:
            can_mua_lon = math.ceil(can_mua_nho / ty_le)
        else:
            can_mua_lon = int(can_mua_nho)

        # Xác định trạng thái
        if ton_kho_nho >= can_nho:
            trang_thai = "ĐỦ KHO"
            du_kho_count += 1
        elif ton_kho_nho == 0:
            trang_thai = "HẾT KHO"
            het_kho_count += 1
        else:
            trang_thai = "CẦN MUA"
            can_mua_count += 1

        results.append({
            'ten': ten,
            'dvt_nho': dvt_nho,
            'dvt_lon': dvt_lon,
            'ty_le_quy_doi': ty_le,
            'can_nho': can_nho,
            'ton_kho_nho': ton_kho_nho,
            'ton_kho_lon': ton_kho_lon,
            'can_mua_nho': can_mua_nho,
            'can_mua_lon': can_mua_lon,
            'trang_thai': trang_thai,
            'dvt_kho': dvt_kho
        })

    # 4. Tạo output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output = {
        'type': 'INVENTORY_COMPARISON',
        'so_khach': so_khach,
        'goi_dv': goi_dv,
        'timestamp': timestamp,
        'inventory_file': inventory_file,
        'vtth_file': vtth_file,
        'items': results,
        'summary': {
            'tong_loai': len(results),
            'can_mua': can_mua_count,
            'het_kho': het_kho_count,
            'du_kho': du_kho_count
        }
    }

    # 5. Lưu kết quả
    output_file = f"D:\\Compass_Coding\\COMPASS_AGENTS\\BO_KHO_MUA_HANG_THEO_TARGET\\workspace\\calculations\\inventory_comparison_{timestamp}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nHOAN THANH!")
    print(f"\nTONG KET:")
    print(f"   - Tong loai: {len(results)}")
    print(f"   - CAN MUA: {can_mua_count}")
    print(f"   - HET KHO: {het_kho_count}")
    print(f"   - DU KHO: {du_kho_count}")
    print(f"\nFile ket qua: {output_file}")

    return output

if __name__ == "__main__":
    vtth_file = r"D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET\workspace\calculations\vtth_20251102_193343.json"
    inventory_file = r"C:\Users\nguye\Downloads\Tong_hop_ton_kho (34) (1).xlsx"

    result = compare_inventory(vtth_file, inventory_file)

    # Hien thi chi tiet
    print("\n" + "=" * 80)
    print("CHI TIET SO SANH")
    print("=" * 80)

    # Bang CAN MUA
    can_mua_items = [item for item in result['items'] if item['trang_thai'] in ['CẦN MUA', 'HẾT KHO']]
    if can_mua_items:
        print(f"\nCAN MUA ({len(can_mua_items)} loai):")
        print("-" * 80)
        for idx, item in enumerate(can_mua_items, 1):
            print(f"{idx:2d}. {item['ten'][:50]:50s} | Can: {item['can_nho']:6.0f} {item['dvt_nho']:6s} | Ton: {item['ton_kho_nho']:6.0f} | Mua: {item['can_mua_lon']:3d} {item['dvt_lon']:6s} | {item['trang_thai']}")

    # Bang DU KHO
    du_kho_items = [item for item in result['items'] if item['trang_thai'] == 'ĐỦ KHO']
    if du_kho_items:
        print(f"\nDU KHO ({len(du_kho_items)} loai):")
        print("-" * 80)
        for idx, item in enumerate(du_kho_items, 1):
            print(f"{idx:2d}. {item['ten'][:50]:50s} | Can: {item['can_nho']:6.0f} {item['dvt_nho']:6s} | Ton: {item['ton_kho_nho']:6.0f}")
