from config import CHUNK_SIZE,CHUNK_OVERLAP
class TextChunker:
    @staticmethod
    def chunk_text(text):
        chunks=[]
        start=0
        while start < len(text):
            chunks.append(text[start:start+CHUNK_SIZE])
            start += CHUNK_SIZE-CHUNK_OVERLAP
        return chunks
