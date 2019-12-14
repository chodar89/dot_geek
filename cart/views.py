from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from products.models import Product, SizeChart
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

# def _check_clothing_stock(size, stock):
#     if size == 

def add_to_cart(request, product_id):
    """
    Add product to cart view
    """
    if request.method == 'POST':
        # Get item qnty and size from product card panel form
        get_item_qnty = int(request.POST.get('quantity'))
        get_item_size = request.POST.get('size')
        try:
            size = SizeChart.objects.get(id=get_item_size)
        except ObjectDoesNotExist:
            size = None
        product = Product.objects.get(id=product_id)
        user_id = _get_user_or_none(request)
        session_cart_id = _cart_id(request)
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
            cart_item = CartItem.objects.get(product=product, cart=cart, item_size=size)
            cart_item.quantity += get_item_qnty
            cart_item.save()
        except CartItem.DoesNotExist:
            # Insert item to DB
            cart_item = CartItem.objects.create(
                product=product,
                quantity=get_item_qnty,
                cart=cart,
                item_size=size
            )
            cart_item.save()
    return redirect('cart_details')

def cart_details(request):
    """
    View that render cart page
    """
    return render(request, 'cart/cart.html')
