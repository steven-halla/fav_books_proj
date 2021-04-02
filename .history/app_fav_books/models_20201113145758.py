from django.db import models

# Create your models here.
class User(models.Model)
    first_name = models.CharField(max_length=20)
    last_name = models.Charfield(max_length=20)
    email = 
    password = models.Char
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)