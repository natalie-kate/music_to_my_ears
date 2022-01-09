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
        'delivery_form': delivery_form
    }
    return render(request, template, context)
