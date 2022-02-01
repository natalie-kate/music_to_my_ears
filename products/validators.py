from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def validate_tracklist(value):
    """ Validate Tracklist field """
    if "," not in value:
        raise ValidationError(_(
            "Did you forget to add commas between your tracks?"),
             code='invalid')
