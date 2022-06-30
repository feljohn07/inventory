from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Supplier

from datetime import datetime

# Pagination
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    # Number of rows to display
    no_rows         = 5
    # Set Up Pagination
    paginator       = Paginator(Supplier.objects.all(), no_rows)
    # Track the page
    page            = request.GET.get('page')
    # product list
    suppliers         = paginator.get_page(page)
    # number of pages
    num_of_pages    = range(suppliers.paginator.num_pages)

    context     = {
        'suppliers': suppliers,
        'num_of_pages': num_of_pages,
    }
    return render(request,'suppliers/index.html', context)


@login_required
def add_view(request):
    return render(request,'suppliers/add.html', {})


@login_required
def add(request):
    suppliers = Supplier(
        supplier        = request.POST['supplier'], 
        address         = request.POST['address'],
        date_added      = datetime.now(),
    )
    suppliers.save()
    return HttpResponseRedirect(reverse('suppliers'))


@login_required
def update_view(request, id):
    supplier = Supplier.objects.get(id=id)
    return render(request,'suppliers/update.html', {'supplier':supplier})


@login_required
def update(request, id):
    # return HttpResponse(id)
    supplier            = Supplier.objects.get(id=id)
    supplier.supplier   = request.POST['supplier']
    supplier.address    = request.POST['address']
    supplier.save()

    return HttpResponseRedirect(reverse('suppliers'))