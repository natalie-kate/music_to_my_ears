from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = ('user', 'email_date')
        widgets = {
            'rate_us': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
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
