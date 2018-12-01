# a mini api for the cart
# this is what is going to be used in the rest of the application
from .models import Cart
import json

# initializes a session for the cart
def initializeCart(request):
    cart = Cart()

    # loads the session with empty variables
    request.session['cart'] = cart.get()
    del cart # Cart class is only used to load into session

# appends the new item to the session var
def addToCart(request, product, quantity):
    cart = Cart(load=request.session['cart'])

    # only adds the id and the quantity of the product
    filtered_item = {
        'id': product.eyewear_id,
        'quantity': quantity
    }

    cart.addToCart(filtered_item)

    # reloads the json into the session var
    request.session['cart'] = cart.get()
    del cart

def changeItemQuantity(request, product, new_quantity):
    cart = Cart(load=request.session['cart'])

    filtered_item = {
        'id': product.eyewear_id,
        'price': product.promotional_price
    }

    cart.changeQuantity(filtered_item, new_quantity)
    request.session['cart'] = cart.get()
    del cart

def deleteFromCart(request, product):
    cart = Cart(load=request.session['cart'])

    filtered_item = {
        'product_id': product.eyewear_id,
        'price': product.promotional_price,
    }

    cart.deleteFromCart(filtered_item)
    request.session['cart'] = cart.get()
    del cart

# this will have all the data for the cart ready for the view
# not done
def refreshCart(request):
    cart = Cart(load=request.session['cart'])
    cart.populate()

    # do more stuff here

