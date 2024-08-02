from django.urls import path 

from . import views

urlpatterns = [
    path("", views.dimensional_func, name="dimensional_measurement"),
]




