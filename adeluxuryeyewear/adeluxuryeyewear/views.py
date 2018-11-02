from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """ Displays ADE home page """

    # Get all index data

    return render(request, 'index.html')
