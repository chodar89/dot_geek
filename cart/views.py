from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from products.models import Product
from .models import Cart, CartItem
from django.contrib.auth.models import User


def _get_user_or_none(request):
    if request.user.is_authenticated:
        user_id_or_none = request.user.id
    else:
        user_id_or_none = None
    return user_id_or_none


def _cart_id(request):
    # Get cart session if not create one
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        request.session.create()
        request.session['cart_id'] = request.session.session_key
        cart_id = request.session['cart_id']
        print('New Cart Id')
    return cart_id


def add_to_cart(request, product_id):
    """
    Add product to cart view
    """
    product = Product.objects.get(id=product_id)
    user_id = _get_user_or_none(request)
    session_cart_id = _cart_id(request)
    print("user +")
    print(user_id)
    try:
        # Check if cart already exists in database
        if user_id:
            cart = Cart.objects.get(user=user_id)
            # CartItem.objects.filter(cart__cart_id=session_cart_id).update(cart=cart.id)
        else:
            cart = Cart.objects.get(cart_id=session_cart_id)
    except Cart.DoesNotExist:
        # Insert data to DB
        if user_id:
            cart = Cart.objects.create(
                cart_id=session_cart_id,
                user=User(id=user_id)
                )
        else:
            cart = Cart.objects.create(
                cart_id=session_cart_id,
                )
        cart.save()
    try:
        # Try to check if item is in cart and rise quantity
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        # Insert item to DB
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart_details')

def cart_details(request, total=0, counter=0, cart_items=None):
    """
    Check all items in cart, count qnty and total price and render cart page
    """
    user_id = _get_user_or_none(request)
    session_cart_id = _cart_id(request)
    try:
        if user_id:
            cart = Cart.objects.get(user=user_id)
        else:
            cart = Cart.objects.get(cart_id=session_cart_id)
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            counter += item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart/cart.html', dict(cart_items=cart_items, total=total, counter=counter))
