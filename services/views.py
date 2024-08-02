from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def services_func(request):
    template = loader.get_template("services/services.html")
    context = {
        "services":"services",
        }
     
    return HttpResponse(template.render(context, request))