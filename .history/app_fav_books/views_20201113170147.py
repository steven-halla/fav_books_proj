from django.urls import 


def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
