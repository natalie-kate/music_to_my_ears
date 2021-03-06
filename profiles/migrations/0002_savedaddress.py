# Generated by Django 3.2.8 on 2022-01-20 22:18

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('saved_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('saved_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('saved_county', models.CharField(blank=True, max_length=80, null=True)),
                ('saved_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('saved_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]
