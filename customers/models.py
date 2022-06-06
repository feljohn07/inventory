from django.db import models
from django.forms import CharField, DateTimeField

class Customer(models.Model):
    firstname           = models.CharField(max_length=100)
    middlename          = models.CharField(max_length=100)
    lastname            = models.CharField(max_length=100)
    customer_address    = models.CharField(max_length=100)
    date_added          = models.DateTimeField()
    date_updated        = models.DateTimeField()

    def __str__(self):
        return self.name