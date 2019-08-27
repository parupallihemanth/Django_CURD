from django.db import models

# Create your models here.

class Restaurants(models.Model):
    name = models.CharField(max_length=40)
    year = models.IntegerField()
    phone = models.IntegerField()
    status = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
