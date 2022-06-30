import imp
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Value as V
from django.db.models.functions import Concat 
from datetime import datetime

from .models import Customer
from .forms import CustomerForm

from django.contrib.auth.decorators import login_required

# Pagination
from django.core.paginator import Paginator

@login_required
def index(request):

    form = CustomerForm

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
        'customers'     : customers,
        'num_of_pages'  : num_of_pages,
        'form'          : form,     
    }

    return render(request, 'customers/index.html', context)


@login_required
def add_view(request):
    return render(request,'customers/add.html', {})


@login_required
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


@login_required
def update_view(request, id):
    customer = Customer.objects.get(id=id)
    return render(request,'customers/update.html', {'customer': customer})
    

@login_required
def update(request, id):
    customer = Customer.objects.get(id=id)

    customer.firstname = request.POST['firstname']
    customer.middlename = request.POST['middlename']
    customer.lastname = request.POST['lastname']
    customer.customer_address = request.POST['customer_address']
    customer.date_updated = datetime.now()
    customer.save()

    return HttpResponseRedirect(reverse('customers'))

@login_required
def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()

    return HttpResponseRedirect(reverse('customers'))


@login_required
def search_customer(request):

    if 'term' in request.GET:

        # Query 
        query_customers = Customer.objects.annotate(full_name = Concat('firstname', V(' '), 'middlename', V(' '), 'lastname')).filter(full_name__icontains = request.GET['term'])

        customers = list()

        for customer in query_customers:
            customers.append({'label' : customer.firstname + ' ' + customer.middlename + '  ' + customer.lastname, 'value': {'id': customer.id, 'url': request.build_absolute_uri('/') + 'customers/view/' + str(customer.id)}})

        return JsonResponse(customers, safe=False)
