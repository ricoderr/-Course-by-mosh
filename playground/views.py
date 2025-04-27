from django.shortcuts import render
from django.db.models import F, Func, Value, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Min, Max, Count, Avg, Sum
from store.models import Product, Customer


def say_hello(request):
    queryset = Product.objects.all()
    list(queryset)
    return render(request, 'hello.html', {'name': 'Rijan',
                                          'queryset': queryset})
