from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index1/', views.Index1.as_view(), name="firstOne"),
    path('index2/', views.Index2.as_view(), name="secondOne"),
    path('index3/<int:pk>', views.Index3.as_view(), name="thirdOne"),
    path('index4/', views.Index4.as_view(), name="fourthOne"),
    path('index5/new/', views.RemarkCreateView.as_view(), name='RCV'),
]