from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self, documents):
        self.docs = documents
        corpus = [d["content"].split() for d in documents]
        self.bm25 = BM25Okapi(corpus)

    def search(self, query, k=5):
        scores = self.bm25.get_scores(query.split())
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return [self.docs[i] for i in ranked[:k]]
