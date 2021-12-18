""" Register Product models with admin so that it appears in admin dashboard"""
from django.contrib import admin
from .models import Vinyl, Genre, Image

admin.site.register(Genre)
admin.site.register(Vinyl)
admin.site.register(Image)
