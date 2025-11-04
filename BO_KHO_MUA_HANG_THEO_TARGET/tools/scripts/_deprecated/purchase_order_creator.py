"""
Purchase Order Creator - Tao phieu mua hang tu dong
"""

import json
import os
import sys
from datetime import datetime
import glob

from google_sheets_api import get_credentials
from googleapiclient.discovery import build


def find_latest_comparison():
    """
    Tim file so sanh moi nhat trong workspace/calculations/
    """
    pattern = "workspace/calculations/comparison_*.json"
    files = glob.glob(pattern)

    if not files:
        return None

    # Sort by modification time, newest first
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]


def load_comparison_results(file_path=None):
    """
    Doc ket qua so sanh tu file JSON
    """
    if not file_path:
        file_path = find_latest_comparison()
        if not file_path:
            print("[ERROR] Khong tim thay file ket qua so sanh")
            print("[HELP] Chay /so-sanh-kho truoc")
            return None

    if not os.path.exists(file_path):
        print(f"[ERROR] File khong ton tai: {file_path}")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"[INFO] Doc ket qua so sanh tu: {file_path}")
        print(f"[INFO] Can mua: {data['summary']['can_mua']} loai")
        print(f"[INFO] Du kho: {data['summary']['du_kho']} loai")

        return data
    except Exception as e:
        print(f"[ERROR] Loi khi doc file: {e}")
        return None


def create_purchase_order_sheet(spreadsheet_id, comparison_data):
    """
    Tao phieu mua hang tu TEMPLATE (giu nguyen logo, format)

    Workflow:
    1. COPY template "Phiếu mua hàng mẫu version 1"
    2. Doi ten sheet thanh "Phiếu_YYYYMMDD_HHMMSS"
    3. Cap nhat header (ngay lap, noi dung)
    4. Dien danh sach CAN MUA vao row 9+ (dung don vi lon)
    """
    print("\n[INFO] Dang tao phieu mua hang tu TEMPLATE...")

    from google_sheets_api import copy_sheet, batch_update_cells, update_cells

    # Ten sheet moi
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_sheet_name = f"Phieu_{timestamp}"

    try:
        # 1. COPY TEMPLATE (GIU NGUYEN LOGO, FORMAT)
        print(f"[INFO] Copy template -> '{new_sheet_name}'")
        new_sheet_id = copy_sheet(
            src_spreadsheet=spreadsheet_id,
            src_sheet="Phiếu mua hàng mẫu version 1",
            dst_spreadsheet=spreadsheet_id,
            dst_sheet=new_sheet_name
        )

        if not new_sheet_id:
            print("[ERROR] Khong the copy template")
            return None

        print(f"[SUCCESS] Da copy template thanh cong (Sheet ID: {new_sheet_id})")

        # 2. Cap nhat HEADER
        print("[INFO] Cap nhat header...")
        header_updates = {
            'A3': [[f"1. Ngày lập: {datetime.now().strftime('%d/%m/%Y')}"]],
            'A4': [["2. Người đề nghị: Phòng Xét Nghiệm"]],
            'E4': [["Phòng ban: Phòng XN"]],
            'A5': [[f"3. Nội dung: Mua VTTH theo yêu cầu phục vụ khách hàng"]]
        }

        batch_update_cells(spreadsheet_id, new_sheet_name, header_updates)
        print("[SUCCESS] Da cap nhat header")

        # 3. Chuan bi du lieu (DUNG DON VI LON + ROUNDUP)
        can_mua = comparison_data['can_mua']
        DATA_START_ROW = 9  # Bat dau tu row 9 (theo template structure)

        data_rows = []
        for idx, item in enumerate(can_mua, 1):
            # DON VI LON - DA ROUNDUP
            so_luong_lon = int(item['can_mua_lon'])
            dvt_lon = item['dvt_lon'] if item['dvt_lon'] else 'cai'

            row = [
                idx,                    # STT
                item['ten'],           # Ten hang
                "",                     # Merge voi B (de trong)
                "",                     # Quy cach
                dvt_lon,               # DVT LON
                so_luong_lon,          # So luong (da ROUNDUP)
                f"CK: {int(item['can_nho'])} {item['dvt_nho']}, TK: {int(item['ton_kho_nho'])} {item['dvt_nho']}"  # Muc dich
            ]
            data_rows.append(row)

        # 4. Ghi du lieu vao sheet
        print(f"[INFO] Ghi {len(data_rows)} items vao sheet...")
        end_row = DATA_START_ROW + len(data_rows) - 1
        update_cells(
            spreadsheet_id,
            new_sheet_name,
            f"A{DATA_START_ROW}:G{end_row}",
            data_rows
        )

        print(f"[SUCCESS] Da dien {len(data_rows)} items vao phieu")

        # URL
        sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit#gid={new_sheet_id}"

        return {
            'sheet_name': new_sheet_name,
            'sheet_id': new_sheet_id,
            'sheet_url': sheet_url,
            'timestamp': timestamp,
            'items_count': len(can_mua),
            'tong_so_luong_lon': sum(item['can_mua_lon'] for item in can_mua)
        }

    except Exception as e:
        print(f"[ERROR] Loi khi tao phieu: {e}")
        import traceback
        traceback.print_exc()
        return None


