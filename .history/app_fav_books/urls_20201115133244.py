from django.urls import path
from . import views

urlpatterns = [
    # the page that contains login/sign form/
    path('', views.index),
    # this is the path that our user registration form POSTs(submits) to.
    # if registration fails, show errors on registration page
    # if registration successful, redirect to /books
    path('register', views.register_new_user),

    # this page displays all books + add book form.
    path('books', views.books_info),
    # this page displays a single book
    path('books/<int:book_id>', views.book_info),
    # this is the path that our create book form POSTs(submit) to.
    # if create book fails, show errors on s
    path('books/add', views.add_new_book),

    path('login', views.log_in),
    path('logout', views.log_user_out),

]
