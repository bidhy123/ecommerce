# Generated by Django 3.2.4 on 2021-06-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productPrice', models.FloatField()),
                ('productName', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
