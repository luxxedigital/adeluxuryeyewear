from django.db import models

# Models for ADE Eyewear products

class Product(models.Model):
    """This model is used to represent a product in the shop."""
    eyewear_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    collection = (
        ('KL', 'Kings Line'),
        ('QL', 'Queens Line'),
        ('UL', 'Unisex Line'),
    )
    special_collection = (
        ('NS', 'Not Special'),
        ('WC', 'Wooden Collection'),
    )
    line = models.CharField(max_length=2, choices=collection, default='KL')
    special = models.CharField(max_length=2, choices=special_collection, default='NS')
    lens_width = models.CharField(max_length=15)
    lens_height = models.CharField(max_length=15)
    bridge_length = models.CharField(max_length=15)
    arm_length = models.CharField(max_length=15)
    image = models.CharField(max_length=150)
    original_price = models.FloatField()
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    )
    gender = models.CharField(max_length=1, choices=gender_options, default='M')
    price = models.FloatField()
    featured = models.BooleanField(default=False)

    # This gives the name of the object (the eyewear)
    def __str__(self):
        return self.name
    

class Instances(models.Model):
    """This model is to store the physical amount 
    there is for each product in the shop."""
    quantity = models.IntegerField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    
class Features(models.Model):
    """This model stores the features for each product."""
    feature = models.CharField(max_length=50)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

class Review(models.Model):
    """This model stores the reviews a product has."""
    username = models.CharField(max_length=25)
    review = models.TextField()
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

class Rating(models.Model):
    """This model stores the rating a product has."""
    rating = models.IntegerField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
