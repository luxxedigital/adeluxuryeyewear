from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.products),
    path('featured-line/', views.featured_line),
    path('kings-line/', views.kings_line),
    path('queens-line/', views.queens_line),
    path('unisex-line/', views.unisex_line),
    path('', views.products, name='products'),
    path('detail/', views.detail, name='detail')
]