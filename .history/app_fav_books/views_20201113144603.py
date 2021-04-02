
# Create your views here.
from django.shortcuts import render, HttpResponse


def index(request):
    returncopy HttpResponse("this is the equivalent of @app.route('/')!")
