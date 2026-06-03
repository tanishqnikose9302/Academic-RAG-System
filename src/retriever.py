from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL
class Retriever:
    def __init__(self):
        self.model=SentenceTransformer(EMBEDDING_MODEL)
    def get_query_embedding(self,q):
        return self.model.encode(q)
