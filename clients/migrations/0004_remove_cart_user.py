# Generated by Django 5.0.6 on 2024-06-18 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]