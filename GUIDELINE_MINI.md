# Mini guideline — bài làm cá nhân

> Điền nội dung này trước khi bắt đầu gán nhãn. Giữ lại các quyết định sau khi self-QC.

## Định nghĩa lớp

| Lớp | Định nghĩa của bạn | Ví dụ/điểm phân biệt |
| --- | --- | --- |
| `car` | Xe con 4-7 chỗ chở người, xe gia đình hoặc xe bán tải nhỏ. | Sedan, SUV, hatchback, taxi, xe bán tải (pickup). Khác `van` ở chỗ đầu xe hoặc đuôi xe phân tách rõ ràng, không phải thân hộp một khối. |
| `truck` | Xe tải chở hàng hóa từ cỡ trung đến lớn. | Xe tải thùng, xe ben chở vật liệu, xe bồn, xe đầu kéo container. Dễ nhận diện nhờ thùng chở hàng riêng biệt phía sau và cabin cao. |
| `bus` | Xe chở khách công cộng hoặc xe du lịch cỡ lớn. | Xe buýt nội đô (kể cả xe buýt dài 2 toa), xe khách liên tỉnh. Thân xe to dài, nhiều cửa đón trả khách, to hơn hẳn minivan. |
| `van` | Xe khoang kín dáng hộp (monovolume), chở người hoặc chở hàng nhẹ. | Minivan gia đình, xe van chở bưu kiện, xe cấp cứu. Khác `car` ở thân xe vuông vức từ đầu tới đuôi, trần cao, đuôi thẳng đứng; khác `bus` vì nhỏ gọn hơn nhiều. |

## Quy tắc chung

- **Box bám sát vật thể nghĩa là:** Vẽ ôm khít phần thân xe nhìn thấy (gồm cả gương, bánh xe sát mặt đường). Không kéo thừa ra đường, vỉa hè hay lấn sang xe bên cạnh.
- **Vật thể bị che khuất:** Nếu bị xe khác hoặc cây/cột che một phần nhưng vẫn nhìn ra loại xe thì vẽ bọc quanh phần nhìn thấy. Nếu bị cột đèn mỏng cắt ngang thì vẽ 1 box trùm cả xe.
- **Vật thể bị cắt bởi rìa ảnh:** Vẽ khít phần xe trong ảnh, mép box chạm đúng mép ảnh. Tuyệt đối không kéo box tràn ra ngoài mép và không đoán phần xe bị khuất.
- **Vật thể rất nhỏ/mơ hồ:** Xe ở quá xa, mờ nhòe không phân biệt được là car, van hay truck thì **bỏ qua, không gán** để tránh gán sai.

## Ghi lại quyết định cho ít nhất ba ca mơ hồ

| Ảnh | Tình huống | Quyết định cuối | Lý do theo schema |
| --- | --- | --- | --- |
| `drive_025.jpg` | Hàng xe con ở làn đối diện bị dải phân cách trồng cây bụi rậm che lấp toàn bộ bánh xe và nửa dưới thân xe. | Gán `car`, box chỉ ôm khít phần nửa trên thân xe nhìn thấy được nhô lên khỏi rặng cây. | Tuân thủ quy tắc che khuất (occlusion): chỉ vẽ box bao quanh phần nhìn thấy được, không cố đoán phần bánh xe bị chìm sâu trong bụi cây. |
| `drive_015.jpg` | Xe tải nhỏ (light truck) chở nhiều bao tải hàng chất cao vượt nóc cabin đang chạy ban đêm. | Gán `truck`, box bao quanh toàn bộ cabin xe và phần hàng hóa chất trên thùng xe. | Đây là xe tải chở hàng thương mại (`truck`). Hàng hóa trên thùng xe gắn liền khối với phương tiện khi lưu thông nên box phải tính cả khối hàng này. |
| `drive_005.jpg` | Xe cứu hộ/kéo xe màu trắng có cabin nhỏ và giàn cẩu chuyên dụng phía sau đang chạy giữa ngã tư ướt mưa. | Gán `truck`, box ôm sát toàn bộ thân xe và giàn cứu hộ phía sau. | Phương tiện cơ giới chuyên dùng chở/kéo xe thuộc nhóm phương tiện vận tải thương mại (`truck`), không thuộc nhóm xe con chở người (`car`). |
| `drive_033.jpg` | Xe buýt lớn màu đỏ ở góc dưới bên trái bị cắt khung (chỉ thấy phần nóc và nửa thân trước). | Gán `bus`, cạnh dưới và cạnh trái của box chạm sát mép ảnh. | Dù bị cắt rìa ảnh (truncation) nhưng các đặc điểm kích thước, màu sơn và kính xe buýt vẫn rất rõ ràng. Box bám sát phần thấy được và chạm đúng mép ảnh. |
