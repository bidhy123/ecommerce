from django.db import models

# Create your models here.


class Shop(models.Model):
    productPrice = models.FloatField()
    productName = models.CharField(max_length=250)
    img = models.ImageField(upload_to="pics")
