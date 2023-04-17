from django.db import models
from django.db.models import Q

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Cake(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=0)
    description = models.TextField()
    image_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def search(query):
        return Cake.objects.filter(
            Q(name__icontains=query) | 
            Q(category__name__icontains=query) |
            Q(price__icontains=query) |
            Q(quantity__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
