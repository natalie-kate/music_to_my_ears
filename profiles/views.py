from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from checkout.models import Order
from .models import UserProfile, SavedAddress
from .forms import UserProfileForm, SavedAddressForm


def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    addresses = SavedAddress.objects.filter(user=request.user)
    orders = Order.objects.filter(user_profile=user_profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            try:
                address = SavedAddress.objects.get(
                    saved_street_address1__iexact=(
                        user_profile.default_street_address1),
                    user=request.user,
                )
                save_address = True
            except SavedAddress.DoesNotExist:
                save_address_data = {
                    'saved_street_address1': (
                        user_profile.default_street_address1),
                    'saved_street_address2': (
                        user_profile.default_street_address2),
                    'saved_town_or_city': user_profile.default_town_or_city,
                    'saved_county': user_profile.default_county,
                    'saved_country': user_profile.default_country,
                    'saved_postcode': user_profile.default_postcode,
                }
                save_address_form = SavedAddressForm(save_address_data)
                save_address = False
            if not save_address:
                address = save_address_form.save(commit=False)
                address.user = request.user
                address.save()
        messages.success(request, 'Profile updated successfully')

    profile_form = UserProfileForm(instance=user_profile)

    context = {
        'profile_form': profile_form,
        'profile': user_profile,
        'addresses': addresses,
        'orders': orders,
        'on_profile_page': True
    }
    template = 'profiles/profile.html'
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.success(request, 'Account deleted!')
    return redirect(reverse('shop'))
