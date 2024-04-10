import json


def ImportLevel(name):
    with open(name + '.json') as f:
        data = json.load(f)
    return data
