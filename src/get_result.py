from src.extract_content_event import Extract_content
from src.extraction_title_event import Extract_title

class Get_result:
    '''Khai báo các biến cần thiết'''
    def __init__(self):
        self.find_title_and_object = Extract_title()
        self.find_content = Extract_content()
    
    '''Tạo kết quả'''
    def get_result(self, public_date, content):
        #Bài báo
        content_lst = content.strip().split(".")

        # #Danh sách các tiêu đề
        # lst_title = self.find_title_and_object.find_title(content_lst)
        
        # danh sách kết quả
        result = []
        content_to_predict = ""
        if content_lst[0] == "" :
            content_to_predict = content_lst[1]
        else:
            content_to_predict = content_lst[0]

        # for i in range(len(lst_title)):
        index_of_title = content_lst.index(content_to_predict)

        #tìm kiếm nội dung của sự kiện
        content = " ".join(self.find_content.extract_content(content_to_predict, content_lst[index_of_title+1:index_of_title+11]))

        #tìm kiếm các chủ thế, khách thể của sự kiện
        chu_the, khach_the = self.find_title_and_object.find_oject(content_to_predict)

        #tìm kiếm thời gian của sự kiện
        thoi_gian = self.find_title_and_object.find_time(content_to_predict, public_date, content)

        #tìm kiếm địa điểm của sự kiện
        location = self.find_title_and_object.find_location(content_to_predict,content)
        result_dict = {
                # 'Sự kiện' : i + 1,
                'Tiêu đề' : content_to_predict,
                'Chủ thể' : chu_the,
                'Khách thể' : khach_the,
                'Thời gian' : thoi_gian,
                'Địa điểm' : location,
                'Nội dung' : content
        }
        #nếu sự kiện không có nội dung => không lưu sự kiện
        # if result_dict['Nội dung'] == '':
        #     continue
        result.append(result_dict)
        return result