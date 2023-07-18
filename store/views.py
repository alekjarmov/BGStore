from django.shortcuts import render, redirect
from store import models
from authenticate.views import create_cart
# Create your views here.
from django.http import HttpResponse, JsonResponse


def home(request):
    context = dict()
    # get the 6 most sold products

    top_sellers = models.Product.objects.order_by('-copies_sold')[:8]
    context['active'] = 'home'
    context['top_sellers'] = top_sellers
    return render(request, "store/home.html", context)


def product(request, product_id):
    context = dict()
    context['active'] = 'product'
    context['product'] = models.Product.objects.get(id=product_id)
    return render(request, "store/product.html", context)


def products(request):
    context = dict()
    context['active'] = 'products'
    context['games'] = models.Product.objects.all()
    return render(request, "store/products.html", context)


def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart: models.Cart = models.Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = create_cart(request.user)

    context = dict()
    context['games'] = cart.games.all()
    context['total'] = cart.total


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    cart: models.Cart = models.Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = create_cart(request.user)

    models.CartItem.objects.create(cart=cart, product=models.Product.objects.get(id=product_id))

    return JsonResponse({'success': True})


def buy(request, product_id):
    context = dict()
    context['game'] = models.Product.objects.get(id=product_id)
    return render(request, "store/buy.html", context)


def payment(request, product_id):
    context = dict()
    context['game'] = models.Product.objects.get(id=product_id)
    return render(request, "store/payment.html", context)
