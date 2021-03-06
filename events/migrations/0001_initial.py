# Generated by Django 3.2.8 on 2022-01-27 22:35

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
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('date', models.CharField(max_length=254)),
                ('time', models.TimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('details', models.TextField()),
                ('location', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
