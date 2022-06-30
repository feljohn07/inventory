from calendar import month
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render

from django.db.models import Sum, F, Count
from django.db.models.functions import TruncMonth, TruncYear
from pkg_resources import safe_extra

from products.models import Product

from purchases.models import Purchase

from orders.models import Order

from datetime import date, datetime

from django.contrib.auth.decorators import login_required

# Import models from Purchases, products, orders, suppliers
@login_required
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

    # Try catch if subracting inventory value with the cost (error occurs when one of the two has no value)
    try:
        sales_margin = inventory_value['value'] - inventory_cost['cost']
    except:
        sales_margin = 0;


    get_monthly_sales = (Order.objects
                            .annotate(month = TruncMonth('created_at'))
                            .values('month')
                            .filter(created_at__year = datetime.now().year)
                            .annotate(order_count = Count('created_at'))
                            .values('month','order_count')
                            .order_by()
                        )

    monthly_dict = [0,0,0,0,0,0,0,0,0,0,0,0,]
        
    for x in get_monthly_sales:
        if datetime.strftime(x['month'], "%m") == '00':
            monthly_dict[0] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '01':
            monthly_dict[1] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '02':
            monthly_dict[2] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '03':
            monthly_dict[3] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '04':
            monthly_dict[4] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '05':
            monthly_dict[5] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '06':
            monthly_dict[6] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '07':
            monthly_dict[7] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '08':
            monthly_dict[8] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '09':
            monthly_dict[9] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '10':
            monthly_dict[10] = x['order_count']

        if datetime.strftime(x['month'], "%m") == '11':
            monthly_dict[11] = x['order_count']


    # return HttpResponse(get_monthly_sales)
    context = {
        'count': count,
        'inventory_on_hand' : inventory_on_hand['inventory_on_hand__sum'],
        'inventory_cost'    : inventory_cost['cost'],
        'inventory_value'   : inventory_value['value'],
        'sales_margin'      : sales_margin,
        'purchases'         : purchases,
        'orders'            : orders,
        'get_monthly_sales' : monthly_dict, # return a json string
    }

    return render(request, 'dashboard/index.html', context)
    # return HttpResponse(template.render(context, request))

    return HttpResponse('')

@login_required
def search(request):

    if 'term' in request.GET:

        query_products = Product.objects.filter(product_name__icontains=request.GET['term'])

        products = list()
        for product in query_products:
            products.append({'label' : product.product_name, 'value': {'id': product.id, 'url': request.build_absolute_uri('/') + 'products/view/' + str(product.id)}})

        return JsonResponse(products, safe=False)

    # return JsonResponse('products', safe=False)

