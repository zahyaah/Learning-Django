from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class Show(TemplateView):
    template_name = 'displayAll/AllTheFiles.html'

