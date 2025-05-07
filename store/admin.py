from django.contrib import admin
from . import models
admin.site.site_header="Rijan's authorized person space (-)"
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ['title', 'unit_price', 'collection']
admin.site.register(models.Collection)
