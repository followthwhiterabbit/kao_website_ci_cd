from django.urls import path 

from . import views

urlpatterns = [
    path("", views.leak_func, name="leak_testing"),
]
