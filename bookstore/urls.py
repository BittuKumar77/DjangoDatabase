from django.urls import path
from .import views

app_name = 'books'

urlpatterns = [
    path('booklist',views.home),
    path('book-details/<str:id>',views.detail,name='book-details')
]