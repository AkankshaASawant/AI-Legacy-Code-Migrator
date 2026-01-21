from fastapi import APIRouter
from evaluation.ragas_runner import run_ragas
from experiments.mlflow_logger import log_run

router = APIRouter()

@router.post("/")
def evaluate(payload: dict):
    dataset = payload["dataset"]

    scores = run_ragas(dataset)
    log_run({"run": "qa_eval"}, scores)

    return scores
