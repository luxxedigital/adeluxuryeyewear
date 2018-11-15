from django.contrib import admin

# Register your models here.
from products.models import Product
from products.models import Specs
from products.models import Features

admin.site.register(Product)
admin.site.register(Specs)
admin.site.register(Features)