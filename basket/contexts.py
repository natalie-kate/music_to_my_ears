""" Imports required for basket_contents """
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Vinyl


def basket_contents(request):
    """ Make basket contents and totals available to all templates """
    basket_products = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    delivery = 4.95

    for product_id, quantity in basket.items():
        product = get_object_or_404(Vinyl, pk=product_id)
        total += quantity * product.price
        item_total = quantity * product.price
        product_count += quantity
        product_images = product.image_set.all()
        basket_products.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'product_images': product_images,
            'item_total': item_total
        })

    grand_total = round((total + Decimal(delivery)), 2)

    context = {
        'basket_products': basket_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
