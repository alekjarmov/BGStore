from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context = dict()
    context['active'] = 'home'
    return render(request, "store/home.html", context)
