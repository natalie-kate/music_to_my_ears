from django.shortcuts import render
from .forms import ContactForm
from profiles.models import UserProfile

def contact(request):
    """ A view to return the contact page """
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
