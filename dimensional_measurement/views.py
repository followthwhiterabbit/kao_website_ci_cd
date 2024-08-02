from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def dimensional_func(request):
    template = loader.get_template("dimensional_measurement/dimensional_measurement.html")
    context = {
        "dimensional":"dimensional",
        }
     
    return HttpResponse(template.render(context, request))
