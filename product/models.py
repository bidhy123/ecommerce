from django.db import models


class Product(models.Model):
    productPrice = models.FloatField()
    productName = models.CharField(max_length=250)
    productDescription = models.TextField()
    img = models.ImageField(upload_to="pics")
