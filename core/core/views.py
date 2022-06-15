import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from core.models import Product


def autocomplete(request):
    if 'term' in request.GET:
        qs = product.objects.filter(title__icontains=request.GET.get('term')) #it will be in the request and to filter those things there
        titles = list() #python list in JSON
        for product in qs:  #loop through query set and append those title to the title list
            titles.append(product.title)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, 'core/home.html')