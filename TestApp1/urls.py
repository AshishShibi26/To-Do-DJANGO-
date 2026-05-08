from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),

    path('adminlogin/', views.adminlogin),

]