from django.contrib import admin
from . import models
admin.site.site_header="Rijan's authorized person space (-)"
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ['title', 'unit_price', 'collection', 'inventory_status']
    list_editable = ['collection']
    ordering = ['title', 'unit_price']
    list_per_page = 10
    @admin.display(ordering='inventory')
    def inventory_status(self, product): 
        if product.inventory < 10: 
            return 'low'
        return 'ok'
admin.site.register(models.Collection)
