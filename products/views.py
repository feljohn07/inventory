from datetime import datetime
from math import prod
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Pagination
from django.core.paginator import Paginator

# Models
from .models import Product

# Supplier Model
from suppliers.models import Supplier

# Purchase and Order Models
from purchases.models import Purchase
from orders.models import Order


@login_required
def index(request, *args, **kwargs):

    # Number of rows to display
    no_rows         = 5
    # Set Up Pagination
    paginator       = Paginator(Product.objects
                                .all()
                                .values(
                                    'id',
                                    'product_name',
                                    'price_per_piece',
                                    'retail_per_piece',
                                    'product_category',
                                    'inventory_received',
                                    'inventory_shipped',
                                    'inventory_on_hand',
                                    'minimum_required',
                                    'supplier__supplier'
                                    ) , no_rows)
    # Track the page
    page            = request.GET.get('page')
    # product list
    product         = paginator.get_page(page)
    # number of pages
    num_of_pages    = range(product.paginator.num_pages)


    # Retrieve 5 recent purchases
    purchases       = ( Purchase.objects
                                .all()
                                .values(
                                    'id',
                                    'created_at',
                                    'product_id__product_name',
                                    'quantity',
                                    )
                                .order_by('-id')[:5]
    )

    # Retrieve 5 recent orders
    orders          = (Order.objects
                            .all()
                            .values(
                                    'id',
                                    'created_at',
                                    'product_id__product_name',
                                    'quantity',
                                    )
                            .order_by('-id')[:5])

    context = {
        'products'              : product,
        'num_of_pages'          : num_of_pages,
        'purchases'             : purchases,
        'orders'                : orders,
    }

    return render(request,'products/index.html', context)


@login_required
def add_view(request):

    suppliers = Supplier.objects.all()
    
    return render(request,'products/add.html', {'suppliers': suppliers})


@login_required
def add(request):

    # return HttpResponse(request.POST['supplier_id'])
    product = Product(
        supplier_id         = request.POST['supplier_id'], 
        product_name        = request.POST['product_name'], 
        price_per_piece     = request.POST['price_per_piece'],
        retail_per_piece    = request.POST['retail_per_piece'],
        product_category    = request.POST['product_category'],
        inventory_received  = request.POST['inventory_received'],
        inventory_on_hand   = request.POST['inventory_received'],
        minimum_required    = request.POST['minimum_required'],
        updated_at          = datetime.now(),
    )
    # return HttpResponse()
    product.save()
    return HttpResponseRedirect(reverse('products'))


@login_required
def update_view(request, id):
    product = Product.objects.get(id=id)
    # return HttpResponse(product.supplier_id)
    supplier = Supplier.objects.get(id = product.supplier_id)

    return render(request,'products/update.html', {'product':product, 'supplier':supplier.supplier})


@login_required
def update(request, id):

    product = Product.objects.get(id=id)

    product.product_name        = request.POST['product_name']
    product.price_per_piece     = request.POST['price_per_piece']
    product.retail_per_piece    = request.POST['retail_per_piece']
    product.product_category    = request.POST['product_category']
    product.minimum_required    = request.POST['minimum_required'] 

    product.save()

    return HttpResponseRedirect(reverse('products'))

@login_required
def delete(request, id):
    product = Product.objects.get(id=id)

    # return HttpResponse(product)
    product.delete()
    return HttpResponseRedirect(reverse('products'))

