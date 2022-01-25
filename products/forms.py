from django import forms
from .models import Vinyl, Genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = Vinyl
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genres]
        self.fields['description'].widget.attrs['placeholder'] = (
            'e.g 2nd studio album')
        self.fields['track_list'].widget.attrs['placeholder'] = (
            'Add in tracklist e.g 1. Track Title, '
            'separating titles with a comma!')
        self.fields['genre'].choices = friendly_names
