from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


def index(request):
    return HttpResponse("<h1>Hello World</h1>")


def index1(request):
    return render(request, 'app1/first.html', {"date": date.today()})
