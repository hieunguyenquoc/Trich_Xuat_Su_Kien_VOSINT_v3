# -*- coding: utf-8 -*-
from src.get_result import Get_result
import time
from datetime import datetime

get_result = Get_result()

if __name__ == '__main__':
    
    content = """
Lý do Harry vội về Mỹ sau lễ đăng quang của Vua Charles III.
Harry đến Anh dự lễ đăng quang của vua cha rồi bay về Mỹ 28 tiếng sau đó để dự sinh nhật con trai, thể hiện hình ảnh một người bố giàu tình yêu thương.

Khoảng 28 tiếng sau khi hạ cánh ở London để dự lễ đăng quang của bố là Vua Charles III ngày 6/5, Harry gấp rút thu dọn đồ đạc để về Mỹ đoàn tụ cùng vợ Meghan Markle và hai con. Trong suốt thời gian diễn ra lễ đăng quang, Công tước xứ Sussex không chụp ảnh cùng bất kỳ thành viên cấp cao nào trong Hoàng gia.

Theo Sky News, trong lúc hoàng gia Anh tham gia tiệc mừng đăng quang của Vua Charles III, Harry đã bay về nhà ở Montecito, California, Mỹ vào tối cùng ngày để kịp dự lễ sinh nhật thứ tư của con trai là Hoàng tử Archie.

Kristen Meinzer, chuyên gia về hoàng gia Anh, nhận định sự xuất hiện của Harry tại lễ đăng quang Vua Charles và hành trình vội vã trở về Mỹ cho thấy anh muốn xuất hiện bên cạnh những người quan trọng nhất vào dịp trọng đại của họ, cả ở Anh lẫn ở Mỹ.

"Tôi thấy không có gì bất thường khi Harry bay về Anh dự sự kiện trọng đại của cha, rồi về nhà bên gia đình vào dịp sinh nhật thứ tư của con trai. Phân chia thời gian cho những người quan trọng là điều mà tất cả chúng ta đều làm", bà giải thích. "Harry không coi thường nghĩa vụ của mình và cũng không phản bội ai. Anh tìm cách để làm một người cha tốt và một người con trung hiếu".
Vợ chồng Harry - Meghan rời hoàng gia Anh và chuyển tới Mỹ sinh sống từ năm 2020. Hai người từ đó viết sách, làm phim tài liệu chứa một số nội dung chỉ trích hoàng gia Anh. Đây là lần đầu Harry gặp lại gia đình sau khi ra mắt hồi ký Spare, tiết lộ nhiều nội dung nhạy cảm và mâu thuẫn với anh trai William.

Nhà sử học hoàng gia Marlene Koenig cho rằng quyết định dự lễ đăng quang bất chấp nỗi bất hòa cho thấy Harry nhận thức được tầm quan trọng của việc có mặt trong ngày quan trọng nhất đời vua cha.

"Đây không phải lúc hòa giải. Đây là ngày của Vua Charles III, Harry nhận ra mình cần phải ở đó vì bố", bà Koenig nói.

Điện Buckingham và vợ chồng Harry - Meghan không bình luận về quyết định rời Anh vội vã của Công tước xứ Sussex.

Giới chuyên gia về hoàng gia Anh cũng cho rằng quyết định không dự lễ đăng quang của Meghan Markle là một chiến lược thông minh của hai vợ chồng. Bà Meinzer cho biết điều này thể hiện họ phối hợp tốt thế nào để vừa làm tròn bổn phận với hoàng gia, vừa chăm lo cho gia đình riêng.

"Quyết định để Harry về Anh và Meghan ở nhà với các con vào ngày sinh nhật Archie là một cách phân chia nhiệm vụ tuyệt vời. Họ cũng phải làm những điều tốt nhất cho gia đình và sức khỏe tinh thần của họ", bà nói.

    """
    custom_datetime = datetime(2023, 5, 11, 0, 0, 0)
    start = time.time()
    print(get_result.get_result(custom_datetime,content))
    print("Time :",time.time() - start)

