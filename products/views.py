from django.shortcuts import render
from django.http import HttpResponse

# /products -> index
#Uniform Resource Locator aka address

#functions for dealing with requests that basically tell django what to display on the page
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')


