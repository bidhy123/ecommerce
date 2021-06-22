from django.shortcuts import render
from home.models import Product


def product(request):
    product1 = Product.objects.all()
    for x in product1:
        if x.awesome is True:
            return render(request, "product.html", {'product1': x})
