from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import SignUpForm, LoginForm


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
            return redirect("home")
        else:
            return render(request, "authenticate/register.html", {"form": form})

    context["form"] = SignUpForm()
    return render(request, "authenticate/register.html", context)


def login_view(request):
    pass