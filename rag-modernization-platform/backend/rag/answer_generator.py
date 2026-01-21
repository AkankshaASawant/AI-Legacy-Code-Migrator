from rag.llm_client import call_llm

def generate_answer(question, context):
    prompt = f"""
Question: {question}

Relevant Files:
{context['files']}

Relevant Symbols:
{context['symbols']}
"""
    return call_llm(prompt)
