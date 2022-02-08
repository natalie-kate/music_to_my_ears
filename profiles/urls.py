""" Imports required for products app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('delete_user/<user_id>/', views.delete_user, name='delete_user'),
]
