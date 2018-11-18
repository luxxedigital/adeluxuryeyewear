from django.urls import path
from . import views

#################################################################
# Add a special routes with a view to experiment with your code
#################################################################

# Filter-by routes
urlpatterns = [
    path('collection/', views.view_all),
    path('collection/all', views.view_all, name='collection-all'),
    path('collection/men', views.view_men, name='collection-men'),
    path('collection/women', views.view_women, name='collection-women'),
    path('collection/unisex', views.view_unisex, name='collection-unisex'),
]

urlpatterns += [
    path('collection/<str:line>/priority__lowprice', views.sort_by_price__low, name='sortby-price-low'),
    path('collection/<str:line>/priority__highprice', views.sort_by_price__high, name='sortby-price-high')
]


# Route for a detail view of the product
urlpatterns += [
    path('collection/<int:id>/', views.collection_detail, name='collection-detail')
]
