from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Pagination
from django.core.paginator import Paginator

from .models import Purchase

# Import Product Model
from products.models import Product

# Datetime
from datetime import datetime


@login_required
def index(request):

    # Number of rows to display
    no_rows         = 5

    # Set Up Pagination
    paginator       = Paginator(
                            Purchase.objects
                                    .all()
                                    .values(
                                        'id',
                                        'quantity',
                                        'created_at',
                                        'product_id__product_name'
                                    )
                                    .order_by('-id'), no_rows
                            )
                    

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


@login_required
def add_view(request):
    products = Product.objects.all()
    return render(request, 'purchases/add.html', {'products': products} )


@login_required
def add(request):

    purchase = Purchase(
        product_id  = Product.objects.get(id = request.POST['product_id']),
        quantity    = request.POST['quantity'],
        created_at  = request.POST['created_at'],
        updated_at  = datetime.now(),
    )
    purchase.save()

    product                     = Product.objects.get(id = request.POST['product_id'])
    product.inventory_received  = product.inventory_received + int(request.POST['quantity'])
    product.inventory_on_hand   = product.inventory_on_hand + int(request.POST['quantity'])
    product.save()

    return HttpResponseRedirect(reverse('purchases'))


@login_required
def delete(request, id):

    purchase  = Purchase.objects.get(id = id)
    product  = Product.objects.get(id = purchase.product_id_id)

    product.inventory_received  = product.inventory_received - int(purchase.quantity)
    product.inventory_on_hand   = product.inventory_on_hand - int(purchase.quantity)

    purchase.delete()
    product.save()
    return HttpResponseRedirect(reverse('purchases'))


@csrf_exempt
@login_required
def save_edit_quantity(request):

    if request.method == "POST":

        purchase  = Purchase.objects.get(id = request.POST['id'])
        product  = Product.objects.get(id = purchase.product_id_id)

        product.inventory_received  = product.inventory_received + (int(request.POST['quantity']) - int(purchase.quantity))
        product.inventory_on_hand   = product.inventory_on_hand + (int(request.POST['quantity']) - int(purchase.quantity))

        purchase.quantity = request.POST['quantity']
        purchase.save()
        product.save()
        
        return JsonResponse({'quantity': int(request.POST['quantity']) - int(purchase.quantity) }, safe=False)

