from django.shortcuts import render
from django.views.generic import View
from app1.models import Restaurants


from app1.mixins import JsonMixin, ResponseMixin
import json

# Create your views here.

class Restaurants_CBV(ResponseMixin,JsonMixin,View):

    def get(self, request, *args, **kwargs):
        try:
            data=Restaurants.objects.all()
        except:
            json_data=json.dumps({"msg":"Sorry no data available"})  
            return self.http_response(json_data, status=400)  
        else:    
            final_data=self.my_JsonMixin(data)
            return self.http_response(final_data, status=200)
        

class Restaurants_Id_CBV(ResponseMixin,JsonMixin,View):

    def get(self, request, id, *args, **kwargs):
        try:
            data=Restaurants.objects.get(id=id)
        except:
            json_data=json.dumps({"msg":"Sorry no data available"}) 
            return self.http_response(json_data, status=400)   
        else:
            final_data=self.my_JsonMixin([data])
            return self.http_response(final_data, status=200)    

