""" Imports required for models """
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """ Creates Event table in database """
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True)
    name = models.CharField(max_length=254, null=False, blank=False)
    date = models.CharField(max_length=254, null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField(null=False, blank=False)
    location = models.TextField(null=False, blank=False)

    def __str__(self):
        """ Overwrites default str method """
        return 'self.name'
