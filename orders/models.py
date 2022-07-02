from django.db import models

from products.models import Product
from customers.models import Customer
from datetime import datetime

class Order(models.Model):
    quantity            = models.IntegerField(default=0, blank=False)
    created_at          = models.DateTimeField(null=False, blank=False)
    updated_at          = models.DateTimeField(null=False, blank=False)
    product_id          = models.ForeignKey( Product , null=True ,on_delete=models.CASCADE)
    customer_id         = models.ForeignKey( Customer , null=True ,on_delete=models.SET_NULL)

    
    # def get_order_month(self):
        
    #     # return order month
    #     return datetime.strftime(self.created_at, "%m")