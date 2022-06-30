from datetime import datetime
from itertools import product
from unicodedata import category
from django.db import models
from django.forms import CharField, DateTimeField

from suppliers.models import Supplier

class Product(models.Model):
    product_name        = models.CharField(max_length=125)
    price_per_piece     = models.DecimalField(max_digits=10, decimal_places=2) # Cost Price
    retail_per_piece    = models.DecimalField(max_digits=10, decimal_places=2) # Retail Price
    product_category    = models.CharField(max_length=50) #Category Id
    inventory_received  = models.IntegerField(default=0, blank=True, null=True)
    inventory_shipped   = models.IntegerField(default=0, blank=True, null=True)
    inventory_on_hand   = models.IntegerField(default=0, blank=True, null=True)
    minimum_required    = models.IntegerField(default=0, blank=True, null=True)

    supplier            = models.ForeignKey(Supplier , null=True ,on_delete=models.CASCADE)
    created_at          = models.DateField(default = datetime.now)
    updated_at          = models.DateField()


class Category(models.Model):
    category = models.CharField(max_length=125)
    created_at = models.DateField( default = datetime.now)
