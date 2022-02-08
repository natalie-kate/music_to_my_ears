""" Imports required for forms """
from django import forms
from .models import UserProfile, SavedAddress


class UserProfileForm(forms.ModelForm):
    """ Create UserProfileForm """
    class Meta:
        """ Fields to render from model """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_first_name': 'Joe',
            'default_surname': 'Smith',
            'default_email': 'j.smith@test.com',
            'default_phone_number': '01234 56789',
            'default_street_address1': '33 Buchanan Street',
            'default_street_address2': 'Flat 2B',
            'default_county': 'Renfrewshire',
            'default_town_or_city': 'Glasgow',
            'default_postcode': 'G13 6LA',
        }

        for field in self.fields:
            if field != 'default_country':
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder


class SavedAddressForm(forms.ModelForm):
    """ Create SavedAddresseForm """
    class Meta:
        """ Fields to render from model """
        model = SavedAddress
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders """
        super().__init__(*args, **kwargs)
        placeholders = {
            'saved_street_address1': '33 Buchanan Street',
            'saved_street_address2': 'Flat 2B',
            'saved_county': 'Renfrewshire',
            'saved_town_or_city': 'Glasgow',
            'saved_postcode': 'G13 6LA',
        }
        for field in self.fields:
            if field != 'saved_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
