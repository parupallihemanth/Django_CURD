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

get_a_resource('2')
