import json


def parse_doctype_schema(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    fields = []
    for f in data.get("fields", []):
        fields.append({
            "name": f["fieldname"],
            "type": f["fieldtype"],
            "target": f.get("options")
        })

    return fields
