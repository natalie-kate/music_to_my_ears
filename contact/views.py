from django.shortcuts import render

def contact(request):
    """ A view to return the contact page """
    return render(request, 'contact/contact.html')
