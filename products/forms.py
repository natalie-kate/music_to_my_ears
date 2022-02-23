""" Imports required for forms """
from django import forms
from .models import Vinyl, Genre
from .validators import validate_tracklist


class ProductForm(forms.ModelForm):
    """ Create ProductForm class """
    class Meta:
        """ Fields to render from model """
        model = Vinyl
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """ Add placeholders and required attribute,
        set autofocus on first field """
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        for field in self.fields:
            if field != 'genre':
                if self.fields[field].required:
                    self.fields[field].widget.attrs['required'] = True
        friendly_names = [(g.id, g.get_friendly_name()) for g in genres]
        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['description'].widget.attrs['placeholder'] = (
            'e.g 2nd studio album')
        self.fields['track_list'].widget.attrs['placeholder'] = (
            'Add in tracklist e.g 1. Track Title, '
            'separating titles with a comma!')
        self.fields['track_list'].validators.append(validate_tracklist)
        self.fields['genre'].choices = friendly_names
