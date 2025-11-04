"""
Inventory Comparison Script
So sánh tồn kho với kết quả VTTH đã tính toán
⭐ LUÔN SO SÁNH BẰNG ĐƠN VỊ NHỎ!
"""

import pandas as pd
import json
import math
import re
from datetime import datetime
from pathlib import Path
import unicodedata


def normalize_name(name):
    """
    Chuẩn hóa tên sản phẩm để matching
    - Lowercase
    - Strip spaces
    - Remove accents (optional)
    - Remove special characters
    """
    if not isinstance(name, str):
        return ""

    # Lowercase và strip
    name = name.strip().lower()

    # Remove multiple spaces
    name = re.sub(r'\s+', ' ', name)

    return name


def remove_accents(text):
    """
    Remove Vietnamese accents for better matching
    """
    if not isinstance(text, str):
        return ""

    # Normalize unicode
    nfd = unicodedata.normalize('NFD', text)

    # Remove combining characters
    text_without_accents = ''.join([c for c in nfd if not unicodedata.combining(c)])

    return text_without_accents


def fuzzy_match_name(name1, name2, threshold=0.7):
    """
    Fuzzy matching cho tên sản phẩm
    Returns: similarity score (0-1)
    """
    # Chuẩn hóa cả 2 tên
    n1 = normalize_name(name1)
    n2 = normalize_name(name2)

    # Remove accents
    n1_no_accent = remove_accents(n1)
    n2_no_accent = remove_accents(n2)

    # Exact match
    if n1 == n2 or n1_no_accent == n2_no_accent:
        return 1.0

    # Substring match
    if n1 in n2 or n2 in n1:
        return 0.9

    if n1_no_accent in n2_no_accent or n2_no_accent in n1_no_accent:
        return 0.85

    # Extract key words (words with length > 3)
    words1 = set([w for w in n1_no_accent.split() if len(w) > 3])
    words2 = set([w for w in n2_no_accent.split() if len(w) > 3])

    if not words1 or not words2:
        return 0.0

    # Jaccard similarity
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))

    if union == 0:
        return 0.0

    return intersection / union


def find_inventory_match(item_name, inventory_df, threshold=0.7):
    """
    Tìm sản phẩm trong file tồn kho
    Returns: (ton_kho_lon, matched_name) hoặc (0, None)
    """
    best_match = None
    best_score = 0
    best_ton_kho = 0

    for idx, row in inventory_df.iterrows():
        inv_name = row.get('Tên hàng', '')
        ton_kho = row.get('Số lượng', 0)

        if pd.isna(inv_name) or inv_name == '':
            continue

        # Calculate similarity
        score = fuzzy_match_name(item_name, inv_name)

        if score > best_score and score >= threshold:
            best_score = score
            best_match = inv_name

            # Parse tồn kho (handle NaN, strings, etc.)
            try:
                best_ton_kho = float(ton_kho) if not pd.isna(ton_kho) else 0
            except:
                best_ton_kho = 0

    if best_match:
        return best_ton_kho, best_match, best_score
    else:
        return 0, None, 0


def load_inventory_file(file_path):
    """
    Đọc file tồn kho (Excel hoặc CSV)
    Returns: DataFrame với columns ['Tên hàng', 'Số lượng', 'ĐVT']
    """
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        # Read Excel
        df = pd.read_excel(file_path, header=None)

        # Find header row (contains 'Tên hàng')
        header_row = None
        for idx, row in df.iterrows():
            if any('tên hàng' in str(cell).lower() for cell in row):
                header_row = idx
                break

        if header_row is None:
            raise ValueError("Không tìm thấy header row trong file Excel")

        # Re-read with correct header
        df = pd.read_excel(file_path, header=header_row)

        # Find 'Số lượng' column
        so_luong_col = None
        for col in df.columns:
            if 'số lượng' in str(col).lower() or 'cuối kỳ' in str(col).lower():
                # Check if this is the quantity column (next row might be "Số lượng")
                if header_row + 1 < len(pd.read_excel(file_path, header=None)):
                    next_row = pd.read_excel(file_path, header=None).iloc[header_row + 1]
                    if 'số lượng' in str(next_row[df.columns.get_loc(col)]).lower():
                        so_luong_col = col
                        break

        # If multi-level header, combine them
        if so_luong_col:
            # Read again without header to get actual data
            df_raw = pd.read_excel(file_path, header=None)
            data_start_row = header_row + 2  # Skip both header rows

            # Find column indices
            header = df_raw.iloc[header_row].tolist()
            ten_hang_idx = next((i for i, v in enumerate(header) if 'tên hàng' in str(v).lower()), None)
            dvt_idx = next((i for i, v in enumerate(header) if 'đvt' in str(v).lower()), None)
            so_luong_idx = df.columns.get_loc(so_luong_col)

            # Extract data
            data = []
            for idx in range(data_start_row, len(df_raw)):
                row = df_raw.iloc[idx]
                if ten_hang_idx is not None and not pd.isna(row[ten_hang_idx]):
                    data.append({
                        'Tên hàng': row[ten_hang_idx],
                        'Số lượng': row[so_luong_idx] if not pd.isna(row[so_luong_idx]) else 0,
                        'ĐVT': row[dvt_idx] if dvt_idx is not None and not pd.isna(row[dvt_idx]) else ''
                    })

            df = pd.DataFrame(data)

    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)

    else:
        raise ValueError("File phải là .xlsx hoặc .csv")

    # Validate columns
    required_cols = ['Tên hàng', 'Số lượng']
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        print(f"⚠️ Warning: Missing columns {missing_cols}")
        print(f"Available columns: {df.columns.tolist()}")

    return df


