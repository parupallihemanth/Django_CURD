from django import forms
from app1.models import Restaurants

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurants

        fields = '__all__'