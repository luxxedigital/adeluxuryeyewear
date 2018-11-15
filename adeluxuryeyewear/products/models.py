from django.db import models

# Models for ADE Eyewear products

class Product(models.Model):
    eyewear_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.CharField(max_length=150)
    quantity = models.IntegerField()
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    )
    gender = models.CharField(max_length=1, choices=gender_options, default='F')
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