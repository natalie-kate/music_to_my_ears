from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name', 'surname', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'county', 'country', 'postcode',
            )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and required attribute, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Josephine',
            'surname': 'Smith',
            'email': 'js@example.com',
            'phone_number': '01234 56789',
            'street_address1': '33 Buchanan Street',
            'street_address2': 'Flat 2B',
            'county': 'Renfrewshire',
            'town_or_city': 'Glasgow',
            'postcode': 'G13 6LA',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = placeholders[field]
                    self.fields[field].widget.attrs['required'] = True
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'delivery_street_address1', 'delivery_street_address2',
            'delivery_town_or_city', 'delivery_county', 'delivery_country',
            'delivery_postcode',
            )
