# -*- coding: utf-8 -*-
import re
from datetime import datetime
import sys

f_dict = open(
    './util/word_date.txt', 'r', encoding='utf-8')


def get_len_str(text: str):
    return len(text.split())

def get_number(text: str)->list:
    regex = "\d{1,}"
    return re.findall(regex,text)

# Đủ ngày thàng năm
def convert_dd_mm_yyyy(text: str, default_datatime: datetime)->datetime:
    try:
        numbers = get_number(text)
        return datetime(day=int(numbers[0]),month=int(numbers[1]),year=int(numbers[2]))
    except Exception as e:
        return default_datatime
    
#Có ngày và tháng
def convert_dd_mm(text: str,default_datatime: datetime)->datetime:
    try:
        now = datetime.now()
        numbers = get_number(text)
        return datetime(day=int(numbers[0]),month=int(numbers[1]),year=now.year)
    except:
        return default_datatime

# Có tháng và năm
def convert_mm_yyyy(text,default_datatime: datetime)->datetime:
    # try:
    #     numbers = get_number(text)
    #     return datetime(day=default_datatime.day,month=int(numbers[0]),year=int(numbers[1]))
    # except Exception as e:
        return default_datatime

# Có ngày tháng
def convert_dd_dd_mm(text:str, default_datatime: datetime)->datetime:
    try:
        now = datetime.now()
        numbers = get_number(text)
        return datetime(day=int(numbers[0]),month=int(numbers[2]),year=now.year)
    except:
        return default_datatime

def get_nearest_date(default_datetime:datetime, entities: list)->datetime:
    min = sys.maxsize
    nearest_date = None
    for entity in entities:
        delta = entity['datetime']-default_datetime
        if abs(delta.days) < min: 
            nearest_date = entity
            min = abs(delta.days)
    return nearest_date

# LOAD TRẠNG TỪ CHỈ THỜI GIAN
tt_dict = dict()
lines = f_dict.readlines()
tt_dict['0'] = '('+'|'.join(sorted(lines[0].strip().split('|'),
                                   key=get_len_str, reverse=True))+')'  # Ngày
tt_dict['1'] = '('+'|'.join(sorted(lines[1].strip().split('|'),
                                   key=get_len_str, reverse=True))+')'  # Tháng
tt_dict['2'] = '('+'|'.join(sorted(lines[2].strip().split('|'),
                                   key=get_len_str, reverse=True))+')'  # Quý
tt_dict['3'] = '('+'|'.join(sorted(lines[3].strip().split('|'),
                                   key=get_len_str, reverse=True))+')'  # Năm


# Thiết đặt các Regex trích xuất thông tin
character = '[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ%0-9\/-]'

list_template_regex = [
    # dd/mm/yyyy 0
    "(%s\s*\d{1,2}\s*[\/.-]\s*\d{1,2}\s*[\/.-]\s*\d{4})(?!%s)" % (tt_dict['0'], character),
    # "(\s*\d{4}\s*-\s*\d{4})(?!%s)" %(character), # yyyy-yyyy
    # mm/yyyy 1
    "(%s\s*\d{1,2}\s*[\/.-]\s*\d{4})(?!%s)" % (tt_dict['1'], character),
    # dd/mm 2
    "(%s\s*\d{1,2}\s*[\/.-]\s*\d{1,2})(?!%s)" % (tt_dict['0'], character),
    # Quý/yyyy 3
    # "(%s\s*[I|II|III|IV]{1,}[\/.-]\s*\d{4})(?!%s)" % (tt_dict['2'], character),
    # ngày dd tháng mm năm yyyy 4
    "(ngày\s*\d{1,2}\s*tháng\s*\d{1,2}\s*năm\s*\d{4})(?!%s)" % (character),
    # Tháng mm năm yyyy 5
    "(tháng\s*\d{1,2}\s*năm\s*\d{4})(?!%s)" % (character),
    # Ngày dd tháng mm 6
    "(ngày\s*\d{1,2}\s*tháng\s*\d{1,2})(?!%s)" % (character),
    # "(%s\s*\d{4})(?!%s)" % (tt_dict['3'], character),  # yyyy
    # từ ngày dd - dd/mm 7
    "(%s\s*\d{1,2}-\d{1,2}\/\d{1,2})(?!%s)" % (tt_dict['0'],character)
]


