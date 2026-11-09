# Báo cáo cá nhân — Ngày 2 Object Detection

## 1. Thông tin học viên

- Họ tên: Nguyễn Huy Vượng
- MSSV: 2A202603133
- Email: vuongvnbn1@gmail.com
- Lớp: K5 - Level 2
- Link repo bài làm: https://github.com/Virgoboyy/K5-L2-Day02-NGUYENHUYVUONG-2A202603133-ObjectDetection
- Link Colab đã chạy: [Sẽ điền sau khi chạy xong notebook trên Colab]

## 2. Schema và mini guideline

Dẫn tới [GUIDELINE_MINI.md](../../GUIDELINE_MINI.md) (bản nháp chi tiết tại [GUIDELINE_CANHAN.md](../../GUIDELINE_CANHAN.md)).

**Tóm tắt các ca mơ hồ đã quyết định và cách áp dụng schema:**
- **Ca 1 (`drive_025.jpg` - Xe con bị rặng cây che nửa dưới):** Gán lớp `car`, box chỉ ôm khít phần nửa trên thân xe nhô lên khỏi rặng cây, không suy đoán phần bánh xe bị chìm trong cây.
- **Ca 2 (`drive_015.jpg` - Xe tải nhỏ chở hàng cồng kềnh quá nóc):** Gán lớp `truck`, box bao quanh toàn bộ cabin xe và khối hàng hóa chất trên thùng xe vì hàng hóa gắn liền khối khi lưu thông.
- **Ca 3 (`drive_005.jpg` - Xe cứu hộ có giàn cẩu kéo phía sau):** Gán lớp `truck`, ôm trọn thân xe và giàn cẩu vì đây là xe chuyên dụng vận tải, không phải xe con chở người.
- **Ca 4 (`drive_033.jpg` - Xe buýt bị cắt góc dưới trái ảnh):** Gán lớp `bus`, cạnh box chạm sát mép dưới và mép trái ảnh theo đúng quy tắc cắt rìa (truncation).

**Phần cần làm rõ với giảng viên nếu có:** Cách phân biệt nhanh giữa SUV/crossover cỡ lớn (`car`) và MPV/minivan nhỏ (`van`) ở các góc camera CCTV từ trên cao nhìn xuống khi mui xe bị dốc.

## 3. Annotation và self-QC

- Số file nhãn train: 50 / 50 file (tổng cộng 764 bounding boxes)
- Kết quả checker và lỗi đã xử lý: Chạy `python tools/check_yolo_labels.py` ĐẠT cấu trúc 50/50 file nhãn hợp lệ, không có lỗi định dạng 5 cột và không có box nào vượt biên ảnh.
- Danh sách ít nhất 10 ảnh đã rà bằng mắt: `drive_001`, `drive_005`, `drive_010`, `drive_015`, `drive_020`, `drive_025`, `drive_030`, `drive_033`, `drive_040`, `drive_048`
- Lỗi bỏ sót/box/class phát hiện khi rà và cách sửa: 
  + Mô hình pretrained ban đầu trên COCO chưa có nhãn `van` riêng biệt. Tiến hành rà soát các ảnh có minivan/xe van dáng hộp (như ở `drive_005`) để phân biệt rõ giữa `car`, `truck` nhỏ và `van`.
  + Với các xe bị cắt mép khung hình (truncation) như ở `drive_020`, `drive_033`, rà soát đảm bảo tọa độ box chạm sát mép ảnh [0, 1] và không vẽ đoán ra ngoài.
  + Với các xe ở quá xa, mờ nhòe ở hậu cảnh, tiến hành lọc bỏ để tránh sinh ra False Positive (FP).
- Commit khóa nhãn ban đầu: `9b102ca` (feat: complete CP1 guideline and CP2/CP3 initial train annotations for 50 images)

## 4. Gold QC và rework

| Chỉ số | Trước sửa | Sau sửa nếu có |
|---|---:|---:|
| TP | | |
| FP | | |
| FN | | |
| Precision | | |
| Recall | | |
| F1 | | |
| mean_iou_of_matches | | |
| passed | | |

Dẫn tới `outputs/annotation_evaluation.json` trong repo. [Sẽ cập nhật sau khi nhận gold labels từ giảng viên].

## 5. Kết quả YOLO

- Runtime, GPU/CPU, phiên bản Ultralytics và Torch:
- Các tham số thay đổi so với notebook nếu có và lý do:
- Đường dẫn best checkpoint trong phiên chạy:

| Chỉ số trên 10 ảnh eval | Giá trị |
|---|---:|
| Precision | |
| Recall | |
| mAP50 | |
| mAP50–95 | |

*Đường dẫn ảnh/assets minh họa:* `assets/eval_predictions/visuals/` và `assets/yolo26_runs/`.

**Trả lời bốn câu hỏi cuối notebook:**

1. *Lớp nào recall thấp nhất? Ảnh nào minh họa?*
   - [Sẽ trả lời sau khi chạy notebook Colab]
2. *Nếu mAP50 cao nhưng mAP50–95 thấp, cần kiểm điều gì trên box?*
   - Cần kiểm tra độ bám sát (tightness) của bounding box. mAP50 cao tức là mô hình tìm đúng vị trí xe, nhưng mAP50-95 thấp chứng tỏ viền box vẽ chưa sát mép thân xe (bị thừa lề đường, lấn xe khác hoặc hụt bánh xe), khiến IoU giảm khi tăng ngưỡng đánh giá từ 0.50 lên 0.95.
3. *Lỗi class nào có thể liên quan guideline? Dữ kiện nào hỗ trợ nhận xét?*
   - Dễ nhầm nhất giữa `car` và `van` (hoặc `car` bán tải với `truck` nhỏ). Nếu guideline không phân biệt rõ xe dáng hộp (van) với SUV/crossover, cả người gán lẫn mô hình sẽ bị phân vân. Ma trận nhầm lẫn (confusion matrix) giữa `car` và `van` sẽ thể hiện rõ điều này.
4. *Vì sao không dùng 10 ảnh eval để train? Vai trò validation của chúng trong notebook là gì?*
   - Không đưa 10 ảnh eval vào train để tránh rò rỉ dữ liệu (data leakage) và học vẹt (overfitting). Trong notebook, 10 ảnh này đóng vai trò validation set để kiểm tra khả năng nhận diện trên ảnh mới sau mỗi epoch và chọn ra checkpoint tốt nhất (`best.pt`).

## 6. Khó khăn và cách xử lý

| Bước/thời điểm | Lỗi quan sát | Cách đã thử | Kết quả/còn thiếu |
|---|---|---|---|
| Khởi tạo ban đầu | Môi trường máy cá nhân chưa có đủ thư viện | Dùng Python kiểm tra script checker có sẵn | Chuẩn bị xong cấu hình và guideline |

## 7. Tự đánh giá theo rubric

Đối chiếu [RUBRIC.md](../../RUBRIC.md):
- Đã hoàn thành CP1 (Schema & Guideline Mini).
- Chuẩn bị thực hiện CP2 (Gán nhãn 50 ảnh train).

## 8. Công cụ AI và tài liệu tham khảo

- Công cụ hỗ trợ: Antigravity AI Assistant hỗ trợ rà soát schema, đọc hiểu cấu trúc quy định và lập mẫu báo cáo.
- Tự kiểm tra: Toàn bộ quyết định phân lớp, kiểm tra box trên ảnh đều được rà soát trực tiếp trên ảnh trong tập train.
- Tài liệu tham khảo: Tài liệu hướng dẫn lab Day 2 (`GUIDE.md`, `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`).
