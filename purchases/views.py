from itertools import product
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Pagination
from django.core.paginator import Paginator

from .models import Purchase

# Import Product Model
from products.models import Product

# Datetime
from datetime import datetime

def index(request):

    # Number of rows to display
    no_rows         = 5

    # Set Up Pagination
    paginator       = Paginator(Purchase.objects.all().order_by('-id'), no_rows)

    # Track the page
    page            = request.GET.get('page')

    # product list
    purchases       = paginator.get_page(page)
    
    # number of pages
    num_of_pages    = range(purchases.paginator.num_pages)

    context = {
        'purchases': purchases,
        'num_of_pages': num_of_pages,
    }

    return render(request, 'purchases/index.html', context)

def add_view(request):
    products = Product.objects.all()
    return render(request, 'purchases/add.html', {'products': products} )

def add(request):

    purchase = Purchase(
        product_id  = Product.objects.get(id = request.POST['product_id']),
        quantity    = request.POST['quantity'],
        # status
        created_at  = request.POST['created_at'],
        updated_at  = datetime.now(),
    )
    purchase.save()

    product                     = Product.objects.get(id = request.POST['product_id'])
    product.inventory_received  = product.inventory_received + int(request.POST['quantity'])
    product.inventory_on_hand   = product.inventory_on_hand + int(request.POST['quantity'])
    product.save()

    return HttpResponseRedirect(reverse('purchases'))
