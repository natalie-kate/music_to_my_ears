from django.shortcuts import render


def basket(request):
    """ A view to return the shopping basket page """
    return render(request, 'basket/basket.html')
