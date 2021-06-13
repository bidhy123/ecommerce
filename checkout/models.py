from django.db import models


class Checkout(models.Model):
    email_address = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
