""" Imports required by products app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Vinyl, Genre, Image


def open_shop(request):
    """ A view to return the shopping page """

    products = Vinyl.objects.all()
    genres = Genre.objects.all()
    images = Image.objects.filter(default=True)
    current_genres = []
    search = None

    if request.GET:
        if 'search' in request.GET:
            search = request.GET['search']
            searches = Q(title__icontains=search) | Q(
                artist__icontains=search) | Q(track_list__icontains=search)
            products = products.filter(searches)
            if not products:
                messages.error(
                    request, (
                        "Sorry your query didn't match any of our products"))
                return redirect(reverse('shop'))

        if not search:
            messages.error(
                request, "Oops you need to enter a search keyword first")
            return redirect(reverse('shop'))

    for genre in genres:
        filtered_products = Vinyl.objects.filter(genre=genre.pk)
        if filtered_products:
            current_genres.append(genre)

    context = {
        'products': products,
        'genres': current_genres,
        'images': images,
        'search': search,
    }

    return render(request, 'products/shop.html', context)


def product(request, product_id):
    """ Get product details """
    quantity_in_basket = 0
    product_info = get_object_or_404(Vinyl, pk=product_id)
    images = Image.objects.filter(vinyl=product_id)
    tracklist = product_info.track_list.split(",")
    basket = request.session.get('basket', {})
    basket_product = product_id in list(basket.keys())
    if basket_product:
        quantity_in_basket = basket[product_id]

    context = {
        'product': product_info,
        'images': images,
        'tracklist': tracklist,
        'basket_product': basket_product,
        'quantity': quantity_in_basket,
    }

    return render(request, 'products/product.html', context)
