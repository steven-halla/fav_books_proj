from django.urls


def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
