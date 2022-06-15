from django.db import models

# Create your models here.

class products(models.Model):
    title = models.Charfield(max_lenght=124)
    qty = model.IntergerField()

    def __str__(self):
        return self.title