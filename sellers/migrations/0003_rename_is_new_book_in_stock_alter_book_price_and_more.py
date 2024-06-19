# Generated by Django 5.0.6 on 2024-06-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_alter_book_category_alter_book_genre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='is_new',
            new_name='in_stock',
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]