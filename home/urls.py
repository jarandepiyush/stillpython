from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('index.html',views.index,name='home'),
    path('about.html',views.about,name='about'),
    path('product.html',views.product,name='product'),

    path('pro1.html',views.pro1,name='product 1'),
    path('pro2.html',views.pro2,name='product 2'),
    path('pro3.html',views.pro3,name='product 3'),
    path('pro4.html',views.pro4,name='product 4'),
    path('pro5.html',views.pro5,name='product 5'),
    path('pro6.html',views.pro6,name='product 6'),



    path('contact.html',views.contact,name='Contact')
]