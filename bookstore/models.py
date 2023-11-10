from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify

from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.   


class Country(models.Model):
    cname = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural='Author_Address'

    def __str__(self):
        return f'{self.street} {self.city} {self.pincode}'
    
class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.OneToOneField('Address',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.address}'


class bookdata(models.Model):
    bname = models.CharField(max_length=50)             
    category = models.CharField(max_length=20)       
    # author = models.CharField(max_length=50)
    author = models.ForeignKey('Author',on_delete=models.CASCADE,null=True,related_name='book')
    price = models.IntegerField()
    best_seller = models.BooleanField(default=False)    
    ratings = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)],null=True)
    slug = models.SlugField(default="",null=False)
    published_country = models.ManyToManyField('country')

    def __str__(self):
        return f"{self.bname} {self.author} {self.price} {self.best_seller}"       

    def save(self,*args,**kwargs):
        self.slug = slugify(self.bname)
        super().save(*args,**kwargs)
                                 

