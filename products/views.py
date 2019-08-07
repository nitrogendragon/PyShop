from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# /products -> index
#Uniform Resource Locator aka address


#functions for dealing with requests that basically tell django what to display on the page


def index(request):
    products = Product.objects.all() # get all products
    # Product.objects.filter() #filter by cost or stock etc
    # Product.objects.get()#get a single product
    # Product.objects.save #insert or update new/existing product
    #return HttpResponse('Hello World')
    #call render function with the server request, the template file name, and a dictionary that contains
    #the data to be passed to the template
    return render(request, 'index.html',
                  {'products': products})

def new(request):
    return HttpResponse('New Products')


