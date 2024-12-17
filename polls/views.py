from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. this is my first poll, and sasha e un pidar")