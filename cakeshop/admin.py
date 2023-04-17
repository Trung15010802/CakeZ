from django.contrib import admin
from .models import Category, Cake

# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity','price', 'image_url')
    
admin.site.register(Category)
admin.site.register(Cake, CakeAdmin)