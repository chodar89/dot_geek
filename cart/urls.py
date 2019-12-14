from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_details, name='cart_details'),
    path('remove/<int:item_id>/', views.remove_one_cart, name='remove_one_cart'),
    path('increase/<int:item_id>/', views.increase_one_cart, name='increase_one_cart'),
    path('delete/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
]
