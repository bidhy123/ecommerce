from django.db import models


class Purchase(models.Model):
    customerFirstName = models.CharField(max_length=100)
    customerLastName = models.CharField(max_length=100)
    customerEmail = models.EmailField()
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()

    def __str__(self):
        return self.customerFirstName
