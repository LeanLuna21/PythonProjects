# Generated by Django 4.2.7 on 2023-11-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='color',
        ),
        migrations.AddField(
            model_name='producto',
            name='color_luz',
            field=models.CharField(default='blue', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='color_sable',
            field=models.CharField(default='silver and black', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=100),
        ),
    ]
