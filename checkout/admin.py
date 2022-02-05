""" Imports required for admin in checkout app """
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Outlining what we want to be able to edit in admin console for
    the line items of an order """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Outlining ordering of information and what we want to be able
    to edit in admin console for orders """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('user_profile', 'order_number', 'order_date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'basket',
                       'stripe_pid')

    fields = ('user_profile', 'order_date', 'order_number', 'first_name',
              'surname', 'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 'country',
              'postcode', 'delivery_street_address1',
              'delivery_street_address2', 'delivery_town_or_city',
              'delivery_county', 'delivery_country',
              'delivery_postcode', 'order_total', 'delivery_cost',
              'grand_total', 'basket', 'stripe_pid')

    list_display = ('order_number', 'order_date', 'surname',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
