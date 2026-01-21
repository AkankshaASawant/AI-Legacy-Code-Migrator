from fastapi import APIRouter
from pydantic import BaseModel
from core.rag_engine import index_codebase

router = APIRouter(prefix="/index", tags=["Index"])

class IndexRequest(BaseModel):
    path: str

@router.post("/")
def index_endpoint(req: IndexRequest):
    result = index_codebase(req.path)
    return {"message": result}
