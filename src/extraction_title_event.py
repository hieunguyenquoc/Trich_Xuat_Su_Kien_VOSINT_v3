# -*- coding: utf-8 -*-
import py_vncorenlp
from src.extraction_time import get_ner_datetime

class Extract_title:
    '''Khởi tạo mô hình cho vncorenlp và list các từ chỉ địa điểm'''
    def __init__(self) :
        self.model = py_vncorenlp.VnCoreNLP(annotators=["wseg","pos","ner"],save_dir="D:/Aiacademy/VOSINT_event_extraction/thu_nghiem/vncore")
        self.lst_word_trigger = ['đến','thăm','tại','ở']

    # def find_title(self,content_lst):
    #     # content_lst = sent_tokenize(content.strip())

    #     #list các tiêu đề được trích rút
    #     title_lst = [content_lst[0]]

    #     #các thông tin về posTag, NER của bài báo
    #     output_content_lst = []

    #     for i in content_lst:
    #         output_content = self.model.annotate_text(i)
    #         output_content_lst.append(list(output_content.values()))
        
    #     #chứa thông tin về posTAG và NER của từng câu trong bài báo
    #     new_output_content_lst = [sublst[0] for sublst in output_content_lst]

    #     #thuật toán tìm kiếm câu tiêu đề
    #     #nếu một câu chứa động từ và xung quanh động từ đó các từ có nhãn posTagging là Nv,Nv,Np thì câu đó là một sự kiện
    #     i = 0
    #     # print(len(new_output_content_lst[5:]))
    #     # print(len(content_lst[5:]))
    #     while i < len(new_output_content_lst[5:]):
    #         j = 0
    #         while j < len(new_output_content_lst[i]):
    #             if new_output_content_lst[i][j]['posTag'].startswith("V"):
    #                 if any(x['posTag'] == 'Nc' or x['posTag'] == 'Np' or x['posTag'] == 'Ny' for x in new_output_content_lst[i][:j]) and any(y['posTag'] == 'Nc' or y['posTag'] == 'Np' or y['posTag'] == 'Ny' for y in new_output_content_lst[i][j+1:]):
    #                     try :
    #                         title_lst.append(content_lst[5:][i])
    #                         i += 10  # Bỏ qua 10 phần tử cạnh đó
    #                     except IndexError:
    #                         break
    #                     if i >= len(new_output_content_lst):
    #                         break  # Dừng vòng lặp nếu i vượt quá chỉ mục
    #                     continue
    #             j += 1
    #         i += 1
                    
    #     return title_lst[:3]

    '''Tìm chủ thế, khách thể của sự kiện'''
    def find_oject(self,title):
        #Chủ thế
        chu_the = []

        #Khách thể
        khach_the = []

        #Các thông tin về posTag và NER của tiêu đề
        output_title = self.model.annotate_text(title)

        #thuật toán tìm chủ thể và khách thể 
        #Nếu một câu có động từ, lấy ở hai bên của động từ ấy những từ có posTag là Nc, Nv, Np
        for sentence in output_title.values():
            for i, word in enumerate(sentence):
                if word['posTag'].startswith('V'):
                    chu_the = [w['wordForm'].replace("_", " ") for w in sentence[:i] if w['posTag'] in ['Nc', 'Np', 'Ny']]
                    khach_the = [w['wordForm'].replace("_", " ") for w in sentence[i+1:] if w['posTag'] in ['Nc', 'Np', 'Ny']]
                    break
        chu_the_final = [i.replace("_"," ") for i in chu_the]
        khach_the_final = [i.replace("_"," ") for i in khach_the]
        
        return ', '.join(chu_the_final), ', '.join(khach_the_final)
    
    '''Tìm kiến địa điểm trong sự kiện'''
    def find_location(self, title, content):
        #danh sách các sự kiện tìm được
        location = []

        #thông tin về posTag và NER của tiêu đề và nội dung của sự kiện
        output = self.model.annotate_text(title + ' ' + content)
        result = []
        for i in output.values():
            result.extend(i)

        #thuật toán tìm kiếm địa điểm
        #Nếu các từ chỉ địa điểm xuất hiện trong câu, tìm các từ ở bên phải từ đó có nhãn NER là B-LOC và I-LOC
        for item in range(len(result)):
            if result[item]['wordForm'] in self.lst_word_trigger:
                for k in result[item+1:item+4]:
                    if(k['nerLabel'] == 'B-LOC' or k['nerLabel'] == 'I-LOC'):
                            location.append(k['wordForm'])
        location = [x.replace("_"," ") for x in location]
        location = list(dict.fromkeys(location))
        if location == []:
            return "Không phát hiện địa điểm"
        else:
            return ' '.join(location)
    
    '''Tìm kiếm thời gian'''
    @staticmethod
    def find_time(title,public_date, content):
        #dựa trên rule-based
        thoi_gian = get_ner_datetime(title + ' ' + content, public_date)
        print(thoi_gian)
        return thoi_gian

# print(find_oject("Chủ tịch nước Võ Văn Thưởng đến Vientiane, bắt đầu thăm Lào."))
