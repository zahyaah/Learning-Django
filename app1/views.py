from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Remark
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("<h1>Hello World</h1>")


# def index1(request):
#     return render(request, 'app1/first.html', {"date": date.today()})
class Index1(TemplateView):
    template_name = 'app1/first.html'
    extra_context = {"date": date.today()}


# def index2(request):
#     dataStored = Remark.objects.all()
#     return render(request, 'app1/AccessIt.html', {"passData": dataStored})
class Index2(TemplateView):
    dataStored = Remark.objects.all()
    template_name = 'app1/AccessIt.html'
    extra_context = {"passData": dataStored}


def index3(request, pk):
    dateStored = Remark.objects.get(pk=pk)
    return render(request, 'app1/priKey.html', {"ds": dateStored})


@login_required(redirect_field_name="http://127.0.0.1:8000/index4", login_url='http://127.0.0.1:8000/admin')
def index4(request):
    return render(request, 'app1/restriction.html', {})
