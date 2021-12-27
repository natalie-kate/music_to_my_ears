from products.models import Vinyl,Images

def basket_contents(request):

    basket_products = []
    bag = request.session.get('basket', {})

    context = {
        'products' = basket_products
    }

    return context
