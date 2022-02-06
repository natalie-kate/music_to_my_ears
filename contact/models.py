""" Imports required for models """
from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """ Creates Contact table in database """
    CHOICES = (
        ('1', '1',),
        ('2', '2',),
        ('3', '3',),
        ('4', '4',),
        ('5', '5',),
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True)
    email_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=254, null=False, blank=False)
    surname = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    order_number = models.CharField(max_length=254, null=True, blank=True)
    query = models.TextField(null=True, blank=True)
    rate_us = models.CharField(
        choices=CHOICES, max_length=6, null=True, blank=True)
