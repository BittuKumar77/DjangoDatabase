from django.shortcuts import render
from .models import bookdata
from django.http import HttpResponseNotFound

# Create your views here.

def home(request):
    b=bookdata.objects.all()
    return render(request,'bookstore/home.html',{'books':b})

def detail(request,id):
    try:
        d=bookdata.objects.get(pk=id)  #slug
        return render(request,"bookstore/details.html",{
            'title':d.bname,
            'category':d.category,
            'author':d.author,
            'price':d.price,
            'best_seller':d.best_seller,
            'ratings':d.ratings

        })
    
    except:
        return HttpResponseNotFound("Invalid Book Request")
