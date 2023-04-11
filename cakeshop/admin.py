from django.contrib import admin
from .models import Cake
# Register your models here.


class CakeAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'image_url')


admin.site.register(Cake, CakeAdmin)
