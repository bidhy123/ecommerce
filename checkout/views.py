
from checkout.models import Purchase
from django.shortcuts import render
from home.models import Product
from django.contrib import messages


def checkout(request):

    return render(request, "checkout.html")


def purchase(request, id):
    purchase1 = Product.objects.get(pk=id)
    print(id)
    purchase = Purchase()
    if request.method == "POST":
        purchase.customerFirstName = request.POST['firstname']
        purchase.customerLastName = request.POST['lastname']
        purchase.customerEmail = request.POST['email']
        purchase.productName = purchase1.productName
        purchase.productPrice = purchase1.productPrice

        purchase.save()
        messages.success(request, 'Thank You for Choosing Our Product.')
    return render(request, "checkout.html", {'purchase1': purchase1})
