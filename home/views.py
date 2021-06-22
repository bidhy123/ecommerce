from home.models import Product
from django.shortcuts import render


def index(request):
    home1 = Product.objects.all()
    value = home1[:3]
    print(value)
    return render(request, "index.html", {'home1': value})
