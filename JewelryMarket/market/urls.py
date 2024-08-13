from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, mame='home')



]