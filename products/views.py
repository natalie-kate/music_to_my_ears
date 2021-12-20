from django.shortcuts import render
from .models import Vinyl, Genre, Image


def open_shop(request):
    """ A view to return the shopping page """
    products = Vinyl.objects.all()
    genres = Genre.objects.all()

    images = Image.objects.all()
    context = {
        'products': products,
        'genres': genres,
        'images': images,
    }
    
    return render(request, 'products/shop.html', context)

