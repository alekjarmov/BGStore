from django.shortcuts import render
from .models import Product
# Create your views here.
from django.http import HttpResponse


def home(request):
    context = dict()
    # get the 6 most sold products

    top_sellers = Product.objects.order_by('-copies_sold')[:8]
    context['active'] = 'home'
    context['top_sellers'] = top_sellers
    return render(request, "store/home.html", context)


def product(request, product_id):
    context = dict()
    context['active'] = 'product'
    context['product'] = Product.objects.get(id=product_id)
    return render(request, "store/product.html", context)