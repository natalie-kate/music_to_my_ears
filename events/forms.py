""" Imports required for forms """
from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """ Create EventForm class """
    class Meta:
        """ Fields to render from model """
        model = Event
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and required attribute,
        set autofocus on first field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'e.g Open Mic Night',
            'date': 'e.g 25th June 2022',
            'time': 'e.g 19:30',
            'location': "e.g Red Lion, Main St, Prestwick, Ayrshire",
            'details': "e.g Open Mic night, all welcome"
            " we have everything bar your talent.",
            'ticket_price': "e.g 22.00 or 0 if free"
        }
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                if self.fields[field].required:
                    placeholder = placeholders[field]
                    self.fields[field].widget.attrs['required'] = True
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
