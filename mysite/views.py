from django.http import Http404
from django.shortcuts import render

import datetime

def hello(request):
    return render(request, "Hello world")

def my_homepage_view(request):
    return render(request, "This is my Home Page!")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'offset': offset, 'next_time': dt})