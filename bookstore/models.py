from django.db import models
from django.db.models.base import Model


# Create your models here.            

class bookdata(models.Model):
    bname = models.CharField(max_length=50)             
    category = models.CharField(max_length=20)       
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    best_seller = models.BooleanField(default=False)                                    
