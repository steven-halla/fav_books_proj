from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(post_data['first_name']) < 3:
            errors['first_name'] = "First name must be 3 characters"

        if post_data['first_name'].isalpha() == False:
            errors['first_name'] = "letters only"

        if len(post_data['last_name']) < 3:
            errors['last_name'] = "Last name must be 3 characters"

        if post_data['last_name'].isalpha() == False:
            errors['last_name'] = "letters only"

        if len(post_data['email']) < 8:
            errors['email'] = "Email must contain 8 characters"

        if post_data['email'].find("@") == -1:
            errors['email'] = "email must contain @ and .com"

        if post_data['email'].find(".com") == -1:
            errors['email'] = "email must contain @ and .com"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        return errors

        if post_data['password'] != post_data['confirm_password']:
            errors['pass_match'] = "password must match confirm password"

        if len(post_data['password']) < 8:
            errors['pass_length'] = "password must be longer than 8 characters"


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    books_uploaded = ""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
     title = models.CharField(max_length=20)
     desc = models.CharField(max_length=40)
    #uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
    #users_who_favorite = models.ManyToManyField(User, related_name="liked_books")
   # created_at = models.DateTimeField(auto_now_add=True)
   # updated_at = models.DateTimeField(auto_now=True)
    
