import json
import math
import sys
import io
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set UTF-8 encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Cấu hình
SPREADSHEET_ID = '1y18Hm-QYHzt5PrdiisPKxmWQidVNEBaG2NthP5Fc800'
SHEET_NAME = 'VTTH'
CREDENTIALS_PATH = r'D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET\config\service-account-key.json'

# Input
so_khach = 101
goi_dv = 'B2B-Gói đồng'

# Mapping cột theo gói
col_mapping = {
    'B2B-Gói cơ bản': 7,   # Cột 7: B2B-Gói cơ bản-Số lượng VTTH sử dụng
    'B2B-Gói đồng': 9,     # Cột 9: B2B-Gói đồng-Số lượng VTTH sử dụng
    'B2B-Gói bạc': 11      # Cột 11: B2B-Gói bạc-Số lượng VTTH sử dụng
}

col_index = col_mapping[goi_dv]

print('🔄 Đang kết nối Google Sheets API...')

# Kết nối Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Đọc dữ liệu
print(f'📖 Đang đọc sheet "{SHEET_NAME}"...')
result = sheet.values().get(
    spreadsheetId=SPREADSHEET_ID,
    range=f'{SHEET_NAME}!A:N'
).execute()

data = result.get('values', [])

if not data:
    print('❌ Không có dữ liệu trong sheet!')
    exit(1)

print(f'✅ Đã đọc {len(data)} dòng dữ liệu')
print(f'📋 Header có {len(data[0])} cột')

# Lọc VTTH theo gói đồng
filtered_items = []
for idx, row in enumerate(data[1:], start=2):  # Bỏ header
    if len(row) <= col_index:
        continue

    # Lấy số lượng VTTH sử dụng (định mức)
    dinh_muc_str = row[col_index] if len(row) > col_index else ''

    # Chỉ lấy nếu có định mức > 0
    try:
        if not dinh_muc_str or dinh_muc_str == '' or dinh_muc_str == '0':
            continue

        dinh_muc = float(dinh_muc_str.replace(',', '.'))

        if dinh_muc <= 0:
            continue

        ten = row[1] if len(row) > 1 else ''
        dvt_lon = row[3] if len(row) > 3 else ''  # Cột 3: Đơn vị tính
        ty_le_str = row[4] if len(row) > 4 else '1'  # Cột 4: Số lượng vật tư trong 1 ĐVT

        # Xử lý tỷ lệ quy đổi (VD: "100 lọ" -> 100)
        if isinstance(ty_le_str, str) and any(char.isdigit() for char in ty_le_str):
            # Tách số ra khỏi chuỗi
            ty_le_quy_doi = float(''.join(filter(lambda x: x.isdigit() or x == '.', ty_le_str.replace(',', '.'))))
            # Lấy đơn vị nhỏ từ chuỗi (VD: "100 lọ" -> "lọ")
            dvt_nho = ''.join(filter(str.isalpha, ty_le_str)).strip()
        else:
            ty_le_quy_doi = float(ty_le_str) if ty_le_str else 1
            dvt_nho = 'cái'

        # Tính toán
        nhu_cau_nho = so_khach * dinh_muc
        so_luong_lon = math.ceil(nhu_cau_nho / ty_le_quy_doi) if ty_le_quy_doi > 0 else math.ceil(nhu_cau_nho)

        filtered_items.append({
            'stt': len(filtered_items) + 1,
            'ten': ten,
            'dinh_muc': dinh_muc,
            'dvt_nho': dvt_nho,
            'dvt_lon': dvt_lon,
            'ty_le_quy_doi': ty_le_quy_doi,
            'nhu_cau_nho': nhu_cau_nho,
            'so_luong_nho': nhu_cau_nho,
            'so_luong_lon': so_luong_lon
        })
    except Exception as e:
        print(f'⚠️ Lỗi dòng {idx} ({row[1] if len(row) > 1 else "?"}): {str(e)}')
        continue

print(f'✅ Đã lọc được {len(filtered_items)} loại VTTH')

# Tạo kết quả
result_data = {
    'so_khach': so_khach,
    'goi_dv': goi_dv,
    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'items': filtered_items,
    'tong_loai': len(filtered_items)
}

# Lưu file
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = r'D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET\workspace\calculations'
output_file = f'{output_dir}\\vtth_{timestamp}.json'

import os
os.makedirs(output_dir, exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(result_data, f, ensure_ascii=False, indent=2)

print(f'💾 Đã lưu vào: {output_file}')

# In kết quả
print('\n' + '='*80)
print(f'✅ ĐÃ TÍNH VTTH CHO {so_khach} KHÁCH - {goi_dv}'.center(80))
print('='*80)
print()
print(f'{'STT':<5} {'Tên Sản Phẩm':<40} {'Định mức':<10} {'Nhu cầu':<15} {'Số lượng':<12} {'ĐVT':<8}')
print(f'{'':>5} {'':>40} {'':>10} {'(đvt nhỏ)':<15} {'(đvt lớn)':<12} {'Lớn':<8}')
print('-'*100)

for item in filtered_items[:30]:  # Hiển thị tất cả
    print(f'{item["stt"]:<5} {item["ten"][:38]:<40} {item["dinh_muc"]:<10.2f} {item["nhu_cau_nho"]:<15.1f} {item["so_luong_lon"]:<12} {item["dvt_lon"]:<8}')

if len(filtered_items) > 30:
    print(f'... và {len(filtered_items) - 30} loại khác')

print()
print('='*80)
print(f'📊 Tổng: {len(filtered_items)} loại VTTH')
print(f'💾 File: {output_file}')
print('='*80)

# Xuất ra JSON để đọc
print('\n--- JSON OUTPUT ---')
print(json.dumps(result_data, ensure_ascii=False, indent=2))
