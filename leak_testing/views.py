from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def leak_func(request):
    template = loader.get_template("leak_testing/leak_testing.html")
    context = {
        "leak":"leak",
        }
     
    return HttpResponse(template.render(context, request))