from django.http import Http404
from django.shortcuts import render
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                # cd.get('email', ['noreply@example.com](mailto:'noreply%40example.com)'),
                # [['siteowner@example.com](mailto:'siteowner%40example.com)'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})