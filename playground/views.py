from django.shortcuts import render
from django.db.models import F, Func, Value, ExpressionWrapper, DecimalField, Q
from django.db.models.aggregates import Min, Max, Count, Avg, Sum
from store.models import Product, Customer, Collection


def say_hello(request):
    
    return render(request, 'hello.html', {'name': 'Rijan'
                                          })
