from django.shortcuts import render
from .models import Product

from django.core.paginator import Paginator


def home_view(request):

    featured_products = Product.objects.order_by('priority')[:4]

    latest_products = Product.objects.order_by('-created_at')[:4]

    return render(request, 'index.html', {'featured_products': featured_products, 'latest_products': latest_products, 'stars': range(5), 'rating': 3})


def products_view(request):

    page = 1

    if request.GET:
        page = int(request.GET.get('page', 1))

    product_list = Product.objects.order_by('-priority')

    product_paginator = Paginator(product_list, 10)

    print(product_paginator)

    product_list = product_paginator.get_page(page)

    return render(request, 'products.html', {'stars': range(5), 'rating': 3, 'products': product_list})


def product_detail_view(request, pk):


    product = Product.objects.get(pk=pk)

    return render(request, 'product_detail.html', {'product': product})
