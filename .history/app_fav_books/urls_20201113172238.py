from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #this will redirect the user to the function to get them to the books page after registering 
    path('register', views.register_New_User)

]
