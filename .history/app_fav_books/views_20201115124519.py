from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request, "index.html")

def register_New_User(request):
    errors = User.objects.basic_validator(request.POST)


    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
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
        
        return redirect('/register/success')

    
#this will put user
def books_info(request):
    user = User.objects.get(id=request.session['user_id'])
    all_books_from_db = Books.objects.all()
    context = {
        "user": user,
        "all_books":all_books_from_db
    }
    return render(request, "books_user_page.html", context)

def log_user_out(request):
    request.session.clear()
    return redirect("/")

def log_in(request):
    email_from_post = request.POST['email']
    password_from_post = request.POST['password']

    user = User.objects.filter(email=email_from_post)
    if len(user) > 0:
        logged_user = user[0]
        print(logged_user.first_name)
        print(logged_user.password)
        request.session['user_id'] = logged_user.id
        return redirect("/register/success")
    else:
        messages.error(request, "email/password does not exist")
        return redirect("register/success")

#adds new book to database that you like
def add_new_book(request):
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
# this will put the user on a web page to display the books info and allow them to unfavorite a book
def book_info(request, book_id):
    this_book = Books.objects.get(id=book_id)
    context = {
        "book":this_book
    }
    return render(request, "book_fav_info.html", context)
