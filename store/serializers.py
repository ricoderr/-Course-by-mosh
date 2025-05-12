from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer): 
    product_count = serializers.IntegerField()
    class Meta: 
        model = Collection
        fields = ['id', 'title', 'product_count']
   

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product
        fields = ['id', 'title','slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
            
    
    def calculate_tax(self, product:Product): 
        return product.unit_price * Decimal(1.1)
    
