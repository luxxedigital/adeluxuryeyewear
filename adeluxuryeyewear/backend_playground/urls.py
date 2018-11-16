from django.urls import path
from . import views

#################################################################
# Add a special routes with a view to experiment with your code
#################################################################

# Developing products filtering
urlpatterns = [
    path('filter/', views.view_all),
    path('filter/all', views.view_all, name='view-all'),
    path('filter/men', views.view_men, name='view-men'),
    path('filter/women', views.view_women, name='view-women'),
    path('filter/unisex', views.view_unisex, name='view-unisex'),
]
