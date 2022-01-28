from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Open Mic Night',
            'date': '25th June 2022',
            'time': '19:30',
            'location': "Red Lion, Main St, Prestwick, Ayrshire",
            'details': "Open Mic night, all welcome"
            "we have everything bar your talent.",
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
