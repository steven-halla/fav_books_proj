from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    #this will launch us to function to render success html page
    path('register/success', views.success_page),
    path('login', views.login),
    path('logout', views.logout)
]
