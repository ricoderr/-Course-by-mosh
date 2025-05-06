from django.shortcuts import render
from django.db.models import F, Func, Value, ExpressionWrapper, DecimalField, Q, Count
from django.db.models.aggregates import Min, Max, Count, Avg, Sum
from store.models import Product, Customer, Collection, Order, OrderItem, CartItem


def say_hello(request):
    queryset = Order.objects.annotate(total_item = Sum('orderitem__quantity')).filter(total_item__gt = 6).select_related('customer')
    count = queryset.count()
    return render(request, 'hello.html', {'name': 'Rijan',
                                          'queryset': queryset,
                                          'count': count
                                          })
