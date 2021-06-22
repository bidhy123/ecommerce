from django.db import models


class Contact(models.Model):
    Name = models.CharField(max_length=250)
    Email_address = models.EmailField(max_length=250)
    Message = models.TextField(max_length=250)

    def __str__(self):
        return self.Name
