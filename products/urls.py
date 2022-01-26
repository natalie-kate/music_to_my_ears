from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.open_shop, name='shop'),
    path('all/', views.view_all_products, name='view_all_products'),
    path('<int:product_id>/', views.product, name='product'),
    path('add/', views.add_vinyl, name='add_vinyl'),
    path('edit/<int:product_id>/', views.edit_vinyl, name='edit_vinyl'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
