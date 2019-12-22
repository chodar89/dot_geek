from django.urls import path

from . import views

urlpatterns = [
    path('order/<int:order_id>', views.order, name='order'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
