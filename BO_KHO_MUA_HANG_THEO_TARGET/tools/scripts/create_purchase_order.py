"""
Purchase Order Creator - Tao phieu mua hang tu JSON comparison result
Version 2.0 - Compatible with new JSON structure
"""

import json
import os
import sys
from datetime import datetime

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from google_sheets_api import (
    SPREADSHEET_ID,
    copy_sheet,
    batch_update_cells,
    update_cells,
    get_sheet_data
)


def load_comparison_results(file_path):
    """
    Doc ket qua so sanh tu file JSON
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] File khong ton tai: {file_path}")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"[INFO] Doc ket qua so sanh thanh cong")
        print(f"[INFO] So khach: {data.get('so_khach', 'N/A')}")
        print(f"[INFO] Goi DV: {data.get('goi_dv', 'N/A')}")
        print(f"[INFO] Tong loai: {data['summary']['tong_loai']}")
        print(f"[INFO] Can mua: {data['summary']['can_mua']} loai")
        print(f"[INFO] Het kho: {data['summary']['het_kho']} loai")
        print(f"[INFO] Du kho: {data['summary']['du_kho']} loai")

        return data
    except Exception as e:
        print(f"[ERROR] Loi khi doc file: {e}")
        import traceback
        traceback.print_exc()
        return None


def filter_items_to_purchase(items):
    """
    Loc ra cac items CAN MUA va HET KHO
    """
    can_mua_list = [
        item for item in items
        if item['trang_thai'] in ['CẦN MUA', 'HẾT KHO']
    ]

    print(f"[INFO] Loc duoc {len(can_mua_list)} items CAN MUA/HET KHO")
    return can_mua_list


def create_purchase_order_sheet(spreadsheet_id, comparison_data, template_name):
    """
    Tao phieu mua hang tu TEMPLATE

    WORKFLOW:
    1. COPY template (GIU NGUYEN FORMAT, LOGO)
    2. Doi ten sheet thanh "Phieu_YYYYMMDD_HHMMSS"
    3. Cap nhat header
    4. Dien danh sach CAN MUA (DUNG DON VI LON)
    5. Luu metadata vao 2 sheets: "Phiếu Mua Hàng" va "Chi Tiết Phiếu Mua Hàng"
    """
    print("\n[INFO] BAT DAU TAO PHIEU MUA HANG TU TEMPLATE...")

    # Loc items can mua
    items = comparison_data.get('items', [])
    can_mua_list = filter_items_to_purchase(items)

    if not can_mua_list:
        print("[INFO] Tat ca deu DU KHO, khong can tao phieu!")
        return None

    # Lay thong tin
    so_khach = comparison_data.get('so_khach', 'N/A')
    goi_dv = comparison_data.get('goi_dv', 'N/A')

    # Ten sheet moi
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_sheet_name = f"Phiếu_{timestamp}"

    try:
        # BUOC 1: COPY TEMPLATE
        print(f"\n[BUOC 1/8] Copy template '{template_name}' -> '{new_sheet_name}'")
        new_sheet_id = copy_sheet(
            src_spreadsheet=spreadsheet_id,
            src_sheet=template_name,
            dst_spreadsheet=spreadsheet_id,
            dst_sheet=new_sheet_name
        )

        if not new_sheet_id:
            print("[ERROR] Khong the copy template")
            return None

        print(f"[SUCCESS] Da copy template (Sheet ID: {new_sheet_id})")

        # BUOC 2: Cap nhat HEADER
        print(f"\n[BUOC 2/8] Cap nhat header...")
        header_updates = {
            'A3': [[f"1. Ngày lập: {datetime.now().strftime('%d/%m/%Y')}"]],
            'A4': [["2. Người đề nghị: Phòng Xét Nghiệm"]],
            'E4': [["Phòng ban: Phòng XN"]],
            'A5': [[f"3. Nội dung: Mua VTTH cho {so_khach} khách - {goi_dv}"]]
        }

        batch_update_cells(spreadsheet_id, new_sheet_name, header_updates)
        print("[SUCCESS] Da cap nhat header")

        # BUOC 3: Chuan bi du lieu (DUNG DON VI LON + ROUNDUP)
        print(f"\n[BUOC 3/8] Chuan bi du lieu...")
        DATA_START_ROW = 9  # Bat dau tu row 9

        data_rows = []
        for idx, item in enumerate(can_mua_list):
            # CRITICAL: Dung don vi lon da ROUNDUP
            so_luong_lon = item['can_mua_lon']
            dvt_lon = item['dvt_lon'] if item['dvt_lon'] else 'cai'

            row = [
                idx + 1,                    # STT
                item['ten'],               # Ten hang
                "",                         # Merge voi B
                "",                         # Quy cach
                dvt_lon,                   # DVT LON
                int(so_luong_lon),         # So luong (da ROUNDUP)
                f"Phục vụ {so_khach} khách - {goi_dv}"  # Muc dich
            ]
            data_rows.append(row)

        print(f"[INFO] Chuan bi {len(data_rows)} items")

        # BUOC 4: Ghi du lieu vao sheet
        print(f"\n[BUOC 4/8] Ghi du lieu vao sheet...")
        end_row = DATA_START_ROW + len(data_rows) - 1
        update_cells(
            spreadsheet_id,
            new_sheet_name,
            f"A{DATA_START_ROW}:G{end_row}",
            data_rows
        )
        print(f"[SUCCESS] Da dien {len(data_rows)} items vao phieu")

        # BUOC 5: Tinh tong so luong
        print(f"\n[BUOC 5/8] Tinh toan tong ket...")
        tong_so_luong_lon = sum(item['can_mua_lon'] for item in can_mua_list)
        print(f"[INFO] Tong so luong: {int(tong_so_luong_lon)} (don vi lon)")

        # BUOC 6: Luu metadata vao sheet "Phiếu Mua Hàng"
        print(f"\n[BUOC 6/8] Luu metadata vao 'Phiếu Mua Hàng'...")
        save_metadata_to_phieu_mua_hang(
            spreadsheet_id,
            new_sheet_name,
            so_khach,
            goi_dv,
            can_mua_list,
            tong_so_luong_lon
        )

        # BUOC 7: Luu chi tiet vao sheet "Chi Tiết Phiếu Mua Hàng"
        print(f"\n[BUOC 7/8] Luu chi tiet vao 'Chi Tiết Phiếu Mua Hàng'...")
        save_details_to_chi_tiet_sheet(
            spreadsheet_id,
            new_sheet_name,
            so_khach,
            goi_dv,
            can_mua_list
        )

        # BUOC 8: Tao ket qua
        print(f"\n[BUOC 8/8] Hoan thanh...")
        sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit#gid={new_sheet_id}"

        result = {
            'success': True,
            'sheet_name': new_sheet_name,
            'sheet_id': new_sheet_id,
            'sheet_url': sheet_url,
            'summary': {
                'so_khach': so_khach,
                'goi_dv': goi_dv,
                'so_loai_hang': len(can_mua_list),
                'tong_sl_lon': int(tong_so_luong_lon),
                'ngay_lap': datetime.now().strftime("%d/%m/%Y")
            },
            'items_count': len(can_mua_list)
        }

        return result

    except Exception as e:
        print(f"\n[ERROR] Loi khi tao phieu: {e}")
        import traceback
        traceback.print_exc()
        return None


def save_metadata_to_phieu_mua_hang(spreadsheet_id, sheet_name, so_khach, goi_dv, can_mua_list, tong_sl):
    """
    Luu metadata vao sheet "Phiếu Mua Hàng"
    """
    try:
        # Doc sheet de tim row tiep theo
        data = get_sheet_data(spreadsheet_id, "Phiếu Mua Hàng")
        next_row = len(data) + 1 if data else 2

        # Tao metadata row
        metadata = [[
            sheet_name,                                      # Ten phieu
            datetime.now().strftime("%d/%m/%Y"),            # Ngay lap
            "Phòng Xét Nghiệm",                             # Nguoi de nghi
            "Phòng XN",                                     # Phong ban
            "VTTH",                                         # Loai hang
            so_khach,                                       # So khach
            goi_dv,                                         # Goi dich vu
            f"Mua VTTH cho {so_khach} khách - {goi_dv}",   # Noi dung
            len(can_mua_list),                              # So loai hang
            int(tong_sl),                                   # Tong so luong
            "Đã tạo",                                       # Trang thai
            "Copy từ template, dùng đơn vị lớn (ROUNDUP)", # Ghi chu
            "",                                             # Reserved
            ",".join([item['ten'] for item in can_mua_list[:10]])  # Top 10 items
        ]]

        # Update
        update_cells(
            spreadsheet_id,
            "Phiếu Mua Hàng",
            f"A{next_row}:N{next_row}",
            metadata
        )

        print(f"[SUCCESS] Da luu metadata vao row {next_row}")
        return True

    except Exception as e:
        print(f"[WARNING] Khong the luu metadata: {e}")
        return False


def save_details_to_chi_tiet_sheet(spreadsheet_id, sheet_name, so_khach, goi_dv, can_mua_list):
    """
    Luu chi tiet vao sheet "Chi Tiết Phiếu Mua Hàng"
    """
    try:
        # Doc sheet de tim row tiep theo
        data = get_sheet_data(spreadsheet_id, "Chi Tiết Phiếu Mua Hàng")
        next_row = len(data) + 1 if data else 2

        # Tao chi tiet rows
        chi_tiet = []
        for item in can_mua_list:
            chi_tiet.append([
                item['ten'],                                # Ten hang
                sheet_name,                                 # Ten phieu
                int(item['can_mua_lon']),                  # So luong (don vi lon)
                item['dvt_lon'] if item['dvt_lon'] else 'cai',  # DVT
                "",                                         # Don gia (de trong)
                f"Phục vụ {so_khach} khách - {goi_dv}",   # Muc dich
                "", "", ""                                  # Reserved
            ])

        # Update
        end_row = next_row + len(chi_tiet) - 1
        update_cells(
            spreadsheet_id,
            "Chi Tiết Phiếu Mua Hàng",
            f"A{next_row}:I{end_row}",
            chi_tiet
        )

        print(f"[SUCCESS] Da luu {len(chi_tiet)} items vao rows {next_row}-{end_row}")
        return True

    except Exception as e:
        print(f"[WARNING] Khong the luu chi tiet: {e}")
        return False


def display_result(result):
    """
    Hien thi ket qua tao phieu
    """
    print("\n" + "="*100)
    print("[SUCCESS] DA TAO PHIEU MUA HANG THANH CONG!")
    print("="*100)

    print(f"\nThong tin phieu:")
    print(f"- Ten sheet: {result['sheet_name']}")
    print(f"- Link: {result['sheet_url']}")

    print(f"\nTom tat:")
    print(f"- So luong mat hang: {result['summary']['so_loai_hang']}")
    print(f"- Tong SL can mua: {result['summary']['tong_sl_lon']} (don vi lon - da ROUNDUP)")
    print(f"- Goi dich vu: {result['summary']['goi_dv']}")
    print(f"- So khach hang: {result['summary']['so_khach']}")

    print(f"\n[LUU Y QUAN TRONG]")
    print("- So sanh ton kho: Dung don vi nho (lo, mieng)")
    print("- Phieu mua hang: Dung don vi lon (hop) - ROUNDUP")
    print("- Vi du: 0.5 hop -> 1 hop, 1.3 hop -> 2 hop")

    print(f"\nURL: {result['sheet_url']}")
    print("="*100)


def save_result_to_file(result, output_dir="workspace/purchase-orders"):
    """
    Luu ket qua ra file JSON
    """
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"purchase_order_{timestamp}.json")

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"\n[INFO] Da luu ket qua: {output_file}")
        return output_file
    except Exception as e:
        print(f"[WARNING] Khong the luu ket qua: {e}")
        return None


# CLI
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_purchase_order.py <comparison_json_file>")
        print("Example: python create_purchase_order.py workspace/calculations/inventory_comparison_20251102_194455.json")
        sys.exit(1)

    comparison_file = sys.argv[1]
    template_name = "Phiếu mua hàng mẫu version 1"

    # Load comparison results
    print("\n" + "="*100)
    print("PURCHASE ORDER CREATOR - TAO PHIEU MUA HANG TU DONG")
    print("="*100)

    comparison_data = load_comparison_results(comparison_file)
    if not comparison_data:
        sys.exit(1)

    # Create purchase order
    result = create_purchase_order_sheet(SPREADSHEET_ID, comparison_data, template_name)

    if result and result['success']:
        # Display result
        display_result(result)

        # Save result to file
        save_result_to_file(result)

        print("\n[SUCCESS] HOAN TAT!")
    else:
        print("\n[ERROR] THAT BAI - Khong the tao phieu mua hang")
        sys.exit(1)
