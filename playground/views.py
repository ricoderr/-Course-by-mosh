from django.shortcuts import render
from django.db.models import F, Func, Value, ExpressionWrapper, DecimalField, Q, Count
from django.db.models.aggregates import Min, Max, Count, Avg, Sum
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    count = OrderItem.objects.filter(order__id = 1).annotate(income = F('unit_price')*F('quantity')).aggregate(Sum('income'))
    return render(request, 'hello.html', {'name': 'Rijan',
                                          'count': count
                                          })
