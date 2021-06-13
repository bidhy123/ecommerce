from django.shortcuts import render
from .models import Shop


def shop(request):
    shop1 = Shop.objects.all()
    return render(request, "index.html", {'shop': shop1})
