from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset, many=True, context = {'request': request})
    return Response(serializer.data)
    
@api_view()
def product_details(request, pk): 
    product=get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, context = {'request': request})
    return Response(serializer.data)

@api_view()
def collection_detail(request, pk): 
    return Response("OK Tested!")
    

# It helps or it instructs django that this is a api view. automatic json response.
# {"rijan": 12,
# "arpan": 10}

# json acts as a bridge between api and client. client --request--> api --response in form of json file--> client

