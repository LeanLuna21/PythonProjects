# Generated by Django 4.2.7 on 2023-11-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='precio_total',
            field=models.FloatField(default=0),
        ),
    ]