def compare_inventory(vtth_file, inventory_file, output_file=None):
    """
    So sánh tồn kho với kết quả VTTH
    ⭐ LUÔN SO SÁNH BẰNG ĐƠN VỊ NHỎ!
    """

    print("=" * 60)
    print("🔍 INVENTORY COMPARISON - SO SÁNH TỒN KHO")
    print("=" * 60)
    print()

    # 1. Load VTTH results
    print("📂 Đang đọc kết quả VTTH...")
    with open(vtth_file, 'r', encoding='utf-8') as f:
        vtth_data = json.load(f)

    so_khach = vtth_data.get('so_khach', 0)
    goi_dv = vtth_data.get('goi_dv', '')
    vtth_items = vtth_data.get('items', [])

    print(f"✅ Đã load {len(vtth_items)} items từ VTTH")
    print(f"   Số khách: {so_khach}")
    print(f"   Gói DV: {goi_dv}")
    print()

    # 2. Load inventory file
    print("📂 Đang đọc file tồn kho...")
    inventory_df = load_inventory_file(inventory_file)
    print(f"✅ Đã load {len(inventory_df)} items từ tồn kho")
    print()

    # 3. Compare each item
    print("🔄 Đang so sánh từng sản phẩm...")
    print()

    results = []
    matched_count = 0
    not_found_count = 0

    for item in vtth_items:
        ten = item['ten']
        can_nho = item['so_luong_nho']  # Nhu cầu đơn vị nhỏ
        ty_le_quy_doi = item['ty_le_quy_doi']
        dvt_nho = item['dvt_nho']
        dvt_lon = item['dvt_lon']

        # Find in inventory
        ton_kho_lon, matched_name, match_score = find_inventory_match(ten, inventory_df, threshold=0.6)

        # ⭐ CHUYỂN TỒN KHO SANG ĐƠN VỊ NHỎ
        ton_kho_nho = ton_kho_lon * ty_le_quy_doi

        # ⭐ SO SÁNH BẰNG ĐƠN VỊ NHỎ
        can_mua_nho = max(0, can_nho - ton_kho_nho)

        # ⭐ QUY ĐỔI SANG ĐƠN VỊ LỚN (ROUNDUP) CHO PHIẾU
        can_mua_lon = math.ceil(can_mua_nho / ty_le_quy_doi) if ty_le_quy_doi > 0 else 0

        # Xác định trạng thái
        if ton_kho_nho >= can_nho:
            trang_thai = "ĐỦ KHO"
        elif ton_kho_nho == 0:
            trang_thai = "HẾT KHO"
        else:
            trang_thai = "CẦN MUA"

        # Tracking
        if matched_name:
            matched_count += 1
            if match_score < 1.0:
                print(f"  🔗 Matched: '{ten}' → '{matched_name}' (score: {match_score:.2f})")
        else:
            not_found_count += 1
            print(f"  ⚠️ Not found: '{ten}'")

        # Save result
        result = {
            'stt': item.get('stt', 0),
            'ten': ten,
            'matched_name': matched_name,
            'match_score': match_score,
            'dvt_nho': dvt_nho,
            'dvt_lon': dvt_lon,
            'ty_le_quy_doi': ty_le_quy_doi,
            'can_nho': round(can_nho, 2),
            'ton_kho_nho': round(ton_kho_nho, 2),
            'ton_kho_lon': round(ton_kho_lon, 2),
            'can_mua_nho': round(can_mua_nho, 2),
            'can_mua_lon': int(can_mua_lon),  # Integer cho phiếu
            'trang_thai': trang_thai
        }

        results.append(result)

    print()
    print(f"✅ Đã so sánh xong!")
    print(f"   Matched: {matched_count}/{len(vtth_items)}")
    print(f"   Not found: {not_found_count}/{len(vtth_items)}")
    print()

    # 4. Summary
    can_mua_items = [r for r in results if r['trang_thai'] in ['CẦN MUA', 'HẾT KHO']]
    du_kho_items = [r for r in results if r['trang_thai'] == 'ĐỦ KHO']
    het_kho_items = [r for r in results if r['trang_thai'] == 'HẾT KHO']

    summary = {
        'tong_loai': len(results),
        'can_mua': len(can_mua_items),
        'du_kho': len(du_kho_items),
        'het_kho': len(het_kho_items),
        'matched': matched_count,
        'not_found': not_found_count
    }

    # 5. Save output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if output_file is None:
        output_dir = Path(__file__).parent.parent.parent / "workspace" / "calculations"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"inventory_comparison_{timestamp}.json"

    output_data = {
        'so_khach': so_khach,
        'goi_dv': goi_dv,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'inventory_file': inventory_file,
        'vtth_file': vtth_file,
        'summary': summary,
        'items': results,
        'can_mua_items': can_mua_items,
        'du_kho_items': du_kho_items
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"💾 Đã lưu kết quả vào: {output_file}")
    print()

    return output_data


