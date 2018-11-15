from django.db import models

# Models for ADE Eyewear products

class Product(models.Model):
    eyewear_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    category = (
        ('KL', 'Kings Line'),
        ('QL', 'Queens Line'),
        ('UL', 'Unisex Line')

    )
    line = models.CharField(max_length=2, choices=category, default='KL')
    image = models.CharField(max_length=150)
    price = models.FloatField()
    quantity = models.IntegerField()
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    )
    gender = models.CharField(max_length=1, choices=gender_options, default='M')
    promotional_price = models.FloatField()

class Specs(models.Model):
    # Specs
    lens_width = models.CharField(max_length=15)
    lens_height = models.CharField(max_length=15)
    bridge_length = models.CharField(max_length=15)
    arm_length = models.CharField(max_length=15)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    
class Features(models.Model):
    # Features
    feature = models.CharField(max_length=50)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)

class Review(models.Model):
    username = models.CharField(max_length=50)
    review = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.ForeignKey("Rating", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)

class Rating(models.Model):
    rating = models.IntegerField()
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)
