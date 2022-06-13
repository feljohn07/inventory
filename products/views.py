from datetime import datetime
from math import prod
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Pagination
from django.core.paginator import Paginator

# Models
from .models import Product

# Supplier Model
from suppliers.models import Supplier

# Purchase and Order Models
from purchases.models import Purchase
from orders.models import Order


def index(request, *args, **kwargs):


    # return HttpResponse(Product.objects
    #                             .all()
    #                             .values(
    #                                 'id',
    #                                 'product_name',
    #                                 'price_per_piece',
    #                                 'retail_per_piece',
    #                                 'variant',
    #                                 'product_category',
    #                                 'inventory_received',
    #                                 'inventory_shipped',
    #                                 'inventory_on_hand',
    #                                 'minimum_required',
    #                                 'supplier__supplier'
    #                                 ) 
    #                             )

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
                                    'variant',
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


def add_view(request):

    suppliers = Supplier.objects.all()
    
    return render(request,'products/add.html', {'suppliers': suppliers})


def add(request):

    # return HttpResponse(request.POST['supplier_id'])
    product = Product(
        supplier_id         = request.POST['supplier_id'], 
        product_name        = request.POST['product_name'], 
        price_per_piece     = request.POST['price_per_piece'],
        retail_per_piece    = request.POST['retail_per_piece'],
        variant             = request.POST['variant'],
        product_category    = request.POST['product_category'],
        inventory_received  = request.POST['inventory_received'],
        inventory_on_hand   = request.POST['inventory_received'],
        minimum_required    = request.POST['minimum_required'],
        updated_at          = datetime.now(),
    )
    # return HttpResponse()
    product.save()
    return HttpResponseRedirect(reverse('products'))


def update_view(request, id):
    product = Product.objects.get(id=id)
    # return HttpResponse(product.supplier_id)
    supplier = Supplier.objects.get(id = product.supplier_id)

    return render(request,'products/update.html', {'product':product, 'supplier':supplier.supplier})


def update(request, id):

    product = Product.objects.get(id=id)

    product.product_name        = request.POST['product_name']
    product.price_per_piece     = request.POST['price_per_piece']
    product.retail_per_piece    = request.POST['retail_per_piece']
    product.variant             = request.POST['variant']
    product.product_category    = request.POST['product_category']

    # Add or 
    # if int(request.POST['inventory_received']) > 0:
    #     product.inventory_received  = product.inventory_received + int(request.POST['inventory_received'])
    # else:
    #     product.inventory_shipped  = product.inventory_shipped + int(request.POST['inventory_received'])

    # product.inventory_on_hand   = product.inventory_on_hand + int(request.POST['inventory_received'])
    product.minimum_required    = request.POST['minimum_required'] 

    product.save()

    return HttpResponseRedirect(reverse('products'))

