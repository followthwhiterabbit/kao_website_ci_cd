from django.urls import path 

from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", views.about_func, name="about_page"),
]



