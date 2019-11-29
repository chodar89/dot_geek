from django.urls import path

from . import views

urlpattern = [
    path('search', views.search, name='search'),
]