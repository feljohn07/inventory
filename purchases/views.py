from itertools import product
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Purchase

# Import Product Model
from products.models import Product

# Datetime
from datetime import datetime

def index(request):
    purchases = Purchase.objects.all().order_by('-id')
    return render(request, 'purchases/index.html', {'purchases': purchases})

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
    
    return HttpResponseRedirect(reverse('purchases'))
