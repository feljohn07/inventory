from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from datetime import datetime

from .models import Customer


def index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {'customers':customers})


def add_view(request):
    return render(request,'customers/add.html', {})


def add(request):
    customer = Customer(
        firstname           = request.POST['firstname'],
        middlename          = request.POST['middlename'],
        lastname            = request.POST['lastname'],
        customer_address    = request.POST['customer_address'],
        date_added          = datetime.now(),
        date_updated        = datetime.now(),
    )
    customer.save()
    return HttpResponseRedirect(reverse('customers'))


def update_view(request, id):
    customer = Customer.objects.get(id=id)
    return render(request,'customers/update.html', {'customer': customer})
    

def update(request, id):
    customer = Customer.objects.get(id=id)

    customer.firstname = request.POST['firstname']
    customer.middlename = request.POST['middlename']
    customer.lastname = request.POST['lastname']
    customer.customer_address = request.POST['customer_address']
    customer.date_updated = datetime.now()
    customer.save()

    return HttpResponseRedirect(reverse('customers'))