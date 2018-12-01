from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='all/'), name='products'),
]

# Filter-by collection
urlpatterns += [
    path('all/', views.view_all, name='collection__all'),
    path('featured/', views.view_featured, name='collection__featured'),
    path('KL/', views.view_men, name='collection__men'),
    path('QL/', views.view_women, name='collection__women'),
    path('UL/', views.view_unisex, name='collection__unisex'),
]

# Sort-by criteria
urlpatterns += [
    path('<str:line>/priority__low-price', views.sort_by_price__low, name='sortby_price-low'),
    path('<str:line>/priority__high-price', views.sort_by_price__high, name='sortby_price-high'),
    path('<str:line>/priority__low-promo-price', views.sort_by_promo_price__low, name='sortby_promoprice-low'),
    path('<str:line>/priority__high-promo-price', views.sort_by_promo_price__high, name='sortby_promoprice-high')
]

# Route for a detail view of the product
urlpatterns += [
    path('<int:id>/', views.collection_detail, name='collection__detail')
]
