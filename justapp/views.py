from datetime import datetime
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse

from justapp.forms import HomeForm
from justapp.models import portScanner

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def blank(request):

    ip = ""
    out = ""

    if request.POST:
        ip = request.POST["ip"]

        if ip != "":
            out = portScanner(ip)


    return render(request, 'blank.html', {
        'current_time': str(datetime.now()),'OutPortScanner':str(out)
    })

def blank1(request):
    return render(request, 'blank.1.html', {
        'current_time': str(datetime.now()),
    })

def blank2(request):
    return render(request, 'blank.2.html', {
        'current_time': str(datetime.now()),
    })
def blank3(request):
    return render(request, 'blank.3.html', {
        'current_time': str(datetime.now()),
    })

def index(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })

def views(request):
    return render(request, 'typography.html', {
        'current_time': str(datetime.now()),
    })