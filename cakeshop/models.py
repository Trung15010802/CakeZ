from django.db import models

# Create your models here.


class Cake(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.TextField(null=True, blank=True)
