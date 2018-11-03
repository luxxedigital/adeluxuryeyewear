from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('<html><body><h1>Contact page</h1></body></html>')