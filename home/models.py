from django.db import models


class Product(models.Model):
    productName = models.CharField(max_length=250)
    productPrice = models.FloatField()
    productDescription = models.TextField()
    img = models.ImageField(upload_to="pics")
    awesome = models.BooleanField(default=False)
