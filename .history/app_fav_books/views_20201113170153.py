from django.urls import path
from . import views 


def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
