import json

def save(data, path):
    updated_data = []
    with open(path, 'w') as f:
        ID = 0
        for _dict in data:
            _dict.update({'id': ID})
            ID += 1
            updated_data.append(_dict)
        json.dump(updated_data, f, indent=4)
