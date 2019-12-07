from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart, CartItem
from django.contrib.auth.models import User



def _cart_id(request):
    # Get cart session if not create one
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    print('test')
    return cart


def add_to_cart(request, product_id):
    """
    Add product to cart view
    """
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            user_id = None
        cart = Cart.objects.create(
            cart_id=_cart_id(request),
            user=user_id.id
            )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('car:car_details')

def cart_details(request):
    return