"""Root url conf. """

from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

# URL Routes #

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    path('ade/', include('ade.urls'))
]

urlpatterns += [
    path('about/', include('about.urls'))
]

urlpatterns += [
    path('contact/', include('contact.urls'))
]

urlpatterns += [
    path('users/', include('users.urls'))
]

urlpatterns += [
    path('products/', include('products.urls'))
]

urlpatterns += [
    path('checkout/', include('checkout.urls'))
]