import os


def find_files(root, extensions):
    results = []
    for path, _, files in os.walk(root):
        for f in files:
            if f.endswith(extensions):
                results.append(os.path.join(path, f))
    return results
