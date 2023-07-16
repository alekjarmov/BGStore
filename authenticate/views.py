from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import SignUpForm, LoginForm
from store import models


def register_view(request: HttpRequest):
    context = dict()
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data["password2"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect("login")
        else:
            return render(request, "authenticate/register.html", {"form": form})

    context["form"] = SignUpForm()
    return render(request, "authenticate/register.html", context)


def login_view(request):
    context = dict()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            cart = models.Cart.objects.filter(user=user).first()
            if not cart:
                cart = create_cart(user)

            return redirect('home')
        else:
            return render(request, 'authenticate/login.html', {'form': form})

    form = LoginForm()
    context['form'] = form
    return render(request, 'authenticate/login.html', context)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/')

    logout(request)
    return redirect('home')


def create_cart(user: User):
    cart = models.Cart.objects.create(user=user)
    cart.save()
    return cart
