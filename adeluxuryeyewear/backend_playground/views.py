from django.shortcuts import render
from products.models import Product

def view_all(request):
    """Returns all the objects in the Product model (all glasses)"""
    collection_all = Product.objects.all()

    return render(request, 'backend_playground/filter_collections.html', context={
        'ade_collection': collection_all
    })

def view_men(request):
    """Returns all the men eyewear objects from Product model"""
    collection_men = Product.objects.filter(gender='M')

    return render(request, 'backend_playground/filter_collections.html', context={
        'ade_collection': collection_men
    })

def view_women(request):
    """Returns all the women eyewear objects from Product model"""
    collection_women = Product.objects.filter(gender='F')

    return render(request, 'backend_playground/filter_collections.html', context={
        'ade_collection': collection_women
    })

def view_unisex(request):
    """Returns all the unisex eyewear objects from Product model"""
    collection_women = Product.objects.filter(gender='U')

    return render(request, 'backend_playground/filter_collections.html', context={
        'ade_collection': collection_women
    })