from backend.retriever.vector_store import store

def hybrid_search(query: str):
    return store.search(query)
