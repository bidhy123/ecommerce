from django.shortcuts import render
from home.models import Product


def shop(request):
    shop1 = Product.objects.all()
    print(shop1)
    return render(request, "shop.html", {'shop1': shop1})
