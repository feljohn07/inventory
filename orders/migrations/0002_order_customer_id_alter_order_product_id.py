# Generated by Django 4.0.4 on 2022-07-01 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('customers', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
