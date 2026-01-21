def build_context(chunks):
    return {
        "files": [c["file"] for c in chunks],
        "symbols": sum([c["symbols"] for c in chunks], [])
    }
