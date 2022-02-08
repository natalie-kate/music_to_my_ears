""" Register Product models with admin so that it appears in admin dashboard"""
from django.contrib import admin
from .models import Genre, Vinyl, Image


class VinylAdmin(admin.ModelAdmin):
    """Change display in admin panel to see important information """
    list_display = (
        'artist',
        'title',
        'stock_quantity',
        'genre'
    )
    ordering = ('artist',)


class ImageAdmin(admin.ModelAdmin):
    """Change order in admin panel """
    list_display = ('image_name', 'image', 'vinyl')
    ordering = ('vinyl',)


class GenreAdmin(admin.ModelAdmin):
    """Change genre display in admin """
    list_display = ('friendly_name',)
    ordering = ('friendly_name',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Vinyl, VinylAdmin)
admin.site.register(Image, ImageAdmin)
