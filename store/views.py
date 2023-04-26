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
    context['test'] = [1, 2, 3]
    print(context)
    return render(request, "store/home.html", context)
