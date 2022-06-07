from ast import Or
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.core.paginator import Paginator

from .models import Order
from purchases.models import Product

# Datetime
from datetime import datetime

def index(request):

    # Number of rows to display
    no_rows         = 5
    # Set Up Pagination
    paginator       = Paginator(Order.objects.all().order_by('-id'), no_rows)
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
        product_id  = Product.objects.get(id = request.POST['product_id']),
        quantity    = request.POST['quantity'],
        created_at  = request.POST['created_at'],
        updated_at  = datetime.now(),
    )
    order.save()

    return HttpResponseRedirect(reverse('orders'))
