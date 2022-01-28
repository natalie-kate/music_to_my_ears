# Register Event so can view in admin panel
from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    """Change display in admin panel to see important information """
    list_display = (
        'name',
        'date',
        'location',
    )
    ordering = ('-date',)


admin.site.register(Event, EventAdmin)
