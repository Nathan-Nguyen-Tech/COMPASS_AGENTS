import sys
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SPREADSHEET_ID = '1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800'
CREDENTIALS_PATH = r'D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET\config\service-account-key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

try:
    print(f"Loading credentials from: {CREDENTIALS_PATH}")
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH, scopes=SCOPES)

    print("Building service...")
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    print("Testing with sheet 'VTTH'...")
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range='VTTH!A1:A5'
    ).execute()

    values = result.get('values', [])
    print(f"✅ Success! Got {len(values)} rows")
    print("Sample data:", values[:3] if len(values) > 0 else "No data")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
