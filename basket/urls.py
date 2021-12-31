""" Imports required basket app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.view_basket, name='basket'),
    path('add/<product_id>/', views.add_to_basket, name='add_to_basket'),
]
