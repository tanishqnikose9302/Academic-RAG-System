import faiss,pickle,numpy as np,os
class VectorStore:
    def create_index(self,embeddings,chunks):
        self.index=faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings,dtype=np.float32))
        self.chunks=chunks
    def save(self,folder):
        os.makedirs(folder,exist_ok=True)
        faiss.write_index(self.index,f'{folder}/index.faiss')
        with open(f'{folder}/chunks.pkl','wb') as f:
            pickle.dump(self.chunks,f)
    def load(self,folder):
        self.index=faiss.read_index(f'{folder}/index.faiss')
        with open(f'{folder}/chunks.pkl','rb') as f:
            self.chunks=pickle.load(f)
    def search(self,query_embedding,k=3):
        _,idx=self.index.search(np.array([query_embedding],dtype=np.float32),k)
        return [self.chunks[i] for i in idx[0] if i < len(self.chunks)]
