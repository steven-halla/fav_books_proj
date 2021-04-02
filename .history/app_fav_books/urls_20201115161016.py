from django.urls import path
from . import views

urlpatterns = [
    # the page that contains login/sign form/
    path('', views.view_index),
    # this is the path that our user registration form POSTs(submits) to.
    # if registration fails, show errors on registration page
    # if registration successful, redirect to /books
    path('register', views.register_new_user),
    # the /login path maps to the login function which logs in the user.
    # if login fails, show error message on index page.
    # if login successful, redirect to /books
    path('login', views.login),
    # the /logout path maps to thg log_user_out function which logs out the user and 
    # redirects to index.
    path('logout', views.logout),

    # this page displays all books + add book form.
    path('books', views.view_books),
    # this page displays a single book
    path('books/<int:book_id>', views.view_book),
    # this is the path that our create book form POSTs(submit) to.
    # if add book successful, show all the books again.
    # if create book fails, show errors on show error on /books page.
    path('books/add', views.add_book),
    # this is the path to add a book to your favorites list.
    # if add is successful, redirect to /books/id
    # if error, redirect to books/id and show error
    path('books/<int:book_id>/favorite', views.favorite_book),
    path('books/')

]
