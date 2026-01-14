import json
from analyzer.file_scanner import find_files
from analyzer.syntax_checker import check_syntax
from erpnext_extractor.doctype_schema_parser import parse_doctype_schema
from erpnext_extractor.business_logic_parser import extract_business_logic
from analyzer.relationship_extractor import extract_links_from_json
from models.entity_model import Entity



ERP_PATH = "erpnext/erpnext/accounts/doctype/sales_invoice"


def main():
    entity = Entity(name="SalesInvoice")

    json_file = f"{ERP_PATH}/sales_invoice.json"
    py_file = f"{ERP_PATH}/sales_invoice.py"

    entity.fields = parse_doctype_schema(json_file)

    methods, rules = extract_business_logic(py_file)
    entity.methods = methods
    entity.business_rules = rules

    with open(json_file) as f:
        schema = json.load(f)
    entity.relationships = extract_links_from_json(schema)

    with open("output/sales_invoice.json", "w") as f:
        json.dump(entity.__dict__, f, indent=2)

    generate_diagram(entity)


def generate_diagram(entity):
    diagram = []
    diagram.append(f"class {entity.name}")

    for field, target in entity.relationships.items():
        diagram.append(f"{entity.name} --> {target}")

    with open("output/class_diagram.txt", "w") as f:
        f.write("\n".join(diagram))


if __name__ == "__main__":
    main()
