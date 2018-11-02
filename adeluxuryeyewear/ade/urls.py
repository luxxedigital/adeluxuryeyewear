from django.urls import path
from . import views

# Home page routes

urlpatterns = [
    path('', views.index, name='index')
]
