""" Imports required for signals.py in checkout app """
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Will update order total if line item edited or added by admin """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ Will update order total if line item deleted by admin """
    instance.order.update_total()
