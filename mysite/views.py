from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def my_homepage_view(request):
    return HttpResponse("This is my Home Page!")