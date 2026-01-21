import numpy as np

class VectorStore:
    def __init__(self):
        self.embeddings = None
        self.documents = []

    def _embed(self, texts):
        """
        Dummy deterministic embedding.
        Replace later with SentenceTransformers / OpenAI / etc.
        """
        if not texts:
            return np.array([])

        # 384-dim fake embedding
        return np.array([
            np.ones(384, dtype=np.float32) * (i + 1)
            for i in range(len(texts))
        ])

    def build(self, documents):
        if not documents:
            raise ValueError("No documents to index")

        texts = [doc["content"] for doc in documents]
        embeddings = self._embed(texts)

        if embeddings.ndim != 2:
            raise ValueError("Embedding generation failed")

        self.embeddings = embeddings
        self.documents = documents

    def search(self, query, top_k=5):
        if self.embeddings is None:
            raise RuntimeError("Index not built")

        # Dummy similarity: return first k docs
        return self.documents[:top_k]


# GLOBAL singleton store
store = VectorStore()
