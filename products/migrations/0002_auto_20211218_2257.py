# Generated by Django 3.2.8 on 2021-12-18 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vinyl',
            name='description',
        ),
        migrations.RemoveField(
            model_name='vinyl',
            name='stock_quantity',
        ),
        migrations.RemoveField(
            model_name='vinyl',
            name='track_list',
        ),
    ]
