from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello, this is my first page</h1>')
