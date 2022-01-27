from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from profiles.models import UserProfile
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        form_data = {
            'first_name': request.POST['first_name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'order_number': request.POST['order_number'],
            'query': request.POST['query'],
            'rate_us': request.POST['rate_us']
        }
        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            user_contact = contact_form.save(commit=False)
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user)
                user_contact.user = user
            user_contact.save()
            messages.success(request, "That's sent, check your email for confirmation")
            return redirect(reverse('shop'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'first_name': profile.default_first_name,
                    'surname': profile.default_surname,
                    'email': profile.default_email,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
        template = 'contact/contact.html'
        context = {
            'contact_form': contact_form
        }
        return render(request, template, context)
