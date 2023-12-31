from django.contrib import admin
from django.urls import path, include
from home import views 

urlpatterns = [
    
    path("", views.home, name='home'),
    path("home", views.home, name ='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("ourreasontostart", views.ourreasontostart, name = 'ourreasontostart'),
    path("trackorders", views.trackorders, name = 'trackorders'),
    path("orders", views.orders, name = 'orders'),  
]
