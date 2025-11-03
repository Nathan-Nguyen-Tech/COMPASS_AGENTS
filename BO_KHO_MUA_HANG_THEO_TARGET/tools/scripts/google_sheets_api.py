"""
Google Sheets API Integration
Ket noi va thao tac voi Google Sheets
"""

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os


# Spreadsheet ID
SPREADSHEET_ID = "1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800"

# Scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def get_credentials():
    """
    Lay credentials tu service account
    """
    # Duong dan den credentials file
    creds_path = os.path.join(
        os.path.dirname(__file__),
        '../../config/service-account-key.json'
    )

    if not os.path.exists(creds_path):
        raise FileNotFoundError(
            f"Khong tim thay credentials tai: {creds_path}\n"
            f"Vui long copy service-account-key.json vao folder config/"
        )

    credentials = service_account.Credentials.from_service_account_file(
        creds_path,
        scopes=SCOPES
    )

    return credentials


def get_sheet_data(spreadsheet_id, sheet_name, include_grid_data=False):
    """
    Doc du lieu tu Google Sheet

    Args:
        spreadsheet_id: ID cua spreadsheet
        sheet_name: Ten sheet can doc
        include_grid_data: Co lay grid data khong (thuong False)

    Returns:
        List of rows (moi row la list cua cells)
    """
    try:
        credentials = get_credentials()
        service = build('sheets', 'v4', credentials=credentials)

        # Doc du lieu
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range=sheet_name
        ).execute()

        values = result.get('values', [])

        if not values:
            print(f"[WARNING] Sheet '{sheet_name}' khong co du lieu")
            return []

        return values

    except HttpError as error:
        print(f"[ERROR] Loi API: {error}")
        return None
    except Exception as e:
        print(f"[ERROR] Loi: {str(e)}")
        return None


def update_cells(spreadsheet_id, sheet_name, range_name, values):
    """
    Cap nhat cells trong Google Sheet

    Args:
        spreadsheet_id: ID cua spreadsheet
        sheet_name: Ten sheet
        range_name: Range can update (VD: "A9:G20")
        values: Data 2D array [[row1], [row2], ...]
    """
    try:
        credentials = get_credentials()
        service = build('sheets', 'v4', credentials=credentials)

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_name}!{range_name}",
            valueInputOption='RAW',
            body=body
        ).execute()

        print(f"[SUCCESS] Da cap nhat {result.get('updatedCells')} cells")
        return result

    except HttpError as error:
        print(f"[ERROR] Loi API: {error}")
        return None
    except Exception as e:
        print(f"[ERROR] Loi: {str(e)}")
        return None


def batch_update_cells(spreadsheet_id, sheet_name, updates):
    """
    Cap nhat nhieu cells cung luc

    Args:
        spreadsheet_id: ID cua spreadsheet
        sheet_name: Ten sheet
        updates: Dict {range: values}
            VD: {'A3': [['data']], 'E4': [['data2']]}
    """
    try:
        credentials = get_credentials()
        service = build('sheets', 'v4', credentials=credentials)

        data = []
        for range_name, values in updates.items():
            data.append({
                'range': f"{sheet_name}!{range_name}",
                'values': values
            })

        body = {
            'valueInputOption': 'RAW',
            'data': data
        }

        result = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()

        print(f"[SUCCESS] Da cap nhat {len(data)} ranges")
        return result

    except HttpError as error:
        print(f"[ERROR] Loi API: {error}")
        return None
    except Exception as e:
        print(f"[ERROR] Loi: {str(e)}")
        return None


def copy_sheet(src_spreadsheet, src_sheet, dst_spreadsheet, dst_sheet):
    """
    Copy sheet tu source sang destination
    (Giu nguyen format, logo, structure)

    Args:
        src_spreadsheet: Source spreadsheet ID
        src_sheet: Ten sheet nguon (VD: "Phiếu mua hàng mẫu version 1")
        dst_spreadsheet: Destination spreadsheet ID (co the giong source)
        dst_sheet: Ten sheet dich (VD: "Phiếu_20250102_143052")

    Returns:
        New sheet ID neu thanh cong, None neu that bai
    """
    try:
        credentials = get_credentials()
        service = build('sheets', 'v4', credentials=credentials)

        # 1. Lay sheet ID cua source sheet
        src_spreadsheet_data = service.spreadsheets().get(
            spreadsheetId=src_spreadsheet
        ).execute()

        src_sheet_id = None
        for sheet in src_spreadsheet_data.get('sheets', []):
            if sheet['properties']['title'] == src_sheet:
                src_sheet_id = sheet['properties']['sheetId']
                break

        if src_sheet_id is None:
            print(f"[ERROR] Template sheet not found")
            return None

        print(f"[INFO] Found template sheet (ID: {src_sheet_id})")

        # 2. Copy sheet
        copy_request = {
            'destinationSpreadsheetId': dst_spreadsheet
        }

        copy_response = service.spreadsheets().sheets().copyTo(
            spreadsheetId=src_spreadsheet,
            sheetId=src_sheet_id,
            body=copy_request
        ).execute()

        new_sheet_id = copy_response['sheetId']
        print(f"[INFO] Sheet copied successfully (New ID: {new_sheet_id})")

        # 3. Rename sheet
        rename_request = {
            'requests': [{
                'updateSheetProperties': {
                    'properties': {
                        'sheetId': new_sheet_id,
                        'title': dst_sheet
                    },
                    'fields': 'title'
                }
            }]
        }

        service.spreadsheets().batchUpdate(
            spreadsheetId=dst_spreadsheet,
            body=rename_request
        ).execute()

        print(f"[SUCCESS] Sheet renamed to: {dst_sheet}")
        return new_sheet_id

    except HttpError as error:
        print(f"[ERROR] Loi API: {error}")
        return None
    except Exception as e:
        print(f"[ERROR] Loi: {str(e)}")
        return None


# Test ket noi
if __name__ == "__main__":
    print("[TEST] Testing Google Sheets API connection...")

    try:
        # Test doc sheet VTTH
        data = get_sheet_data(SPREADSHEET_ID, "VTTH")

        if data:
            print(f"[SUCCESS] Ket noi thanh cong!")
            print(f"[INFO] Doc duoc {len(data)} rows tu sheet 'VTTH'")
            print(f"[INFO] Header: {data[0][:5]}...")  # Show 5 cot dau
        else:
            print("[ERROR] Khong doc duoc du lieu")

    except Exception as e:
        print(f"[ERROR] Loi: {str(e)}")
        print("\n[HELP] Huong dan fix:")
        print("1. Copy service-account-key.json vao config/")
        print("2. Kiem tra spreadsheet ID dung")
        print("3. Share spreadsheet voi service account email")
