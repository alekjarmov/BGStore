import random

from django.shortcuts import render, redirect
from store import models
from authenticate.views import create_cart
# Create your views here.
from django.http import HttpResponse, JsonResponse


def home(request):
    context = dict()
    # get the 6 most sold products
    top_sellers = models.Product.objects.order_by('-copies_sold')[:8]

    if request.GET.get('success'):
        context['success'] = True
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
    context['title'] = 'All Games'
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


def categories(request, category_id):
    id_name_map = dict()
    id_name_map[1] = '2 Player games'
    id_name_map[2] = 'Abstract Games'
    id_name_map[3] = 'Coop Games'
    context = dict()
    context['active'] = 'categories'
    # generate a random subset of games from all games
    all_games = models.Product.objects.all()
    if len(all_games) == 0:
        how_many = 0
    else:
        how_many = random.randint(1, len(all_games))
    random_games = random.sample(list(all_games), how_many)
    context['games'] = random_games
    context['title'] = id_name_map[category_id]
    return render(request, "store/products.html", context)
