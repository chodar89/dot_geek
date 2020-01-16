from django.urls import path, include

from . import views

urlpatterns = [
    path('reset', include('django.contrib.auth.urls')),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
