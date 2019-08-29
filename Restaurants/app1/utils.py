import json

def is_json(data):
    try:
        data=json.loads(data)
        valid = True
    except:
        valid = False    