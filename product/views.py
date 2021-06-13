
from django.shortcuts import render
from .models import Product


def product(request):
    product1 = Product.objects.all()
    return render(request, "index.html", {'product1': product1})
