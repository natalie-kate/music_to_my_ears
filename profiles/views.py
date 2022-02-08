""" Imports required by products app """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order
from .models import UserProfile, SavedAddress
from .forms import UserProfileForm, SavedAddressForm


@login_required
def profile(request):
    """ Render profile template"""
    user_profile = get_object_or_404(UserProfile, user=request.user)
    addresses = SavedAddress.objects.filter(user=request.user)
    orders = Order.objects.filter(user_profile=user_profile)

    if request.method == 'POST':
        # If post method update users default information
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            try:
                # Check if address is already in database
                address = SavedAddress.objects.get(
                    saved_street_address1__iexact=(
                        user_profile.default_street_address1),
                    user=request.user,
                )
                save_address = True
            except SavedAddress.DoesNotExist:
                # If address doesn't exist get info from form
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
                # Save address to database
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


@login_required
def order_history(request, order_number):
    """ Get users order and open with checkout-success template """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)


@login_required
def delete_user(request, user_id):
    """ Delete account """
    user = request.user.id
    if not request.user.id == user:
        messages.error(request, "Sorry, you can't do that.")
        return redirect(reverse('account_login'))
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.success(request, 'Account deleted!')
    return redirect(reverse('shop'))
