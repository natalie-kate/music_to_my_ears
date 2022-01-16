import json
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
from basket.contexts import basket_contents
from products.models import Vinyl
from .forms import OrderForm, DeliveryForm
from .models import Order, OrderLineItem

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

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
            'delivery_street_address1':
            request.POST['delivery_street_address1'],
            'delivery_street_address2':
            request.POST['delivery_street_address2'],
            'delivery_town_or_city': request.POST['delivery_town_or_city'],
            'delivery_county': request.POST['delivery_county'],
            'delivery_country': request.POST['delivery_country'],
            'delivery_postcode': request.POST['delivery_postcode'],
        }

        order_form = OrderForm(form_data)
        delivery_form = DeliveryForm(delivery_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.basket = json.dumps(basket)
            if delivery_data:
                order.delivery_street_address1 = request.POST['delivery_street_address1']
                order.delivery_street_address2 = request.POST['delivery_street_address2']
                order.delivery_town_or_city = request.POST['delivery_town_or_city']
                order.delivery_county = request.POST['delivery_county']
                order.delivery_country = request.POST['delivery_country']
                order.delivery_postcode = request.POST['delivery_postcode']
            else:
                order.delivery_street_address1 = request.POST['street_address1']
                order.delivery_street_address2 = request.POST['street_address2']
                order.delivery_town_or_city = request.POST['town_or_city']
                order.delivery_county = request.POST['county']
                order.delivery_country = request.POST['country']
                order.delivery_postcode = request.POST['postcode']
            order.save()
            for item_id, quantity in basket.items():
                try:
                    product = Vinyl.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

                except Vinyl.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't"
                        " found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
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


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, "Thanks for your order!")
    if 'basket' in request.session:
        del request.session['basket']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }
    return render(request, template, context)
