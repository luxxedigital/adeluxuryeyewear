from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def products(request):
    return HttpResponse('products')

def featured_line(request):
    return HttpResponse("kings-line")

def kings_line(request):
    return HttpResponse("kings-line")

def queens_line(request):
    return HttpResponse("kings-line")

def unisex_line(request):
    return HttpResponse("kings-line")

# just to commit something