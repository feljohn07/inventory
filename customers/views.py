from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from datetime import datetime

from .models import Customer

# Pagination
from django.core.paginator import Paginator


def index(request):

    # Number of rows to display
    no_rows         = 5
    # Set Up Pagination
    paginator       = Paginator(Customer.objects.all(), no_rows)
    # Track the page
    page            = request.GET.get('page')
    # product list
    customers         = paginator.get_page(page)
    # number of pages
    num_of_pages    = range(customers.paginator.num_pages)

    context = {
        'customers'             : customers,
        'num_of_pages'          : num_of_pages,
    }

    return render(request, 'customers/index.html', context)


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