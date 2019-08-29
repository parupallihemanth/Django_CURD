from django.shortcuts import render
from django.views.generic import View
from app1.models import Restaurants


from app1.mixins import JsonMixin, ResponseMixin
import json

# Create your views here.


#This class based view is responsible for  http methods which doesn't require id
class Restaurants_CBV(ResponseMixin,JsonMixin,View):

    #Get all objects from database
    def get(self, request, *args, **kwargs):
        try:
            data=Restaurants.objects.all()
        except:
            json_data=json.dumps({"msg":"Sorry no data available"})  
            return self.http_response(json_data, status=400)  
        else:    
            final_data=self.my_JsonMixin(data)
            return self.http_response(final_data, status=200)
    
    def post(self, request, *args, **kwargs):
        


        
#This class based view is responsible for  http methods which require id
class Restaurants_Id_CBV(ResponseMixin,JsonMixin,View):

    #Get particular resource from databse
    def get(self, request, id, *args, **kwargs):
        try:
            data=Restaurants.objects.get(id=id)
        except Restaurants.DoesNotExist:
            json_data=json.dumps({"msg":"Sorry requested data not available"}) 
            return self.http_response(json_data, status=404)   
        else:
            json_data=self.my_JsonMixin([data, ])
            return self.http_response(json_data)    





