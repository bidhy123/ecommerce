from django.urls import path

from . import views

urlpatterns = [
    path("purchase/<int:id>", views.purchase, name="purchase"),
    path('checkout', views.checkout, name='checkout'),
]
