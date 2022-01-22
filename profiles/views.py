from django.shortcuts import render, get_object_or_404
from .models import UserProfile, SavedAddress
from checkout.models import Order


def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    addresses = SavedAddress.objects.filter(user=request.user)
    orders = Order.objects.filter(user_profile=user_profile)
    context = {
        'profile': user_profile,
        'addresses': addresses,
        'orders': orders
    }
    template = 'profiles/profile.html'
    return render(request, template, context)
