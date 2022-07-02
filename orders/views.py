from ast import Or
from math import prod
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render

from django.core.paginator import Paginator

from customers.models import Customer

from .models import Order
from purchases.models import Product

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Datetime
from datetime import datetime

@login_required
def index(request):

    # Number of rows to display
    no_rows         = 5
    # Set Up Pagination
    paginator       = Paginator(
                            Order.objects
                            .all()
                            .values(
                                'id',
                                'created_at',
                                'quantity',
                                'product_id__product_name',
                                'customer_id_id__firstname'
                            )
                            .order_by('-id')
                        , no_rows)
    # Track the page
    page            = request.GET.get('page')
    # product list
    orders         = paginator.get_page(page)
    # number of pages
    num_of_pages    = range(orders.paginator.num_pages)

    context = {
        'orders'        : orders,
        'num_of_pages'  : num_of_pages,
    }
    return render(request, 'orders/index.html', context)


@login_required
def add_view(request):

    products = Product.objects.all()
    customer = Customer.objects.all()

    return render(request, 'orders/add.html', {'products': products, 'customer': customer})


@login_required
def add(request):

    order = Order(
        product_id  = Product.objects.get(id = request.POST['product_id']), # get the instance of the Model object Product
        customer_id  = Customer.objects.get(id = request.POST['customer_id']), # get the instance of the Model object Product
        quantity    = request.POST['quantity'],
        created_at  = request.POST['created_at'],
        updated_at  = datetime.now(),
    )

    # Product Instance
    product = Product.objects.get(id = request.POST['product_id'])
    product.inventory_shipped   = product.inventory_shipped + int(request.POST['quantity'])
    product.inventory_on_hand   = product.inventory_on_hand - int(request.POST['quantity'])

    order.save()
    product.save()

    return HttpResponseRedirect(reverse('orders'))


@login_required
def delete(request, id):
    
    order = Order.objects.get(id = id)
    product  = Product.objects.get(id = order.product_id_id)
    product.inventory_shipped  = product.inventory_shipped - int(order.quantity)
    product.inventory_on_hand   = product.inventory_on_hand + int(order.quantity)

    order.delete()
    product.save()

    return HttpResponseRedirect(reverse('orders'))


@csrf_exempt
@login_required
def save_edit_quantity(request):


    if request.method == "POST":

        order  = Order.objects.get(id = request.POST['id'])
        product  = Product.objects.get(id = order.product_id_id)

        product.inventory_shipped  = product.inventory_shipped + (int(request.POST['quantity']) - int(order.quantity))
        product.inventory_on_hand   = product.inventory_on_hand - (int(request.POST['quantity']) - int(order.quantity))

        order.quantity = request.POST['quantity']
        order.save()
        product.save()
        
        return JsonResponse({'quantity': int(request.POST['quantity']) - int(order.quantity)}, safe=False)
