import os
import ast

def parse_codebase(path):
    documents = []

    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".py"):
                full = os.path.join(root, f)
                with open(full, "r", encoding="utf-8") as fh:
                    src = fh.read()
                tree = ast.parse(src)
                documents.append({
                    "file": full,
                    "content": src,
                    "symbols": [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
                })
    return documents
