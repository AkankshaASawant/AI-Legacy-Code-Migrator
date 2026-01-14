import re


def extract_links_from_json(schema):
    links = {}
    for field in schema.get("fields", []):
        if field.get("fieldtype") in ["Link", "Table"]:
            links[field["fieldname"]] = field.get("options")
    return links
