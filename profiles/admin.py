from django.contrib import admin
from .models import SavedAddress

class SavedAddressAdmin(admin.ModelAdmin):
    """Change display in admin panel to see important information """
    list_display = (
        'user',
        'saved_street_address1',
    )
    ordering = ('user',)

admin.site.register(SavedAddress, SavedAddressAdmin)
