"""Root URLconf"""

from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import RedirectView
from . import views

# URL Routes #

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', RedirectView.as_view(url='ade/'), name='index')
]

urlpatterns += [
    path('ade/', include('ade.urls'))
]

urlpatterns += [
    path('about/', include('about.urls'), name='about')
]

urlpatterns += [
    path('contact/', include('contact.urls'), name='contact')
]

urlpatterns += [
    path('users/', include('users.urls'))
]

urlpatterns += [
    path('products/', include('products.urls'), name='collections')
]

urlpatterns += [
    path('checkout/', include('checkout.urls'), name='checkout')
]

# Route for backend-testing
urlpatterns += [
    path('bendplay/', include('backend_playground.urls'))
]