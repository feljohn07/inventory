from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render

from django.db.models import Sum, F

from products.models import Product

from purchases.models import Purchase

from orders.models import Order

from datetime import date, datetime

# Import models from Purchases, products, orders, suppliers

def dashboard(request):

    # Total Number of Products
    count = Product.objects.count()

    # Total Number of Products on Hand
    inventory_on_hand = Product.objects.aggregate(Sum('inventory_on_hand'))

    # Total Inventory on Hand
    inventory_cost = Product.objects.aggregate(cost = Sum(F('price_per_piece') * F('inventory_on_hand')))

    # Total Number of products
    inventory_value = Product.objects.aggregate(value = Sum(F('retail_per_piece') * F('inventory_on_hand')))

    # Total Purchased Product today
    purchases = Purchase.objects.filter(
        created_at__year = datetime.now().year,
        created_at__month = datetime.now().month,
        created_at__day = datetime.now().day,
    ).count()

    # Total Ordered Products today
    orders = Order.objects.filter(
        created_at__year = datetime.now().year,
        created_at__month = datetime.now().month,
        created_at__day = datetime.now().day,
    ).count()

    
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
        'purchases': purchases,
        'orders': orders,
    }

    return render(request, 'dashboard/index.html', context)
    # return HttpResponse(template.render(context, request))

    return HttpResponse('')
