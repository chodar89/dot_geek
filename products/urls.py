from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:product_id>', views.product, name='product'),
    path('search', views.search, name='search')
]
