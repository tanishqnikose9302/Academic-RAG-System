from src.pdf_loader import PDFLoader
from src.chunker import TextChunker
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.retriever import Retriever
from src.llm_local import LocalLLM

class RAGPipeline:
    def __init__(self):
        self.embedder=EmbeddingModel()
        self.store=VectorStore()
        self.retriever=Retriever()

    def ingest_document(self,pdf_path):
        text=PDFLoader.load_pdf(pdf_path)
        chunks=TextChunker.chunk_text(text)
        embeddings=self.embedder.generate_embeddings(chunks)
        self.store.create_index(embeddings,chunks)
        self.store.save('vectorstore')

    def answer_query(self,query):
        self.store.load('vectorstore')
        q=self.retriever.get_query_embedding(query)
        return self.store.search(q)
