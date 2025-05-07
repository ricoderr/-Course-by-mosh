from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

@api_view()
def product_list(request):
    return Response("hello")
    
@api_view()
def product_details(request, id): 
    try:
        product=Product.objects.get(pk=1)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except product.DoesNotExist(): 
        return Response(status=status.HTTP_404_NOT_FOUND)

# It helps or it instructs django that this is a api view. automatic json response.
# {"rijan": 12,
# "arpan": 10}

# json acts as a bridge between api and client. client --request--> api --response in form of json file--> client

