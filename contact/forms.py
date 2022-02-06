""" Imports required for forms """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Create ContactForm class """
    class Meta:
        """ Fields to render from model """
        model = Contact
        exclude = ('user', 'email_date')
        widgets = {
            'rate_us': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and required attribute,
        set autofocus on first field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Josephine',
            'surname': 'Smith',
            'email': 'jsmith@example.com',
            'order_number': "You'll find this in your confirmation email ",
            'query': "Any comments or questions you may have",
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rate_us':
                if self.fields[field].required:
                    placeholder = placeholders[field]
                    self.fields[field].widget.attrs['required'] = True
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
