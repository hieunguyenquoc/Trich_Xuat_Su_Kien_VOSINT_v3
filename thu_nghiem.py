import re
import datetime
f_dict = open(
    './util/word_date.txt', 'r', encoding='utf-8')


def get_len_str(text: str):
    return len(text.split())

def get_number(text: str)->list:
    regex = "\d{1,}"
    return re.findall(regex,text)

# Đủ ngày thàng năm
def convert_dd_mm_yyyy(text: str)->datetime:
    numbers = get_number(text)
    return datetime.datetime(day=int(numbers[0]),month=int(numbers[1]),year=int(numbers[2]))

#Có ngày và tháng
def convert_dd_mm(text: str)->datetime:
    now = datetime.datetime.now()
    numbers = get_number(text)
    return datetime.datetime(day=int(numbers[0]),month=int(numbers[1]),year=now.year)

# Có tháng và năm
def convert_mm_yyyy(text)->datetime:
    numbers = get_number(text)
    return datetime.datetime(day=1,month=int(numbers[0]),year=int(numbers[1]))

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
    "(%s\s*[I|II|III|IV]{1,}[\/.-]\s*\d{4})(?!%s)" % (tt_dict['2'], character),
    # ngày dd tháng mm năm yyyy 4
    "(ngày\s*\d{1,2}\s*tháng\s*\d{1,2}\s*năm\s*\d{4})(?!%s)" % (character),
    # Tháng mm năm yyyy 5
    "(tháng\s*\d{1,2}\s*năm\s*\d{4})(?!%s)" % (character),
    # Ngày dd tháng mm 6
    "(ngày\s*\d{1,2}\s*tháng\s*\d{1,2})(?!%s)" % (character),
    "(%s\s*\d{4})(?!%s)" % (tt_dict['3'], character),  # yyyy
]

regex_keyword = "(%s|%s|%s|%s)" % (
    tt_dict['0'], tt_dict['1'], tt_dict['2'], tt_dict['3'])

regex2convert = {
    0: convert_dd_mm_yyyy,
    4: convert_dd_mm_yyyy,
    1: convert_mm_yyyy,
    5: convert_mm_yyyy,
    2: convert_dd_mm,
    6: convert_dd_mm
}

def get_ner_datetime(text):
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
                entity['datetime'] = regex2convert[idx](entity['text'])
                break   
        entity['tag'] = 'DATETIME'
        entity['start_position'] = iter.start()
        entity['end_position'] = iter.end()
        obj['entities'].append(entity)
    try:
        return obj['entities'][0]['datetime']
    except IndexError:
        return "Không có thời gian"

    


if __name__ == "__main__":
    sentence = """
US Virgin Islands gửi trát đòi hầu tòa cho Elon Musk trong vụ kiện Jeffrey Epstein ở tháng 2 năm 2018
    """
    result = get_ner_datetime(sentence)
    print(result)