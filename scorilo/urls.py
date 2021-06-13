from django.urls import path

from . import views

urlpatterns = [
    path("home", views.index, name="home"),
    path("shop", views.shop, name="shop"),
    path("product", views.product, name="product"),
    path("checkout", views.checkout, name="checkout"),
    path("contact", views.contact, name="contact"),
]
