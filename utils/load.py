import json

def load(path):
    with open(path, "r") as f:
        data = json.load(f)

    return data
