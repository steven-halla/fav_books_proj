from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# contains user signup + login form
def view_index(request):
    return render(request, "index.html")

# user signup form will post to a url (/register) which maps to this function
def register_new_user(request):
    # returns a dictionary of errors.
    # e.g. errors['first_name'] = 'letters only'
    errors = User.objects.user_registration_validator(request.POST)

    # iterate over each error (key/value) pair in the errors dictionary
    # and take the error key and value and makes a full error message,
    # and then adds the error message via messages.error()
    if len(errors) > 0:
        for key, value in errors.items():
            error_msg = key + ' - ' + value
            messages.error(request, error_msg)
        
        return redirect("/")
    
    else:
        first_name_from_post = request.POST['first_name']
        last_name_from_post = request.POST['last_name']
        email_from_post = request.POST['email']
        password_from_post = request.POST['password']
        new_user = User.objects.create(
            first_name=first_name_from_post,
            last_name=last_name_from_post,
            email=email_from_post,
            password=password_from_post
        )
        print(new_user.id)
        request.session['user_id'] = new_user.id
        
        return redirect('/books')


def login(request):
    # user did provide email/password, now lets check database
    email_from_post = request.POST['email']
    password_from_post = request.POST['password']

    # this will return all users that have the email_from_post
    # in future we should require email to be unique
    users = User.objects.filter(email=email_from_post)
    if len(users) == 0:
        messages.error(request, "email/password does not exist")
        return redirect("/")

    user = users[0]
    print(user)

    # check that the user submitted password is the same as what we have stored in the database
    if (user.password != password_from_post):
        messages.error(request, "email/password does not exist")
        return redirect("/")
    
    request.session['user_id'] = user.id
    return redirect("/books")


def logout(request):
    request.session.clear()
    return redirect("/")


#this will put user to books_user_page
def view_books(request):
    if 'user_id' not in request.session:
        redirect
    user = User.objects.get(id=request.session['user_id'])
    all_books_from_db = Books.objects.all()
    context = {
        "user": user,
        "all_books": all_books_from_db
    }
    return render(request, "books_user_page.html", context)

# this will put the user on a web page to display the books info and allow them to unfavorite a book


def view_book(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    all_books_from_db = Books.objects.all()
    context = {
        "user": user,
        "all_books": all_books_from_db
    }
    return render(request, "book_fav_info.html", context)

#adds new book to database that you like


def add_book(request):
    errors = Books.objects.basic_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("register/success")

    else:
        title_from_post = request.POST['title']
        description_from_post = request.POST['desc']
        book = Books.objects.create(
            title=title_from_post,
            desc=description_from_post,
            uploaded_by_id=request.session['user_id']
        )
        print(book.id)
        request.session['book_id'] = book.id

        return redirect("/register/success")
