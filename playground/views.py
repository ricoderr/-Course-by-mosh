from django.shortcuts import render
from django.db.models import Q,F
from django.http import HttpResponse
from store.models import Product, OrderItem



def say_hello(request):
    # output = ordered product sorted according to the title
    query_set= Product.objects.select_related('collection').all()
    count = query_set.count()

    return render(request, 'hello.html', {'name': 'Mosh',
                                          'Products': query_set, 
                                          'Total_products': count})
