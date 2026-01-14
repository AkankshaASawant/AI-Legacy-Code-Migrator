import ast


class PythonASTParser(ast.NodeVisitor):
    def __init__(self):
        self.methods = []
        self.calls = []

    def visit_FunctionDef(self, node):
        calls = []
        for n in ast.walk(node):
            if isinstance(n, ast.Call) and hasattr(n.func, "id"):
                calls.append(n.func.id)

        self.methods.append({
            "name": node.name,
            "calls": list(set(calls))
        })
        self.generic_visit(node)
