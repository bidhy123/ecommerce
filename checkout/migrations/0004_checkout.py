# Generated by Django 3.2.4 on 2021-06-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0003_delete_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerFirstName', models.CharField(max_length=100)),
                ('customerLastName', models.CharField(max_length=100)),
                ('customerFirstEmail', models.EmailField(max_length=254)),
                ('purchasedItemName', models.CharField(max_length=255)),
                ('purchasedItemPrice', models.FloatField()),
            ],
        ),
    ]
