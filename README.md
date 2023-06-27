# AIACADEMY VN
## Trích xuất sự kiện

Đây là hệ thống trích xuất các sự kiện từ một bài báo theo các tiêu chí

- Tiêu đề
- Chủ thể
- Khách thể
- Thời gian
- Địa điểm
- Nội dung

## Tính năng

- Áp dụng cho bất kỳ bài báo nào
- Không cần huấn luyện trước

## Công nghệ

Hệ thống sử dụng các công nghệ sau :

- [VncoreNLP] - Dùng để thực hiện việc posTag và NER
- [BERT] - để vectơ hóa, sau đó tính độ tương đồng cosine giữa các văn bản
- [python] - Ngôn ngữ lập trinh python

## Cài đặt
> Lưu ý : thay đổi đường dẫn folder vncore trong file extraction_title_event.py thành đường dẫn tuyệt đối trên máy

Cần cài đặt trước JAVA
* Java 1.8+ (JRE or JDK) || Hàm theo hướng dẫn sau `https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-do-I-install-Java-on-Ubuntu`

`Notice: Setting your JAVA_HOME! export JAVA_HOME='/usr/lib/jvm/{your_java_version}'`

Bước 1 : Clone source code

```sh
git clone https://gitlab.aiacademy.edu.vn/research-develop/nlp/vosint_v3_event_extraction.git
```

Bước 2 : Cài đặt các thư viện cần thiết

```sh
cd ../folder_code
pip install -r requirements.txt
```

Bước 3 : Chạy
```sh
python main.py
```

