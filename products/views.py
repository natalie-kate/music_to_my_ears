from django.shortcuts import render
from .models import Vinyl, Genre, Image


def open_shop(request):
    """ A view to return the shopping page """
    products = Vinyl.objects.all()
    genres = Genre.objects.all()
    
    current_genres = []

    for genre in genres:
        filtered_products = Vinyl.objects.filter(genre= genre.pk)
        if filtered_products:
            current_genres.append(genre)

    images = Image.objects.all()
    context = {
        'products': products,
        'genres': current_genres,
        'images': images,
    }
    
    return render(request, 'products/shop.html', context)

