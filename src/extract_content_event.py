from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize

class Extract_content:
    '''Khởi tạo mô hình PhoBERT'''
    def __init__(self):
        self.model = SentenceTransformer('VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')
    
    '''Tiến hành embedding'''
    def get_embeddings(self, sentences):
        #st = time.time()
        #print("-------Getting embedding for document-------")
        #tokenized các câu
        sentences_tokenizer = [tokenize(sentence) for sentence in sentences]

        #tiến hành embedding (device sẽ được tự động setup)
        embeddings = self.model.encode(sentences_tokenizer)
        # print("Embedding time: ", time.time() - st)
        # print("Embedding shape :",embeddings.shape)
        return embeddings

    '''Tìm kiếm nội dung của sự kiện'''
    def extract_content(self,title, candidate):
        #danh sách các sự kiện trích rút được
        content = []

        #tiêu đề cần tìm kiếm nội dung
        title_embedd = self.get_embeddings([title])

        #thuật toán tìm kiếm nội dung
        #nếu độ tương đồng của các câu ứng viên lớn hơn 0.5 => sẽ thêm vào content
        for i in candidate:
            if round(cosine_similarity(title_embedd, self.get_embeddings([i]))[0][0], 2) >= 0.5:
                content.append(i)
        return content