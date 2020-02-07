"""
Utility functions for cart views
"""

import stripe


def _get_user_or_none(request):
    """
    Check if user is authenticated
    """
    if request.user.is_authenticated:
        user_id_or_none = request.user.id
    else:
        user_id_or_none = None
    return user_id_or_none


def _cart_id(request):
    """
    Get cart session if not create one
    """
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        request.session.create()
        request.session['cart_id'] = request.session.session_key
        cart_id = request.session['cart_id']
    return cart_id


def _get_product_stock(size, i):
    if size == 'XS':
        product_stock = i.product.stock_xs
    elif size == 'S':
        product_stock = i.product.stock_s
    elif size == 'M':
        product_stock = i.product.stock_m
    elif size == 'L':
        product_stock = i.product.stock_l
    elif size == 'XL':
        product_stock = i.product.stock_xl
    elif size == 'XXL':
        product_stock = i.product.stock_xxl
    elif size == 'XXXL':
        product_stock = i.product.stock_xxxl
    else:
        product_stock = i.product.stock
    return product_stock

def _charge(total, description, customer):
    charge = stripe.Charge.create(
        amount=total,
        currency="gbp",
        description=description,
        customer=customer.id
    )
    return charge