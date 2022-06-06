# Generated by Django 4.0.4 on 2022-05-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_inventory_on_hand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory_on_hand',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='inventory_received',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='inventory_shipped',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='minimum_required',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
