from ast import Or
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render

from django.core.paginator import Paginator

from .models import Order
from purchases.models import Product

from django.views.decorators.csrf import csrf_exempt

# Datetime
from datetime import datetime

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
                                'product_id__product_name'
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

def add_view(request):

    products = Product.objects.all()

    return render(request, 'orders/add.html', {'products': products})


def add(request):

    order = Order(
        product_id  = Product.objects.get(id = request.POST['product_id']), # get the instance of the Model object Product
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

def delete(request, id):
    
    order = Order.objects.get(id = id)
    order.delete()

    return HttpResponseRedirect(reverse('orders'))

@csrf_exempt
def save_edit_quantity(request):


    if request.method == "POST":

        order  = Order.objects.get(id = request.POST['id'])

        order.quantity = request.POST['quantity']
        order.save()
        
        return JsonResponse({'quantity': order.quantity}, safe=False)
