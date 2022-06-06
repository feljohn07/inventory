from ast import Or
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Order
from purchases.models import Product

# Datetime
from datetime import datetime

def index(request):
    orders = Order.objects.all().values()
    return render(request, 'orders/index.html', {'orders': orders})

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
