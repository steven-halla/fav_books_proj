from django.db import models
import re

# Create your models here.
class User(models.Model)
    first_name = models.CharField(max_length=20)
    last_name = models.Charfield(max_length=20)
    email = 
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)