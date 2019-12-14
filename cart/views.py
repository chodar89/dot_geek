from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib import messages

from products.models import Product, SizeChart
from .models import Cart, CartItem
from django.contrib.auth.models import User


import stripe
from django.conf import settings

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


def cart_details(request, total=0, counter=0, cart_items=None):
    """
    Render cart page
    Check all items in cart, count qnty and total price 
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
            if item.item_size:
                size = item.item_size.size
                qnty = item.quantity
                stock_xs = item.product.stock_xs
                stock_s = item.product.stock_s
                stock_m = item.product.stock_m
                stock_l = item.product.stock_l
                stock_xl = item.product.stock_xl
                stock_xxl = item.product.stock_xxl
                stock_xxxl = item.product.stock_xxxl
                if size == 'XS':
                    if qnty > stock_xs:
                        qnty = stock_xs
                        item.save()
                        messages.error(request, f'We have only {stock_xs} {item.product.name} in stock. Sorry.')
                if size == 'S':
                    if qnty > stock_s:
                        qnty = stock_s
                        item.save()
                        messages.error(request, f'We have only {stock_s} {item.product.name} in stock. Sorry.')
                if size == 'M':
                    if qnty > stock_m:
                        qnty = stock_m
                        item.save()
                        messages.error(request, f'We have only {stock_m} {item.product.name} in stock. Sorry.')
                if size == 'L':
                    if qnty > stock_l:
                        qnty = stock_l
                        item.save()
                        messages.error(request, f'We have only {stock_l} {item.product.name} in stock. Sorry.')
                if size == 'XL':
                    if qnty > stock_xl:
                        qnty = stock_xl
                        item.save()
                        messages.error(request, f'We have only {stock_xl} {item.product.name} in stock. Sorry.')
                if size == 'XXL':
                    if qnty > stock_xxl:
                        qnty = stock_xxl
                        item.save()
                        messages.error(request, f'We have only {stock_xxl} {item.product.name} in stock. Sorry.')
                if size == 'XXXL':
                    if qnty > stock_xxxl:
                        qnty = stock_xxxl
                        item.save()
                        messages.error(request, f'We have only {stock_xxxl} {item.product.name} in stock. Sorry.')
            else:
                if item.quantity > item.product.stock:
                    item.quantity = item.product.stock
            total += (item.product.price * item.quantity)
            counter += item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'DOT GEEK Shop - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY

    context = {
        'cart_items': cart_items,
        'total': total,
        'counter': counter,
        'data_key': data_key,
        'stripe_total': stripe_total,
        'description': description
    }
    return render(request, 'cart/cart.html', context)
