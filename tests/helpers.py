import os.path as path
import json

def load_json(file_path):
    report_path = path.abspath(file_path)

    with open(report_path, 'r') as f:
        content = f.read()
    return json.loads(content)
