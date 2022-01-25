from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.open_shop, name='shop'),
    path('<int:product_id>/', views.product, name='product'),
    path('add/', views.add_vinyl, name='add_vinyl'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
