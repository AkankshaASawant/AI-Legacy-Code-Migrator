from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy

def run_ragas(dataset):
    results = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy]
    )
    return results
