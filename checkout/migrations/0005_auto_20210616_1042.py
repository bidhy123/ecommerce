# Generated by Django 3.2.4 on 2021-06-16 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_checkout'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Checkout',
            new_name='Purchase',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='customerFirstEmail',
            new_name='customerEmail',
        ),
    ]
