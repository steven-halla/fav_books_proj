from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# contains user signup + login form
def view_index(request):
    # bonus, if user is already logged in, lets not show them login/registration page,
    # and instead redirect them to /books, which is already where we redirect users
    # after they login/register.
    if 'user_id' in request.session:
        return redirect("/books")

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
    
    # we store the logged in user's id in the session variable, 
    # so that we can quickly get the current logged in user's id any time we need it in back end functions. 
    # e.g. view_books when we look up the user by: User.objects.get(id=request.session['user_id'])
    # session variables are shared accors all of my requests
    # LEARN
    request.session['user_id'] = user.id

    return redirect("/books")


def logout(request):
    request.session.clear()
    return redirect("/")


# this will render view_books.html page.
# this page will show a list of all the books and the current logged in user.
def view_books(request):
    if 'user_id' not in request.session:
        return redirect("/")

    user = User.objects.get(id=request.session['user_id'])
    all_books_from_db = Books.objects.all()
    context = {
        "user": user,
        "all_books": all_books_from_db
    }
    return render(request, "view_books.html", context)

# this will render view_book.html page.
# this page will show a single book and the current logged in user.
def view_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect("/")

    user = User.objects.get(id=request.session['user_id'])
    book_from_db = Books.objects.get(id=book_id)
    context = {
        "user": user,
        "book": book_from_db
    }

    print(book_from_db.id)

    return render(request, "view_book.html", context)


# adds new book to database that you like
def add_book(request):
    if 'user_id' not in request.session:
        return redirect("/")

    errors = Books.objects.add_book_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            error_msg = key + ' - ' + value
            messages.error(request, error_msg)
        return redirect("/books")

    # current logged in user
    current_user = User.objects.get(id=request.session['user_id'])


    title_from_post = request.POST['title']
    description_from_post = request.POST['desc']
    book = Books.objects.create(
        title=title_from_post,
        desc=description_from_post,
        uploaded_by_id=current_user.id,
    )
    print(book)

    book.users_who_favorite.add(current_user)

    return redirect("/books")


# favorite a book that you did not upload
def favorite_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect("/")

    book_from_db = Books.objects.get(id=book_id)
    user_from_db = User.objects.get(id=request.session['user_id'])

    # TODO if user has already added book as favorite, just return, don't re-add

    book_from_db.users_who_favorite.add(user_from_db)

    book_from_db.save()

    return redirect("/books/" + str(book_id))

def edit_book(request):
    errors = Books.objects.add_book_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/books/" + str(book_id) + "/edit")
    
    book_to_update = Books.objects.get
