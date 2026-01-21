from fastapi import APIRouter
from pydantic import BaseModel
from core.rag_engine import query_rag

router = APIRouter(prefix="/query", tags=["Query"])

class QueryRequest(BaseModel):
    question: str

@router.post("/")
def query_endpoint(req: QueryRequest):
    answer = query_rag(req.question)
    return {"answer": answer}
