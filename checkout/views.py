from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
import stripe
from basket.contexts import basket_contents
from .forms import OrderForm, DeliveryForm
from .models import Order, OrderLineItem


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get('basket', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        delivery_data = {
            'delivery_street_address1': request.POST['delivery_street_address1'],
            'delivery_street_address2': request.POST['delivery_street_address2'],
            'delivery_town_or_city': request.POST['delivery_town_or_city'],
            'delivery_county': request.POST['delivery_county'],
            'delivery_country': request.POST['delvery_country'],
            'delivery_postcode': request.POST['delivery_postcode'],
        }
        order_form = OrderForm(form_data, delivery_data)

    else:
        basket = request.session.get('basket')
        if not basket:
            messages.error(request, "You need to add something to checkout!")
            return redirect(reverse('shop'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
        delivery_form = DeliveryForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'delivery_form': delivery_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)
