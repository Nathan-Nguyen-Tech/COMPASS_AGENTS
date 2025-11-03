import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

file_path = r'C:\Users\nguye\Downloads\Tong_hop_ton_kho (1).xlsx'

# Đọc 10 dòng đầu
df = pd.read_excel(file_path, header=None, nrows=10)

print("Cấu trúc file tồn kho:")
print("="*80)

for i, row in df.iterrows():
    print(f"Row {i}: {list(row)}")

print("\n" + "="*80)
print(f"Tổng số cột: {len(df.columns)}")
