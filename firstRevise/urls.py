from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register,name='index'),
    path('publishResult', views.publish,name='index'),
]
