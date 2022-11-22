from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index1/', views.index1),
    path('index2/', views.index2),
]