def save_purchase_order_metadata(po_info, comparison_data):
    """
    Luu metadata phieu mua hang
    """
    os.makedirs('workspace/purchase-orders', exist_ok=True)

    timestamp = po_info['timestamp']
    metadata_file = f"workspace/purchase-orders/po_{timestamp}.json"

    metadata = {
        'timestamp': timestamp,
        'sheet_name': po_info['sheet_name'],
        'sheet_id': po_info['sheet_id'],
        'sheet_url': po_info['sheet_url'],
        'items_count': po_info['items_count'],
        'comparison_file': comparison_data.get('comparison_file', 'N/A'),
        'summary': comparison_data['summary']
    }

    try:
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        print(f"\n[INFO] Da luu metadata: {metadata_file}")
    except Exception as e:
        print(f"[WARNING] Khong the luu metadata: {e}")

    return metadata_file


def display_purchase_order_result(po_info):
    """
    Hien thi ket qua tao phieu mua hang
    """
    print("\n" + "="*100)
    print("[SUCCESS] DA TAO PHIEU MUA HANG TU TEMPLATE!")
    print("="*100)
    print(f"Sheet name: {po_info['sheet_name']}")
    print(f"So loai can mua: {po_info['items_count']}")
    print(f"Tong so luong: {po_info['tong_so_luong_lon']} (don vi lon)")
    print(f"\nURL: {po_info['sheet_url']}")
    print("="*100)
    print("\n[INFO] Phieu da duoc tao bang cach COPY TEMPLATE")
    print("[INFO] Logo, format, cau truc duoc giu nguyen 100%")
    print("[INFO] Chi cap nhat: Header + Du lieu items CAN MUA")
    print("="*100)


# CLI
if __name__ == "__main__":
    from google_sheets_api import SPREADSHEET_ID

    comparison_file = sys.argv[1] if len(sys.argv) > 1 else None

    # Load comparison results
    comparison_data = load_comparison_results(comparison_file)
    if not comparison_data:
        sys.exit(1)

    # Check if there are items to buy
    if comparison_data['summary']['can_mua'] == 0:
        print("\n[INFO] Tat ca deu DU KHO, khong can tao phieu mua hang!")
        sys.exit(0)

    # Create purchase order sheet
    po_info = create_purchase_order_sheet(SPREADSHEET_ID, comparison_data)

    if po_info:
        # Save metadata
        save_purchase_order_metadata(po_info, comparison_data)

        # Display result
        display_purchase_order_result(po_info)
    else:
        print("\n[ERROR] Khong the tao phieu mua hang")
        sys.exit(1)
