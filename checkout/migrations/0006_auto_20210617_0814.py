# Generated by Django 3.2.4 on 2021-06-17 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20210616_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='purchasedItemName',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchasedItemPrice',
        ),
    ]
