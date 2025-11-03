# Command: /youtube

Trích xuất transcript từ video YouTube để phân tích hoặc lưu trữ.

## Mô Tả

Command này sẽ:
1. Trích xuất transcript (phụ đề) từ video YouTube
2. Lưu vào workspace hoặc context (tùy chọn)
3. Hiển thị transcript hoặc tóm tắt nội dung

## Sử Dụng

```bash
/youtube <url> [--save workspace|context]
```

### Tham Số

- **url** (bắt buộc): URL video YouTube
- **--save** (tùy chọn): Lưu transcript vào đâu
  - `workspace`: Lưu vào workspace/transcripts/
  - `context`: Lưu vào context/transcripts/

## Ví Dụ

```bash
# Trích xuất và hiển thị
/youtube https://www.youtube.com/watch?v=VIDEO_ID

# Trích xuất và lưu vào workspace
/youtube https://www.youtube.com/watch?v=VIDEO_ID --save workspace

# Trích xuất và lưu vào context
/youtube https://www.youtube.com/watch?v=VIDEO_ID --save context
```

## Use Cases

### 1. Học Về Google Sheets API
```bash
/youtube https://www.youtube.com/watch?v=vISRn5qFrkM --save context
```
Lưu transcript tutorial về Google Sheets API vào context để tham khảo.

### 2. Training Materials
```bash
/youtube https://www.youtube.com/watch?v=TRAINING_VIDEO --save workspace
```
Lưu transcript video đào tạo về quy trình mua hàng.

### 3. Quick Reference
```bash
/youtube https://www.youtube.com/watch?v=DEMO_VIDEO
```
Xem nhanh transcript để tìm thông tin.

## Output

```markdown
✅ Đã trích xuất transcript từ YouTube

📹 Video: [Video Title]
🔗 URL: https://www.youtube.com/watch?v=VIDEO_ID
⏱️ Thời lượng: 15:30
📝 Số dòng transcript: 245

---

[Transcript content...]

---

💾 Đã lưu vào: workspace/transcripts/video-title-20250202.txt
```

## Notes

- Chỉ hoạt động với video có phụ đề (subtitles/captions)
- Hỗ trợ cả phụ đề tự động và manual
- Transcript được lưu dưới dạng text file
- Tên file tự động tạo từ video title + timestamp

## Related

- Research agent có thể phân tích transcript
- Dùng để học về Google Sheets API, Python, v.v.
