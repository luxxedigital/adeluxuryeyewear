from django.contrib import admin
from django.conf.urls import url, include
from . import views


# we can change the name of the uris later
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
    url(r'^products/', include('products.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^checkout/', include('checkout.urls')),

]
