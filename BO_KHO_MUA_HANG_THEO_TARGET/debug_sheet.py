import json
import sys
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Cấu hình
SPREADSHEET_ID = '1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800'
SHEET_NAME = 'VTTH'
CREDENTIALS_PATH = r'D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET\config\service-account-key.json'

# Kết nối Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Đọc dữ liệu
result = sheet.values().get(
    spreadsheetId=SPREADSHEET_ID,
    range=f'{SHEET_NAME}!A:N'
).execute()

data = result.get('values', [])

print(f'Tổng số dòng: {len(data)}')
print(f'\nHeader (dòng 1):')
for idx, col in enumerate(data[0]):
    print(f'  Cột {idx}: {col}')

print(f'\nDòng 2 (mẫu dữ liệu):')
if len(data) > 1:
    row = data[1]
    print(f'  Số cột: {len(row)}')
    for idx, val in enumerate(row):
        print(f'  Cột {idx}: {val}')

print(f'\n--- KIỂM TRA CỘT 12 (Gói đồng) ---')
print(f'Giá trị ở các dòng:')
for idx, row in enumerate(data[1:11], start=2):  # Kiểm tra 10 dòng đầu
    if len(row) > 12:
        print(f'Dòng {idx}: Tên={row[1] if len(row) > 1 else ""}, Cột 12="{row[12]}" (len={len(row[12])})')
    else:
        print(f'Dòng {idx}: Chỉ có {len(row)} cột')

print(f'\n--- KIỂM TRA TẤT CẢ GIÁ TRỊ ĐỘC NHẤT Ở CỘT 12 ---')
unique_values = set()
for row in data[1:]:
    if len(row) > 12:
        unique_values.add(row[12])

print(f'Các giá trị độc nhất ở cột 12:')
for val in sorted(unique_values):
    print(f'  "{val}" (len={len(val)})')
