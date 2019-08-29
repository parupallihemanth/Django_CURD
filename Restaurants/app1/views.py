from django.shortcuts import render
from django.views.generic import View
from app1.models import Restaurants
from app1.utils import is_json
from app1.forms import RestaurantForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app1.mixins import JsonMixin, ResponseMixin
import json

# Create your views here.


#This class based view is responsible for  http methods which doesn't require id
@method_decorator(csrf_exempt, name= 'dispatch')
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

        data = request.body
        valid_json = is_json(data)

        if not valid_json:
            json_data=json.dumps({"msg":"Plese send only valid JSON"})
            return self.http_response(json_data, status=404)
        restaurant_data = json.loads(data)
        form = RestaurantForm(restaurant_data) 

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg":"Restaurant created successfully"})
            return self.http_response(json_data, status=200) 

        if form.error():
            json_data=json.dumps(form.error)
            return self.http_response(json_data, status=404)  
         



        
#This class based view is responsible for  http methods which require id
@method_decorator(csrf_exempt, name= 'dispatch')
class Restaurants_Id_CBV(ResponseMixin,JsonMixin,View):
    def get_obj_by_id(self, id):
            try:
                restaurant = Restaurants.objects.get(id=id)
            except:
                restaurant = None
            return restaurant 

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


    #To update a resource
    def put(self, request, id, *args, **kwargs):
        restaurant = self.get_obj_by_id(id)
        data = request.body
        valid_json = is_json(data)

        if not valid_json:
            json_data = json.dumps({"msg":"Please send valid json data"})
            return self.http_response(json_data, status=404)
        update_data = json.loads(data)
        original_data={
            'name' : restaurant.name,
            'year' : restaurant.year,
            'phone' : restaurant.phone,
            'status' : restaurant.status,
            'address' : restaurant.address
        }
        original_data.update(update_data)
        form = RestaurantForm(original_data, instance=restaurant)

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg":"Details updated successfully"})
            return self.http_response(json_data, status=200)
        if form.error():
            json_data = json.dumps({form.error})
            return self.http_response(json_data, status=404)    


