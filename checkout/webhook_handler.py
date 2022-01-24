import time
import json
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from products.models import Vinyl
from .models import Order, OrderLineItem
from profiles.models import UserProfile, SavedAddress
from profiles.forms import UserProfileForm, SavedAddressForm


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

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
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        delivery_details = intent.shipping

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile_data = {
                    'default_first_name': billing_details.name.split(" ")[0],
                    'default_surname': billing_details.name.split(" ")[1],
                    'default_email': billing_details.email,
                    'default_phone_number': billing_details.phone,
                    'default_street_address1': billing_details.address.line1,
                    'default_street_address2': billing_details.address.line2,
                    'default_town_or_city': billing_details.address.city,
                    'default_county': billing_details.address.state,
                    'default_country': billing_details.address.country,
                    'default_postcode': billing_details.address.postal_code,
                }
                save_address_data = {
                    'saved_street_address1': delivery_details.address.line1,
                    'saved_street_address2': delivery_details.address.line2,
                    'saved_town_or_city': delivery_details.address.city,
                    'saved_county': delivery_details.address.state,
                    'saved_country': delivery_details.address.country,
                    'saved_postcode': delivery_details.address.postal_code,
                }
                user_profile_form = UserProfileForm(
                    profile_data, instance=profile)

                if user_profile_form.is_valid():
                    user_profile_form.save()
                    try:
                        address = SavedAddress.objects.get(
                            saved_street_address1__iexact=order.street_address1,
                            user=request.user,
                        )
                        save_address = True
                    except SavedAddress.DoesNotExist:
                        save_profile_address = {
                            'saved_street_address1': billing_details.address.line1,
                            'saved_street_address2': billing_details.address.line2,
                            'saved_town_or_city': billing_details.address.city,
                            'saved_county': billing_details.address.state,
                            'saved_country': billing_details.address.country,
                            'saved_postcode': billing_details.address.postal_code,
                        }
                        save_address_form = SavedAddressForm(save_profile_address)
                        save_address = False
                    if not save_address:
                        address = save_address_form.save(commit=False)
                        address.user = request.user
                        address.save()

            save_address_form = SavedAddressForm(save_address_data)
            if save_address_form.is_valid():
                try:
                    address = SavedAddress.objects.get(
                        saved_street_address1__iexact=order.delivery_street_address1,
                        user=request.user,
                    )
                    save_address = True
                except SavedAddress.DoesNotExist:
                    save_address = False
                if not save_address:
                    address = save_address_form.save(commit=False)
                    address.user = request.user
                    address.save()

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
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received:{event["type"]},'
                "SUCCESS: Verified order already in database",
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    user_profile=profile,
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
                    
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}, '
            "SUCCESS: Created order in webhook", status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
