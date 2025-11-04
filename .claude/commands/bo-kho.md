# Kho - Hệ thống Mua Hàng Tự Động

Bạn đang gọi agent **BO_KHO_MUA_HANG_THEO_TARGET**.

## Context

Agent này giúp:
- Tính toán nhu cầu VTTH và Hóa Chất
- So sánh với tồn kho
- Tạo phiếu mua hàng tự động trong Google Sheets

## 🛠️ AVAILABLE TOOLS & SCRIPTS

**⚠️ CRITICAL: Project này đã có Python scripts sẵn trong `tools/scripts/`**

**LUÔN SỬ DỤNG CÁC SCRIPTS CÓ SẴN TRƯỚC KHI VIẾT CODE MỚI!**

📖 **Xem chi tiết:** [tools/SCRIPTS_GUIDE.md](BO_KHO_MUA_HANG_THEO_TARGET/tools/SCRIPTS_GUIDE.md)

**Canonical scripts:**
- `tools/scripts/calculator.py` - Tính VTTH
- `tools/scripts/calculate_chemicals.py` - Tính Hóa Chất
- `tools/scripts/inventory_comparator.py` - So sánh tồn kho
- `tools/scripts/create_purchase_order.py` - Tạo phiếu mua hàng

**Example usage:**
```bash
cd BO_KHO_MUA_HANG_THEO_TARGET
python tools/scripts/calculator.py
```

## Working Directory

Thay đổi working directory sang project:
```
cd BO_KHO_MUA_HANG_THEO_TARGET
```

## Các lệnh có sẵn

Sau khi vào folder, bạn có thể dùng:
- `/tinh-vtth` - Tính VTTH cho số khách (dùng calculator.py)
- `/tinh-hoa-chat` - Tính hóa chất (dùng calculate_chemicals.py)
- `/so-sanh-kho` - So sánh với file tồn kho (dùng inventory_comparator.py)
- `/tao-phieu` - Tạo phiếu mua hàng (dùng create_purchase_order.py)

## Instructions

1. Chuyển working directory: `cd BO_KHO_MUA_HANG_THEO_TARGET`
2. **Kiểm tra scripts có sẵn trong tools/scripts/ trước**
3. Hỏi user muốn làm gì (tính VTTH, hóa chất, hoặc tạo phiếu)
4. Sử dụng Python scripts tương ứng (KHÔNG tự viết code mới)

Bắt đầu bằng cách hỏi user: "Bạn muốn làm gì hôm nay?"
