from django.shortcuts import render
from django.http import HttpResponse

# Home page view
def index(request):
    """ *Test only """

    msg = 'Hello World!'

    # The data sent to the template
    context = {
        'message': msg
    }

    # The return response - the template with the data(context)
    return render(request, 'ade/index.html', context)

