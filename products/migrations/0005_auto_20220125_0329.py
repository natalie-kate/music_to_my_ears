# Generated by Django 3.2.8 on 2022-01-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_image_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinyl',
            name='release_year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='vinyl',
            name='track_list',
            field=models.TextField(),
        ),
    ]
