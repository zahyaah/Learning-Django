from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Remark


def index(request):
    return HttpResponse("<h1>Hello World</h1>")


def index1(request):
    return render(request, 'app1/first.html', {"date": date.today()})


def index2(request):
    dataStored = Remark.objects.all()
    return render(request, 'app1/AccessIt.html', {"passData": dataStored})


def index3(request, pk):
    dateStored = Remark.objects.get(pk=pk)
    return render(request, 'app1/priKey.html', {"ds": dateStored})