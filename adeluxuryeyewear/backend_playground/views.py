from django.shortcuts import render
from products.models import Product


##############
# List Views
##############

def view_all(request):
    """Returns all the objects in the Product model (all glasses)"""
    collection_all = Product.objects.all()

    return render(request, 'backend_playground/collection_list.html', context={
        'ade_collection': collection_all
    })

def view_men(request):
    """Returns all the men(King's line) eyewear objects from Product model"""
    collection_men = Product.objects.filter(line='KL')

    return render(request, 'backend_playground/collection_list.html', context={
        'ade_collection': collection_men
    })

def view_women(request):
    """Returns all the women(Queen's line) eyewear objects from Product model"""
    collection_women = Product.objects.filter(line='QL')

    return render(request, 'backend_playground/collection_list.html', context={
        'ade_collection': collection_women
    })

def view_unisex(request):
    """Returns all the unisex(Unisex line) eyewear objects from Product model"""
    collection_unisex = Product.objects.filter(line='UL')

    return render(request, 'backend_playground/collection_list.html', context={
        'ade_collection': collection_unisex
    })

#################
# Sort-by Views
#################

def sort_by_price__low(request, line):
    collection_by_price = Product.objects.filter(line=line).order_by('price')

    return render(request, 'backend_playground/collection_list.html', context={
        'ade_collection': collection_by_price,
    })

def sort_by_price__high(request, line):
    collection_by_price = Product.objects.filter(line=line).order_by('-price')

    return render(request, 'backend_playground/collection_list.html', context={
        'ade_collection': collection_by_price,
    })

def sort_by_promo_price(request):
    pass

def sort_by_alphabetical(request):
    pass

#################
# Detail View
#################

def collection_detail(request, id):
    collection_item = Product.objects.filter(eyewear_id=id)

    print(collection_item)

    return render(request, 'backend_playground/collection_detail.html', context={
        'ade_collection_item': collection_item
    })