from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #this will redirect the user to the 
    path('register', views.register_new_user)

]
