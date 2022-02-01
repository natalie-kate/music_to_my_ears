# Generated by Django 3.2.8 on 2022-02-01 21:58

from django.db import migrations, models
import products.validators


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220125_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinyl',
            name='track_list',
            field=models.TextField(validators=[products.validators.validate_tracklist]),
        ),
    ]
