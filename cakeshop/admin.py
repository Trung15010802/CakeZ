from django.contrib import admin
from .models import Category, Cake

# Register your models here.


class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price', 'image_url')
    search_fields = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Cake, CakeAdmin)
