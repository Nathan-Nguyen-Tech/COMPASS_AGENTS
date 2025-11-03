# Command: /kho

Menu chính của hệ thống mua hàng tự động.

## Mô Tả

Hiển thị menu tương tác với 3 lựa chọn chính:
1. Tính VTTH
2. Tính Hóa Chất
3. So sánh tồn kho & tạo phiếu

## Sử Dụng

```bash
/kho
```

## Output

```
Xin chào! 👋 Tôi có thể giúp gì?

1️⃣ Tính VTTH
   Tính vật tư tiêu hao theo số khách hàng

2️⃣ Tính Hóa Chất
   Tính hóa chất (bao gồm QC/CALIB) theo số khách hàng

3️⃣ So sánh tồn kho & tạo phiếu
   So sánh với file tồn kho và tạo phiếu mua hàng tự động

---

Chọn số (1, 2 hoặc 3):
```

## Xử Lý User Input

```python
user_choice = input()

if user_choice == "1":
    # Chuyển sang /tinh-vtth
    print("Số lượng khách hàng:")
    so_khach = int(input())
    print("Gói dịch vụ (Enter = B2B-Gói đồng):")
    goi_dv = input() or "B2B-Gói đồng"
    # Execute calculator agent for VTTH

elif user_choice == "2":
    # Chuyển sang /tinh-hoa-chat
    print("Số lượng khách hàng:")
    so_khach = int(input())
    print("Gói dịch vụ (Enter = B2B-Gói đồng):")
    goi_dv = input() or "B2B-Gói đồng"
    # Execute calculator agent for Hóa Chất

elif user_choice == "3":
    # Kiểm tra đã có kết quả tính toán chưa
    if not has_calculation_results():
        print("⚠️ Bạn chưa tính VTTH hoặc Hóa Chất!")
        print("Vui lòng chọn 1 hoặc 2 trước.")
    else:
        print("Đường dẫn file tồn kho (.xlsx hoặc .csv):")
        file_path = input()
        # Execute inventory manager + purchase order creator

else:
    print("❌ Lựa chọn không hợp lệ. Vui lòng chọn 1, 2 hoặc 3.")
```

## Related Commands

- `/tinh-vtth` - Tính VTTH trực tiếp
- `/tinh-hoa-chat` - Tính Hóa Chất trực tiếp
- `/so-sanh-kho` - So sánh tồn kho trực tiếp
- `/tao-phieu` - Tạo phiếu trực tiếp

## Notes

Command này chủ yếu dùng để hướng dẫn user mới. User có kinh nghiệm có thể dùng trực tiếp các commands cụ thể.
