from django.db import models

from suppliers.models import Supplier
from products.models import Product

class Purchase(models.Model):
    quantity            = models.IntegerField(default=0, blank=False)
    created_at          = models.DateTimeField(null=False, blank=False)
    updated_at          = models.DateTimeField(null=False, blank=False)
    product_id          = models.ForeignKey( Product , null=True ,on_delete=models.CASCADE)