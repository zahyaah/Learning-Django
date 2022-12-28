from django.shortcuts import render
from app1 import models
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexOne(TemplateView):
    template_name = 'app2/App2_HomePage.html'
    extra_context = {'dataCovered': models.Remark.objects.all()}


class IndexTwo(LoginRequiredMixin, TemplateView):  # the mixin should be added before the TemplateView
    template_name = 'app2/Authorisation.html'
    login_url = '/admin'


