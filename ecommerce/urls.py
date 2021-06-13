"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import checkout
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
# from django.conf.urls import *
from checkout import views as views3
from product import views as views2
from shop import views as views1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scorilo.urls')),
    path("checkout", views3.checkout, name="checkout"),
    path("product", views2.product, name="product"),
    path("shop", views1.shop, name="shop"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
