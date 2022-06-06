from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render

from django.db.models import Sum, F
from products.models import Product

# Import models from Purchases, products, orders, suppliers

def dashboard(request):
    # Total Number of Products
    count = Product.objects.count()

    # Total Number of Products on Hand
    inventory_on_hand = Product.objects.aggregate(Sum('inventory_on_hand'))

    inventory_cost = Product.objects.aggregate(cost = Sum(F('price_per_piece') * F('inventory_on_hand')))
    inventory_value = Product.objects.aggregate(value = Sum(F('retail_per_piece') * F('inventory_on_hand')))
    
    try:
        sales_margin = inventory_value['value'] - inventory_cost['cost']
    except:
        sales_margin = 0;

    context = {
        'count': count,
        'inventory_on_hand': inventory_on_hand['inventory_on_hand__sum'],
        'inventory_cost': inventory_cost['cost'],
        'inventory_value': inventory_value['value'],
        'sales_margin': sales_margin,
        
    }

    return render(request, 'dashboard/index.html', context)
    # return HttpResponse(template.render(context, request))

    return HttpResponse('')
