""" Imports for products app models"""
from django.db import models


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
    release_year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


class Image(models.Model):
    """ Creates Image table in database """
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
    image = models.ImageField()
    default = models.BooleanField(default=False)
