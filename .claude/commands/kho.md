# Kho - Hệ thống Mua Hàng Tự Động

Bạn đang gọi agent **BO_KHO_MUA_HANG_THEO_TARGET**.

## Context

Agent này giúp:
- Tính toán nhu cầu VTTH và Hóa Chất
- So sánh với tồn kho
- Tạo phiếu mua hàng tự động trong Google Sheets

## Working Directory

Thay đổi working directory sang project:
```
cd BO_KHO_MUA_HANG_THEO_TARGET
```

## Các lệnh có sẵn

Sau khi vào folder, bạn có thể dùng:
- `/tinh-vtth` - Tính VTTH cho số khách
- `/tinh-hoa-chat` - Tính hóa chất
- `/so-sanh-kho` - So sánh với file tồn kho
- `/tao-phieu` - Tạo phiếu mua hàng

## Instructions

1. Chuyển working directory: `cd BO_KHO_MUA_HANG_THEO_TARGET`
2. Hỏi user muốn làm gì (tính VTTH, hóa chất, hoặc tạo phiếu)
3. Thực hiện workflow tương ứng

Bắt đầu bằng cách hỏi user: "Bạn muốn làm gì hôm nay?"
