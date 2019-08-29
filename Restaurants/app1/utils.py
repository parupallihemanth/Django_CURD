import json

def is_json(data):
    try:
        dict_data=json.loads(data)
        valid = True
    except ValueError:
        valid = False    

    return valid    