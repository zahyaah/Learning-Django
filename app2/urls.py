from django.urls import path
from . import views


urlpatterns = [
    path('indexone/', views.IndexOne.as_view(), name='TakeOne'),
    path('indextwo/', views.IndexTwo.as_view(), name='TakeTwo'),
]