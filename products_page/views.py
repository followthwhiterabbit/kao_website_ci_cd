from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def products_func(request):
    template = loader.get_template("products/products_page.html")
    context = {
        "product":"our_products",
        }
     
    return HttpResponse(template.render(context, request))