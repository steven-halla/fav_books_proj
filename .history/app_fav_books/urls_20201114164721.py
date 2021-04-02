from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #this will redirect the user to the function to get them to the books page after registering 
    path('register', views.register_New_User),
    path('register/success', views.books_info),
    path('logout', views.log_user_out),
    path('login'.views.books_info)

]
