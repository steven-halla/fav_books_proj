from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #this will redirect the user to the function to get them to the books page after registering 
    path('register', views.register_New_User),
    path('register/success', views.books_info),
    path('logout', views.log_user_out),
    path('login', views.log_in),
    path('register/books/add', views.add_new_book),
    path('regester/')

]
