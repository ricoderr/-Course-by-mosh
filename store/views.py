from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, CollectionSerializer
from .models import Product, Collection



@api_view(['GET', 'POST'])
def product_list(request):
    if request.method =='GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST': 
        serializer = ProductSerializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, pk): 
    product=get_object_or_404(Product, pk=pk)
    
    if request.method == 'GET': 
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT': 
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE': 
        if product.orderitems.count() >0: 
            return Response({'error': 'product cannot be deleted because it is associated with an order item'},status= status.HTTP_405_METHOD_NOT_ALLOWED)
        
        else: 
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        

@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET': 
        queryset = Collection.objects.annotate(product_count = Count('product')).all()
        serializer = CollectionSerializer(
            queryset, many = True
        )
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        serializer = CollectionSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk): 
    collection = get_object_or_404(Collection, pk=pk)
    
    if request.method == 'GET': 
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT': 
        serializer = CollectionSerializer(collection, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE': 
        if collection.product.count() >0: 
            return Response({'error': 'The specific collection is forbidden to be deleted because products is present in the collection.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else: 
            collection.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        

    

# It helps or it instructs django that this is a api view. automatic json response.
# {"rijan": 12,
# "arpan": 10}

# json acts as a bridge between api and client. client --request--> api --response in form of json file--> client

