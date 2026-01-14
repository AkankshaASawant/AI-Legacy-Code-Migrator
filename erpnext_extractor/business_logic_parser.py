from analyzer.ast_parser import PythonASTParser
import ast


def extract_business_logic(py_file):
    with open(py_file, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    parser = PythonASTParser()
    parser.visit(tree)

    rules = []
    for m in parser.methods:
        if "check" in m["name"] or "validate" in m["name"]:
            rules.append(f"Rule enforced in {m['name']}")

    return parser.methods, rules
