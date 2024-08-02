from django.urls import path 

from . import views

urlpatterns = [
    path("", views.callibrators_func, name="callibrators"),
]
