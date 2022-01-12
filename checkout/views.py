from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm, DeliveryForm


def checkout(request):
    basket = request.session.get('basket')
    if not basket:
        messages.error(request, "You need to add something to checkout!")
        return redirect(reverse('shop'))
    order_form = OrderForm()
    delivery_form = DeliveryForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'delivery_form': delivery_form,
        'stripe_public_key': 'pk_test_51Jv5j8DCCRtNzyqm2EPWyMDp92MInKO01GEQ95avUQVOd9NEFeCrSricKfuDRtYp6pkN3Bnq1nV0BB8TOMCBBLYb00RJk49n28',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
