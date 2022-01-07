""" Imports required for basket app views """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Vinyl


def view_basket(request):
    """ A view to return the shopping basket page """
    context = {
        'is_basket': True
    }
    return render(request, 'basket/basket.html', context)


def add_to_basket(request, product_id):
    """ Add a product to the shopping basket """
    product = get_object_or_404(Vinyl, pk=product_id)
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    quantity = 1

    if product_id in list(basket.keys()):
        basket[product_id] += quantity
        messages.success(request, (
            f"Updated {product.title} quantity to {basket[product_id]}"))
    else:
        basket[product_id] = quantity
        messages.success(request, f"Added {product.title} to your bag!")

    request.session['basket'] = basket
    return redirect(redirect_url)


def edit_quantity(request, product_id):
    """ Edit quantity of basket product """
    if request.method == 'POST':
        product = get_object_or_404(Vinyl, pk=product_id)
        quantity = request.POST.get('quantity')
        basket = request.session.get('basket', {})
        basket[product_id] = int(quantity)
        messages.success(request, (
            f"That's { product.title } quantity updated to { quantity }"))
        request.session['basket'] = basket
        return redirect('view_basket')


def delete_item(request, product_id):
    """ Delete product from basket """
    product = get_object_or_404(Vinyl, pk=product_id)
    basket = request.session.get('basket', {})
    basket.pop(product_id)
    messages.success(request, (
            f"That's { product.title } removed from your basket."))
    request.session['basket'] = basket
    return redirect('view_basket')
