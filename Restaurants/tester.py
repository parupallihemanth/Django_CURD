import requests
import json
BASE_URL = 'http://localhost:8000/'
ENDPOINT = 'api/'


def get_all_resources():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

# get_all_resources()          

def get_a_resource(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())

# get_a_resource('2')

def create_a_resource():
    new_restaurant={
        'name':"Barrington",
        'year': 2002,
        'phone':868086423,
        'status': 'close',
        'address':'Barrington st'
    }

    resp=requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_restaurant))
    print(resp.status_code)
    print(resp.json())

create_a_resource()