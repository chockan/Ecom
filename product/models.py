from django.db import models
from datetime import datetime

# Create your models here.
class Product1(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ratings = models.DecimalField(max_digits=5, decimal_places=2) 
    description = models.TextField()
    stock = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    sold_by = models.CharField(max_length=200, null=False, blank=False,default="mr_cho")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    
    
    def __str__(self):
        return self.name
    
    
    
class DataModel(models.Model):
    name = models.CharField(max_length=50)  # Adjusted max_length
    phone_number = models.CharField(max_length=20)  # Adjusted max_length
    door_number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    town_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    district_pincode = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    message = models.TextField()  # Changed to TextField for potentially longer messages

    class Meta:
        # Optionally remove db_table to use Django's default table naming convention
        db_table = "DataModel"
