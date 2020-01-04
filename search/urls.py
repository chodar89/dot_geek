from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('navbar_brand/<int:brand_id>', views.navbar_brand, name='navbar_brand'),
    path('navbar_type/<int:type_id>', views.navbar_type, name='navbar_type'),
    path('carousel_search/<int:carousel_id>', views.carousel_search, name='carousel_search'),
]