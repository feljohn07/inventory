from tkinter.tix import Tree
from django.db import models
from django.forms import CharField

class Supplier(models.Model):
    supplier = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    date_added = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.supplier