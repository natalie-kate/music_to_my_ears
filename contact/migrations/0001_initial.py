# Generated by Django 3.2.8 on 2022-01-26 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=254)),
                ('surname', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('order_number', models.CharField(blank=True, max_length=254, null=True)),
                ('query', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
