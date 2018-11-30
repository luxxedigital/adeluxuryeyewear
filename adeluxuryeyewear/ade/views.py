from django.shortcuts import render
from django.http import HttpResponse
import cart.cart as cart
import json

# Home page view
def index(request):
    """ *Test only """

    msg = 'Hello World!'

    # The data sent to the template
    context = {
        'message': msg
    }

    # creates cart session
    if request.session.get('cart') is None:
        request.session.set_expiry(259200)
        cart.initializeCart(request)

    # testing purposes only
    print(request.session['cart'])

    # The return response - the template with the data(context)
    return render(request, 'ade/index.html', context)

