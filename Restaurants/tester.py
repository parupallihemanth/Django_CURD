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
        'name':"Atlantic Hotel",
        'year': 2008,
        'phone':878586423,
        'status': 'close',
        'address':'Robie st'
    }

    resp=requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_restaurant))
    print(resp.status_code)
    print(resp.json())

# create_a_resource()

def update_a_resource(id):
    update_restaurant={
        'status':'close'
    }
    resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/', data=json.dumps(update_restaurant))
    print(resp.status_code)
    print(resp.json())

# update_a_resource(1)    


def delete_a_resource(id):
    res = requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
    print(res.status_code)
    print(res.json())


delete_a_resource(6)
