""" Imports and views required for home app."""
from django.shortcuts import render


def error_404(request, exception):
    """ Render 404.html template """
    return render(request, '404.html', status=404)


def error_500(request):
    """ Render 500.html template """
    return render(request, '500.html', status=500)
