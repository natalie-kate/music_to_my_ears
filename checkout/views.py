from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
import stripe
from basket.contexts import basket_contents
from .forms import OrderForm, DeliveryForm


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
