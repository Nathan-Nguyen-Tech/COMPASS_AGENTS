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
CREDENTIALS_PATH = r'D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET\config\service-account-key.json'

# Input
so_khach = 100
goi_dv = 'B2B-Gói đồng'

# Mapping cột theo gói
col_mapping = {
    'B2B-Gói cơ bản': 13,   # Cột 13
    'B2B-Gói đồng': 12,     # Cột 12
    'B2B-Gói bạc': 14       # Cột 14
}

col_index = col_mapping[goi_dv]

print('🔄 Đang kết nối Google Sheets API...')

# Kết nối Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# ⭐ BƯỚC 1: Đọc sheet "Hoa Chat Chi Tiet"
print('📖 Đang đọc sheet "Hoa Chat Chi Tiet"...')
result = sheet.values().get(
    spreadsheetId=SPREADSHEET_ID,
    range='Hoa Chat Chi Tiet!A:O'
).execute()

chi_tiet_data = result.get('values', [])

if not chi_tiet_data:
    print('❌ Không có dữ liệu trong sheet "Hoa Chat Chi Tiet"!')
    exit(1)

print(f'✅ Đã đọc {len(chi_tiet_data)} dòng dữ liệu')

# ⭐ BƯỚC 2: Lọc hóa chất theo điều kiện
# Cột 5: Loại hóa chất (phải = "Chạy mẫu")
# Cột 12/13/14: Gói (phải = "x")
filtered_items = []
for idx, row in enumerate(chi_tiet_data[1:], start=2):  # Bỏ header
    if len(row) <= col_index:
        continue

    try:
        loai_hc = row[5] if len(row) > 5 else ''
        goi_mark = row[col_index] if len(row) > col_index else ''

        # Điều kiện lọc
        if loai_hc == 'Chạy mẫu' and goi_mark == 'x':
            ten = row[3] if len(row) > 3 else ''  # Cột 3: Tên HC
            lo_per_hop = float(row[9]) if len(row) > 9 and row[9] else 1  # Cột 9: Lọ/hộp
            test_per_lo = float(row[10]) if len(row) > 10 and row[10] else 0  # Cột 10: Test/lọ

            filtered_items.append({
                'ten': ten,
                'lo_per_hop': lo_per_hop,
                'test_per_lo': test_per_lo
            })
    except Exception as e:
        print(f'⚠️ Lỗi dòng {idx}: {str(e)}')
        continue

print(f'✅ Đã lọc được {len(filtered_items)} loại hóa chất')

if not filtered_items:
    print('❌ Không tìm thấy hóa chất nào!')
    exit(1)

# ⭐ BƯỚC 3: Đọc sheet "Hoa Chat" để tra cứu QC/CALIB
print('📖 Đang đọc sheet "Hoa Chat" để tra cứu QC/CALIB...')
result2 = sheet.values().get(
    spreadsheetId=SPREADSHEET_ID,
    range='Hoa Chat!A:Z'
).execute()

hoa_chat_data = result2.get('values', [])
print(f'✅ Đã đọc {len(hoa_chat_data)} dòng từ sheet "Hoa Chat"')

# ⭐ BƯỚC 4: Tính toán
results = []
for item in filtered_items:
    ten = item['ten']
    lo_per_hop = item['lo_per_hop']
    test_per_lo = item['test_per_lo']

    # Tra cứu QC/CALIB từ sheet "Hoa Chat"
    test_qc = 2      # Mặc định
    test_calib = 4   # Mặc định

    for qc_row in hoa_chat_data[1:]:
        ten_qc = qc_row[1] if len(qc_row) > 1 else ''
        if ten_qc.strip().lower() == ten.strip().lower():
            test_qc = int(float(qc_row[16])) if len(qc_row) > 16 and qc_row[16] else 2
            test_calib = int(float(qc_row[24])) if len(qc_row) > 24 and qc_row[24] else 4
            break

    # Đặc biệt: HC không có QC/CALIB
    keywords_no_qc = ['dung dịch', 'dung dich', 'wash', 'tiểu', 'tieu', 'diluit', 'lyse', 'clean', 'dye']
    if any(keyword in ten.lower() for keyword in keywords_no_qc):
        test_qc = 0
        test_calib = 0

    # Tính toán
    test_khach = so_khach
    tong_test = test_khach + test_qc + test_calib

    if test_per_lo > 0:
        so_lo = math.ceil(tong_test / test_per_lo)
        so_hop = math.ceil(so_lo / lo_per_hop)
    else:
        so_lo = 1
        so_hop = 1

    # Xác định đơn vị lớn
    if '20L' in ten or '20l' in ten.lower():
        dvt_lon = 'Thùng'
    elif any(k in ten.lower() for k in ['dung dịch', 'dung dich', 'lyse', 'clean']):
        dvt_lon = 'Chai'
    else:
        dvt_lon = 'Hộp'

    results.append({
        'stt': len(results) + 1,
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

# Tạo kết quả
result_data = {
    'type': 'HOA_CHAT',
    'so_khach': so_khach,
    'goi_dv': goi_dv,
    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'items': results,
    'tong_loai': len(results)
}

# Lưu file
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = r'D:\Compass_Coding\COMPASS_AGENTS\BO_KHO_MUA_HANG_THEO_TARGET\workspace\calculations'
output_file = f'{output_dir}\\hoa_chat_{timestamp}.json'

import os
os.makedirs(output_dir, exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(result_data, f, ensure_ascii=False, indent=2)

print(f'💾 Đã lưu vào: {output_file}')

# In kết quả
print('\n' + '='*120)
print(f'✅ ĐÃ TÍNH HÓA CHẤT CHO {so_khach} KHÁCH - {goi_dv}'.center(120))
print('='*120)
print()
print(f'{'STT':<5} {'Tên Hóa Chất':<45} {'Test/lọ':<10} {'KH':<6} {'QC':<6} {'Cal':<6} {'Tổng':<8} {'Lọ':<6} {'ĐVT Lớn':<12}')
print('-'*120)

for item in results:
    print(f'{item["stt"]:<5} {item["ten"][:43]:<45} {item["test_per_lo"]:<10.0f} {item["test_khach"]:<6} {item["test_qc"]:<6} {item["test_calib"]:<6} {item["tong_test"]:<8} {item["so_luong_nho"]:<6} {item["so_luong_lon"]:<4} {item["dvt_lon"]:<8}')

print()
print('='*120)
print(f'📊 Tổng: {len(results)} loại hóa chất')
print(f'💾 File: {output_file}')
print('='*120)

# Xuất ra JSON để đọc
print('\n--- JSON OUTPUT ---')
print(json.dumps(result_data, ensure_ascii=False, indent=2))
