""" Imports required basket app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.view_basket, name='view_basket'),
    path('add/<product_id>/', views.add_to_basket, name='add_to_basket'),
    path('edit/<product_id>/', views.edit_quantity, name='edit_quantity'),
    path('delete/<product_id>/', views.delete_item, name='delete_item'),
]
