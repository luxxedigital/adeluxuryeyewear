from django.urls import path
from . import views

#################################################################
# Add a special routes with a view to experiment with your code
#################################################################

# Filter-by routes
urlpatterns = [
    path('collection/', views.view_all),
    path('collection/all', views.view_all, name='collection-all'),
    path('collection/KL', views.view_men, name='collection-men'),
    path('collection/QL', views.view_women, name='collection-women'),
    path('collection/UL', views.view_unisex, name='collection-unisex'),
]

urlpatterns += [
    path('collection/<str:line>/priority__low-price', views.sort_by_price__low, name='sortby_price-low'),
    path('collection/<str:line>/priority__high-price', views.sort_by_price__high, name='sortby_price-high'),
    path('collection/<str:line>/priority__low-promo-price', views.sort_by_promo_price__low, name='sortby_promoprice-low'),
    path('collection/<str:line>/priority__high-promo-price', views.sort_by_promo_price__high, name='sortby_promoprice-high')
]


# Route for a detail view of the product
urlpatterns += [
    path('collection/<int:id>/', views.collection_detail, name='collection-detail')
]