def display_comparison_results(data):
    """
    Hiển thị kết quả so sánh dưới dạng bảng markdown
    """
    print()
    print("=" * 80)
    print("📊 KẾT QUẢ SO SÁNH TỒN KHO")
    print("=" * 80)
    print()

    so_khach = data['so_khach']
    goi_dv = data['goi_dv']
    summary = data['summary']
    can_mua_items = data['can_mua_items']
    du_kho_items = data['du_kho_items']

    print(f"✅ Đã so sánh tồn kho cho **{so_khach} khách** - **{goi_dv}**")
    print()

    # Bảng CẦN MUA
    if can_mua_items:
        print(f"## 🔴 CẦN MUA ({len(can_mua_items)} loại)")
        print()
        print("| STT | Tên Sản Phẩm | Cần ({}) | Tồn ({}) | Mua ({}) | Mua ({}) | Trạng Thái |".format(
            "đơn vị nhỏ", "đơn vị nhỏ", "đơn vị nhỏ", "đơn vị lớn"
        ))
        print("|-----|--------------|----------|----------|----------|----------|------------|")

        for item in can_mua_items[:20]:  # Top 20
            print("| {} | {} | {} {} | {} {} | {} {} | {} {} | {} |".format(
                item['stt'],
                item['ten'][:40],  # Truncate long names
                int(item['can_nho']),
                item['dvt_nho'],
                int(item['ton_kho_nho']),
                item['dvt_nho'],
                int(item['can_mua_nho']),
                item['dvt_nho'],
                item['can_mua_lon'],
                item['dvt_lon'] if item['dvt_lon'] else 'cái',
                item['trang_thai']
            ))

        if len(can_mua_items) > 20:
            print(f"| ... | ... | ... | ... | ... | ... | ... |")
            print(f"(Hiển thị 20/{len(can_mua_items)} items)")

        print()

    # Bảng ĐỦ KHO
    if du_kho_items:
        print(f"## ✅ ĐỦ KHO ({len(du_kho_items)} loại)")
        print()
        print("| STT | Tên Sản Phẩm | Cần | Tồn | Trạng Thái |")
        print("|-----|--------------|-----|-----|------------|")

        for item in du_kho_items[:10]:  # Top 10
            print("| {} | {} | {} {} | {} {} | {} |".format(
                item['stt'],
                item['ten'][:40],
                int(item['can_nho']),
                item['dvt_nho'],
                int(item['ton_kho_nho']),
                item['dvt_nho'],
                item['trang_thai']
            ))

        if len(du_kho_items) > 10:
            print(f"| ... | ... | ... | ... | ... |")
            print(f"(Hiển thị 10/{len(du_kho_items)} items)")

        print()

    # Tổng kết
    print("📊 **Tổng kết:**")
    print(f"- Tổng loại: **{summary['tong_loai']}**")
    print(f"- CẦN MUA: **{summary['can_mua']}** loại (bao gồm HẾT KHO: {summary['het_kho']} loại)")
    print(f"- ĐỦ KHO: **{summary['du_kho']}** loại")
    print(f"- Matched in inventory: **{summary['matched']}/{summary['tong_loai']}**")
    print(f"- Not found: **{summary['not_found']}/{summary['tong_loai']}**")
    print()

    print("⚠️ **LƯU Ý QUAN TRỌNG:**")
    print("✅ So sánh tồn kho: Dùng **đơn vị nhỏ** (lọ, miếng, ml, etc.)")
    print("✅ Phiếu mua hàng: Dùng **đơn vị lớn** (Hộp, Bịch, etc.) - **ROUNDUP**")
    print("✅ Ví dụ: 0.5 hộp → 1 hộp, 1.3 hộp → 2 hộp")
    print()

    return data


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python inventory_comparison.py <vtth_file> <inventory_file>")
        sys.exit(1)

    vtth_file = sys.argv[1]
    inventory_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None

    # Compare
    result = compare_inventory(vtth_file, inventory_file, output_file)

    # Display
    display_comparison_results(result)
