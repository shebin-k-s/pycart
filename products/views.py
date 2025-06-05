from django.shortcuts import render

# Create your views here.


def home_view(request):

    return render(request, 'index.html')


def products_view(request):
    return render(request, 'products.html', {'stars': range(5), 'rating': 3,'products':range(20)})


def product_detail_view(request):
    return render(request, 'product_detail.html')
