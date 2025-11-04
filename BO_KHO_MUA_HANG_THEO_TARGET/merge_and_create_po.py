"""
Merge VTTH and Hoa Chat comparison results and create combined purchase order
"""
import json
import sys
import io
from datetime import datetime

# Set UTF-8 encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read both comparison files
hoa_chat_file = "workspace/calculations/comparison_20251103_130813.json"
vtth_file = "workspace/calculations/comparison_20251103_133421.json"

print(f"[INFO] Đọc file Hóa Chất: {hoa_chat_file}")
with open(hoa_chat_file, 'r', encoding='utf-8') as f:
    hoa_chat_data = json.load(f)

print(f"[INFO] Đọc file VTTH: {vtth_file}")
with open(vtth_file, 'r', encoding='utf-8') as f:
    vtth_data = json.load(f)

# Merge can_mua lists
print("[INFO] Gộp danh sách CẦN MUA...")
combined_can_mua = []

# Add Hóa Chất
for item in hoa_chat_data['can_mua']:
    item['loai'] = 'Hóa Chất'
    combined_can_mua.append(item)

# Add VTTH
for item in vtth_data['can_mua']:
    item['loai'] = 'VTTH'
    combined_can_mua.append(item)

print(f"[SUCCESS] Đã gộp: {len(hoa_chat_data['can_mua'])} Hóa Chất + {len(vtth_data['can_mua'])} VTTH = {len(combined_can_mua)} loại")

# Create combined comparison data
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
combined_data = {
    'timestamp': timestamp,
    'can_mua': combined_can_mua,
    'du_kho': [],
    'summary': {
        'tong_loai': len(combined_can_mua),
        'can_mua': len(combined_can_mua),
        'du_kho': 0
    },
    'note': 'Combined: Hóa Chất + VTTH cho 50 khách - B2B-Gói đồng'
}

# Save combined file
output_file = f"workspace/calculations/comparison_combined_{timestamp}.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=2)

print(f"[SUCCESS] Đã lưu file tổng hợp: {output_file}")
print(f"\n[INFO] Tổng kết:")
print(f"  - Hóa Chất: {len(hoa_chat_data['can_mua'])} loại")
print(f"  - VTTH: {len(vtth_data['can_mua'])} loại")
print(f"  - Tổng cộng: {len(combined_can_mua)} loại")

# Return output file path for next step
print(f"\n{output_file}")
