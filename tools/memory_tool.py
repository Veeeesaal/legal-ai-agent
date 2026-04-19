from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Memory:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.data = []

    def add(self, text):
        embedding = self.model.encode([text])
        self.index.add(np.array(embedding))
        self.data.append(text)

    def search(self, query):
        if len(self.data) == 0:
            return "No memory found"

        query_embedding = self.model.encode([query])
        D, I = self.index.search(np.array(query_embedding), k=2)

        results = [self.data[i] for i in I[0]]
        return "\n".join(results)