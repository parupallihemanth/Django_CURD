from django.core.serializers import serialize
from django.http import HttpResponse
import json
class JsonMixin(object):
    def my_JsonMixin(self, data):
            json_data=serialize('json', data)
            dict_data=json.loads(json_data)
            final_data=[]
            for obj in dict_data:
                data=obj['fields']
                final_data.append(data)
            final_json=json.dumps(final_data) 
            return final_json   

class ResponseMixin(object):
    def http_response(self,json_data, status=200):
        return HttpResponse(json_data, status=status)    
