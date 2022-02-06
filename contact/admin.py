""" Imports required by admin """
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Outine what fields we want admin to see """
    list_display = ('email_date', 'query', 'order_number', 'user', 'rate_us')
    ordering = ('-email_date', 'user',)


admin.site.register(Contact, ContactAdmin)
