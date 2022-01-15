""" Imports required basket app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', 
         views.checkout_success, name='checkout_success'),
]
