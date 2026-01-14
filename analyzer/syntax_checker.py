def check_syntax(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            compile(f.read(), file_path, "exec")
        return None
    except SyntaxError as e:
        return str(e)
