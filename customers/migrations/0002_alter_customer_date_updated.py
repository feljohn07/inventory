# Generated by Django 4.0.4 on 2022-06-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_updated',
            field=models.DateTimeField(),
        ),
    ]
