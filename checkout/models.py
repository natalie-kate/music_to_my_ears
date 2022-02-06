""" Imports required for checkout app models """
import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField
from products.models import Vinyl
from profiles.models import UserProfile


class Order(models.Model):
    """ General order information """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    delivery_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    delivery_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    delivery_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    delivery_county = models.CharField(
        max_length=50, null=True, blank=True)
    delivery_country = CountryField(null=True, blank=True)
    delivery_postcode = models.CharField(max_length=20, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Generate an order number using UUID """
        order_number = uuid.uuid4().hex.upper()
        return order_number

    def save(self, *args, **kwargs):
        """ Override the save method to ensure an order number
        is generated """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        """ Update grand total each time a line item is added """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        number_of_products = self.lineitems.aggregate(
            Sum('quantity'))['quantity__sum'] or 0
        self.delivery_cost = Decimal(4.95 + ((number_of_products - 1)/2))
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def __str__(self):
        """ Override the default str. """
        return self.order_number


class OrderLineItem(models.Model):
    """ Individual product details in order """
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Vinyl, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """ Override the save method to set the lineitem total
        and update the order total. """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """ Override the default str. """
        return f'{self.product.title} on order {self.order.order_number}'
