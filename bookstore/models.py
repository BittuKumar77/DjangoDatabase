from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify

from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.            

class bookdata(models.Model):
    bname = models.CharField(max_length=50)             
    category = models.CharField(max_length=20)       
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    best_seller = models.BooleanField(default=False)    
    ratings = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)],null=True)
    slug = models.SlugField(default="",null=False)

    def __str__(self):
        return f"{self.bname} {self.author} {self.price} {self.best_seller}"       

    def save(self,*args,**kwargs):
        self.slug = slugify(self.bname)
        super().save(*args,**kwargs)
                                 

