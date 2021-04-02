from django.urls import path
from . import views

urlpatterns = [
    # the page that contains login/sign form
    path('', views.index),
    # this is the path that our user registration form posts to.
    path('register', views.register_new_user),
    # the page to show after a user has been created/registered.
    path('register/success', views.books_info),
    path('logout', views.log_user_out),
    path('login', views.log_in),
    path('register/books/add', views.add_new_book),
    path('books/<int:book_id>', views.book_info)

]
