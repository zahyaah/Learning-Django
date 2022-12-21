from django.shortcuts import render
from app1 import models
from django.views.generic import TemplateView


class IndexOne(TemplateView):
    template_name = 'app2/App2_HomePage.html'
    extra_context = {'dataCovered': models.Remark.objects.all()}