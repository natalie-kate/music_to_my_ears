""" Imports required for basket_contents """
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Vinyl


def basket_contents(request):
    """ Make basket contents and totals available to all templates """
    basket_products = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    basket_bin = []

    for product_id, quantity in basket.items():
        product = get_object_or_404(Vinyl, pk=product_id)
        if quantity <= product.stock_quantity:
            product_name = product.title.replace(" ", "_").lower
            total += Decimal(quantity) * product.price
            item_total = Decimal(quantity) * product.price
            product_count += int(quantity)
            product_images = product.image_set.all()
            stock_quantity_list = []
            for value in range(1, (product.stock_quantity + 1)):
                stock_quantity_list.append(value)
            basket_products.append({
                'product_id': product_id,
                'quantity': quantity,
                'product': product,
                'product_images': product_images,
                'item_total': item_total,
                'product_name': product_name,
                'stock_quantity_list': stock_quantity_list
            })
        else:
            messages.error(request, (
                f'Sorry { product.title} no longer has { quantity }'
                'left in stock.'))
            basket_bin.append(product_id)

    if basket_bin:
        for product_id in basket_bin:
            basket.pop(product_id)
            request.session['basket'] = basket

    delivery = 4.95 + ((product_count - 1)/2)
    grand_total = round((total + Decimal(delivery)), 2)

    context = {
        'basket_products': basket_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
