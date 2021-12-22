from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.open_shop, name='shop'),
    path('<product_id>', views.product, name='product')
]
