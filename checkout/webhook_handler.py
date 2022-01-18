import time
import json
from django.http import HttpResponse
from products.models import Vinyl
from .models import Order, OrderLineItem


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.payment_succeeded webhook from Stripe """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket

        billing_details = intent.charges.data[0].billing_details
        delivery_details = intent.shipping

        order_exists = None
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(stripe_pid=pid)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received:{event["type"]},'
                "SUCCESS: Verified order already in database",
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=billing_details.name.split(" ")[0],
                    surname=billing_details.name.split(" ")[1],
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    town_or_city=billing_details.address.city,
                    county=billing_details.address.state,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    delivery_street_address1=delivery_details.address.line1,
                    delivery_street_address2=delivery_details.address.line2,
                    delivery_town_or_city=delivery_details.address.city,
                    delivery_county=delivery_details.address.state,
                    delivery_country=delivery_details.address.country,
                    delivery_postcode=delivery_details.address.postal_code,
                    basket=basket,
                    stripe_pid=pid,
                )
                for item_id, quantity in json.loads(basket).items():
                    product = Vinyl.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

            except Exception as error:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]}, '
                    f'ERROR: {error}', status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}, '
            "SUCCESS: Created order in webhook", status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
