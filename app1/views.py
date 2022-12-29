from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Remark
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,
                                  DetailView,
                                  ListView,
                                  CreateView,
                                  UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RemarkForm


class RemarkUpdateView(UpdateView):
    model = Remark
    # fields = ["name", "text"]
    form_class = RemarkForm
    success_url = "/app1/index2/"


class RemarkCreateView(CreateView):
    model = Remark
    # fields = ["name", "text"]
    form_class = RemarkForm
    success_url = "/app1/index2/"


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

# class Index2(TemplateView):
#     dataStored = Remark.objects.all()
#     template_name = 'app1/AccessIt.html'
#     extra_context = {"passData": dataStored}


class Index2(ListView):
    model = Remark
    context_object_name = "passData"
    template_name = 'app1/AccessIt.html'


# def index3(request, pk):
#     try:
#         dateStored = Remark.objects.get(pk=pk)
#     except Remark.DoesNotExist:
#         raise Http404("Doesn't Exist, Seriously")
#     return render(request, 'app1/priKey.html', {"ds": dateStored})


class Index3(DetailView):
    model = Remark
    context_object_name = 'ds'
    template_name = 'app1/priKey.html'


# @login_required(redirect_field_name="http://127.0.0.1:8000/index4", login_url='http://127.0.0.1:8000/admin')
# def index4(request):
#     return render(request, 'app1/restriction.html', {})


class Index4(LoginRequiredMixin, TemplateView):
    template_name = 'app1/restriction.html'
    login_url = 'http://127.0.0.1:8000/admin/'

