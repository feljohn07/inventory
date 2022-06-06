from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Supplier

from datetime import datetime


def index(request):
    # Retrieve all products
    suppliers = Supplier.objects.all().values()
    context = {
        'suppliers': suppliers,
    }
    return render(request,'suppliers/index.html', context)

def add_view(request):
    return render(request,'suppliers/add.html', {})

def add(request):
    suppliers = Supplier(
        supplier        = request.POST['supplier'], 
        address         = request.POST['address'],
        date_added      = datetime.now(),
    )
    suppliers.save()
    return HttpResponseRedirect(reverse('suppliers'))

def update_view(request, id):
    supplier = Supplier.objects.get(id=id)
    return render(request,'suppliers/update.html', {'supplier':supplier})

def update(request, id):
    # return HttpResponse(id)
    supplier = Supplier.objects.get(id=id)
    supplier.supplier   = request.POST['supplier']
    supplier.address    = request.POST['address']
    supplier.save()

    return HttpResponseRedirect(reverse('suppliers'))