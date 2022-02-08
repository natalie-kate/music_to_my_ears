""" Imports for profile app models"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ Creates UserProfile table in database"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=20, null=True, blank=True)
    default_surname = models.CharField(max_length=20, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return "self.user.username"

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """ When user created, create profile """
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()


class SavedAddress(models.Model):
    """ Creates SavedAddress table in database """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    saved_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    saved_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    saved_county = models.CharField(max_length=80, null=True, blank=True)
    saved_country = CountryField(blank_label='Country', null=True, blank=True)
    saved_postcode = models.CharField(max_length=20, null=True, blank=True)