regex_keyword = "(%s|%s|%s|%s)" % (
    tt_dict['0'], tt_dict['1'], tt_dict['2'], tt_dict['3'])

regex2convert = {
    0: convert_dd_mm_yyyy,
    3: convert_dd_mm_yyyy,
    1: convert_mm_yyyy,
    4: convert_mm_yyyy,
    2: convert_dd_mm,
    5: convert_dd_mm,
    6: convert_dd_dd_mm
}

def get_ner_datetime(text,default_datatime: datetime):
    obj = {}
    obj['text'] = text.strip()
    obj['entities'] = []
    text = text.strip().lower()

    # Bắt Regex theo Forms
    regex = "|".join(list_template_regex)
    # for regex in list_template_regex:
    result = re.finditer(regex, text)
    for iter in result:
        entity = {}
        entity['text'] = iter.group()
        entity['datetime'] = None
        for idx, regex in enumerate(list_template_regex):
            if re.compile(regex).match(entity['text']):
                entity['datetime'] = regex2convert[idx](entity['text'],default_datatime)
                break   
        entity['tag'] = 'DATETIME'
        entity['start_position'] = iter.start()
        entity['end_position'] = iter.end()
        obj['entities'].append(entity)
    print(obj['entities'])
    if get_nearest_date(default_datatime,obj['entities']) is None:
        return default_datatime
    else:
        return get_nearest_date(default_datatime,obj['entities'])['datetime']
    # return obj['entities


# if __name__ == "__main__":
#     default_datetime = datetime(2023,5,11)
#     sentence = "Nhật viện trợ 100 xe quân sự cho Ukraine. Bộ Quốc phòng Nhật Bản thông báo viện trợ 100 xe quân sự cho Ukraine, song chưa công bố số lượng cụ thể từng chủng loại và thời gian chuyển giao. Thứ trưởng Quốc phòng Nhật Bản Toshiro Ino ngày 25/5 trao tài liệu cho Đại sứ Ukraine Sergiy Korsunsky, trong đó liệt kê ba loại phương tiện quân sự mà Tokyo viện trợ cho Kiev là xe bán tải với trọng tải nửa tấn, phương tiện tốc độ cao và phương tiện xử lý vật liệu. Ngoài ra, gói viện trợ còn có 30.000 suất ăn. Chúng tôi hy vọng chiến sự sẽ sớm kết thúc và cuộc sống bình yên quay trở lại. Chúng tôi sẽ hỗ trợ nhiều nhất có thể, ông Ino nói. Cơ quan Mua sắm, Công nghệ và Hậu cần thuộc Bộ Quốc phòng Nhật Bản đang hoàn thiện chi tiết về thời gian bàn giao và số lượng phương tiện cụ thể. Giới chức Nhật Bản công bố gói viện trợ trong bối cảnh chính phủ nước này tìm cách nới lỏng quy định chuyển giao thiết bị quân sự theo chính sách an ninh quốc gia mới, cho phép lực lượng phòng vệ sở hữu năng lực phản công để tung đòn tấn công lãnh thổ quốc gia khác trong tình huống khẩn cấp và các điều kiện đặc biệt. Trong khi nhiều quốc gia đã viện trợ xe tăng chủ lực, tên lửa và tiêm kích cho Ukraine, Nhật Bản chỉ cung cấp các loại trang bị và thiết bị phi sát thương do chính sách cấm chuyển giao vũ khí cho những quốc gia đang tham gia xung đột quân sự. Nhật Bản đã viện trợ áo chống đạn, mũ bảo hiểm, mặt nạ phòng độc, quần áo bảo hộ, máy bay không người lái (UAV) cỡ nhỏ và suất ăn từ khi chiến sự bùng phát tháng 2/2022. Nhật Bản cũng đề nghị điều trị cho binh sĩ Ukraine bị thương tại bệnh viện quân y của nước này. Tổng trị giá các khoản viện trợ Nhật Bản đã chuyển cho Ukraine là 7 tỷ USD. Nhật Bản cũng đồng ý tiếp nhận 2.000 người tị nạn Ukraine, hỗ trợ nhà cửa, việc làm và giáo dục cho họ. Động thái này được đánh giá là hiếm hoi đối với Nhật Bản, quốc gia nổi tiếng với chính sách nhập cư nghiêm ngặt."
#     result = get_ner_datetime(sentence,default_datatime=default_datetime)
#     print(result)
