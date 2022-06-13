from django.db import models

from products.models import Product
from datetime import datetime

class Order(models.Model):
    quantity            = models.IntegerField(default=0, blank=False)
    status              = models.CharField(max_length=100)
    created_at          = models.DateTimeField(null=False, blank=False)
    updated_at          = models.DateTimeField(null=False, blank=False)
    product_id          = models.ForeignKey( Product , null=True ,on_delete=models.SET_NULL)
    # customer_id         = models.ForeignKey( Product , null=True ,on_delete=models.SET_NULL)

    
    # def get_order_month(self):
        
    #     # return order month
    #     return datetime.strftime(self.created_at, "%m")