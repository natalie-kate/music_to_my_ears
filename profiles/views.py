from django.shortcuts import render, get_object_or_404
from .models import UserProfile, SavedAddress
from checkout.models import Order


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    addresses = SavedAddress.objects.filter(user=profile)
    orders = Order.objects.filter(user_profile=profile)
    context = {
        'profile': profile,
        'addresses': addresses,
        'orders': orders
    }
    template = 'profiles/profile.html'
    return render(request, template, context)
