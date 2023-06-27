# -*- coding: utf-8 -*-
from extract_content_event import Extract_content
from sklearn.metrics.pairwise import cosine_similarity
import time

class check_duplicate_event_vosint:
    def __init__(self):
        self.extract = Extract_content()
    
    def check_duplicate_ev(self, root_event, event_need_compare):
        # su_kien_trung = []
        score = cosine_similarity(self.extract.get_embeddings([event_need_compare['Tiêu đề']]),self.extract.get_embeddings([root_event['Tiêu đề']]))
        #print(round(score[0][0], 2))
        if score[0][0] >= 0.75:
            # su_kien_trung.append(True)
            return 1
        elif 0.5 <= score[0][0] < 0.8:
            if event_need_compare['Chủ thể'] == root_event['Chủ thể'] and event_need_compare['Khách thể'] == root_event['Khách thể']:
                return 1
            else:
                return 0
        else:
            return 0
        # if any(su_kien_trung) == True:
        #     return "Bài báo có sự kiện trùng với sự kiện gốc"
        # else:
        #     return "Bài báo không có sự kiện trùng với sự kiện gốc"
        

if __name__ == "__main__":
    event_root = {'Sự kiện': 1, 
                  'Tiêu đề': 'Lý do Harry vội về Mỹ sau lễ đăng quang của Vua Charles III', 
                  'Chủ thể': 'Harry', 
                  'Khách thể': 'Vua Charles III', 
                  'Thời gian': 'Ngày 6/5', 
                  'Địa điểm': 'Mỹ', 
                  'Nội dung': 'Harry đến Anh dự lễ đăng quang của vua cha rồi bay về Mỹ 28 tiếng sau đó để dự sinh nhật con trai, thể hiện hình ảnh một người bố giàu tình yêu thương. Khoảng 28 tiếng sau khi hạ cánh ở London để dự lễ đăng quang của bố là Vua Charles III ngày 6/5, Harry gấp rút thu dọn đồ đạc để về Mỹ đoàn tụ cùng vợ Meghan Markle và hai con. Trong suốt thời gian diễn ra lễ đăng quang, Công tước xứ Sussex không chụp ảnh cùng bất kỳ thành viên cấp cao nào trong Hoàng gia. Theo Sky News, trong lúc hoàng gia Anh tham gia tiệc mừng đăng quang của Vua Charles III, Harry đã bay về nhà ở Montecito, California, Mỹ vào tối cùng ngày để kịp dự lễ sinh nhật thứ tư của con trai là Hoàng tử Archie.'}

    paper = {'Sự kiện': 1, 'Tiêu đề': 'Hoàng tử Harry về Mỹ ngay sau lễ đăng quang của Vua Charles III.', 'Chủ thể': 'Harry, Mỹ', 'Khách thể': 'Vua Charles III', 'Thời gian': 'datetime.datetime(2023, 5, 12, 15, 30)', 'Địa điểm': 'Không phát hiện địa điểm', 'Nội dung': 'VTV.vn - Hoàng tử Harry vội vã rời London chưa đầy một giờ sau khi lễ đăng quang của cha anh, Vua Charles III, kết thúc vào thứ Bảy. Theo nguồn tin của Page Six, Công tước xứ Sussex đã vội vã trở về California để về kịp sinh nhật lần thứ 4 của con trai - Hoàng tử Archie.'}
    
    check_duplicate = check_duplicate_event_vosint()
    start = time.time()
    result = check_duplicate.check_duplicate_ev(event_root, paper)
    print(result)
    print("Time :",time.time() - start)