""" Imports for products app models"""
from django.db import models
from .validators import validate_tracklist


class Genre(models.Model):
    """ Creates Genre table in database"""
    genre = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.genre

    def get_friendly_name(self):
        """ Returns a user friendly name for display purposes """
        return self.friendly_name


class Vinyl(models.Model):
    """ Creates Vinyl table in database """
    title = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_year = models.CharField(max_length=4, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    stock_quantity = models.IntegerField(default=1)
    track_list = models.TextField(validators=[validate_tracklist])

    def __str__(self):
        return self.title


class Image(models.Model):
    """ Creates Image table in database """
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
    image = models.ImageField()
    image_name = models.CharField(max_length=254, null=True, blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.image_name
