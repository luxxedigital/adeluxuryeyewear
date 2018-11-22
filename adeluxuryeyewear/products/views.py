from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

##############
# List Views
##############

def view_all(request):
    """Returns all the objects in the Product model (all glasses)"""
    collection_all = Product.objects.all()

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_all,
        'collection': 'all'
    })

def view_featured(request):
    """Returns all the featured eyewear objects from the Product model"""
    collection_featured = Product.objects.filter(featured__exact=True)

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_featured,
        'collection': 'featured'
    })


def view_men(request):
    """Returns all the men(King's line) eyewear objects from Product model"""
    collection_men = Product.objects.filter(line='KL')

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_men,
        'collection': 'KL'
    })

def view_women(request):
    """Returns all the women(Queen's line) eyewear objects from Product model"""
    collection_women = Product.objects.filter(line='QL')

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_women,
        'collection': 'QL'
    })

def view_unisex(request):
    """Returns all the unisex(Unisex line) eyewear objects from Product model"""
    collection_unisex = Product.objects.filter(line='UL')

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_unisex,
        'collection': 'UL'
    })

#################
# Sort-by Views
#################

def sort_by_price__low(request, line):
    """ Sorts a collection by price(low-high). The line is either 'all', 'KL', 'QL', or 'UL'.
        Return the objects in that collection sorted by that criteria.
    """

    if line != 'KL' and line != 'QL' and line != 'UL':
        collection_by_price = Product.objects.all().order_by('price')
    else:
        # TODO: Fix passing the line variable for all collections as a parameter.
        if line == 'all':
            collection_by_price = Product.objects.filter(line=line).order_by('price')
            line = 'all'
        else:
            collection_by_price = Product.objects.filter(featured__exact=True).order_by('price')
            line = 'featured'

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_by_price,
        'collection': line
    })

def sort_by_price__high(request, line):

    if line != 'KL' and line != 'QL' and line != 'UL':
        collection_by_price = Product.objects.all().order_by('-price')
        line = 'all'
    else:
        collection_by_price = Product.objects.filter(line=line).order_by('-price')

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_by_price,
        'collection': line
    })

def sort_by_promo_price__low(request, line):

    if line != 'KL' and line != 'QL' and line != 'UL':
        collection_by_promo_price = Product.objects.all().order_by('promotional_price')
        line = 'all'
    else:
        collection_by_promo_price = Product.objects.filter(line=line).order_by('promotional_price')

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_by_promo_price,
        'collection': line
    })

def sort_by_promo_price__high(request, line):

    if line != 'KL' and line != 'QL' and line != 'UL':
        collection_by_promo_price = Product.objects.all().order_by('-promotional_price')
        line = 'all'
    else:
        collection_by_promo_price = Product.objects.filter(line=line).order_by('-promotional_price')

    return render(request, 'products/collection_list.html', context={
        'ade_collection': collection_by_promo_price,
        'collection': line
    })

def sort_by_name__ascending(request):
    pass

def sort_by_name__descending(request):
    pass

#################
# Detail View
#################

def collection_detail(request, id):
    collection_item = Product.objects.filter(eyewear_id=id)

    print(collection_item)

    return render(request, 'products/collection_detail.html', context={
        'ade_collection_item': collection_item
    })


