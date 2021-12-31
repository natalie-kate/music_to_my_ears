from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Vinyl, Image


def basket_contents(request):
    image = Image.objects.all()
    basket_products = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    delivery = 4.95

    for product_id, quantity in basket.items():
        product = get_object_or_404(Vinyl, pk=product_id)
        total += quantity * product.price
        product_count += quantity
        product_images = product.image_set.all()
        basket_products.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'product_images': product_images,
        })

    grand_total = Decimal(total + delivery)

    context = {
        'basket_products': basket_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
