from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index1/', views.Index1.as_view()),
    path('index2/', views.Index2.as_view()),
    path('index3/<int:pk>', views.index3),
    path('index4/', views.index4)
]