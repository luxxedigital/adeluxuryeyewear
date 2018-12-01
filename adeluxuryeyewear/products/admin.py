from django.contrib import admin

# Register your models here.
from products.models import Product, Instances, Features, Review, Rating, ProductDetailPhotos

admin.site.register(Product)
admin.site.register(Instances)
admin.site.register(Features)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(ProductDetailPhotos)