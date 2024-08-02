from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def callibrators_func(request):
    template = loader.get_template("callibrators/callibrators.html")
    context = {
        "callibrators":"callibrators",
        }
     
    return HttpResponse(template.render(context, request))