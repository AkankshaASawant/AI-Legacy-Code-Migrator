from fastapi import FastAPI
from api.routes.index import router as index_router
from api.routes.query import router as query_router

app = FastAPI(title="RAG Modernization Platform")

app.include_router(index_router)
app.include_router(query_router)

@app.get("/")
def root():
    return {"status": "API running"}
