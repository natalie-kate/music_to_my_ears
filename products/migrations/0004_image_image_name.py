# Generated by Django 3.2.8 on 2021-12-19 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211218_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]