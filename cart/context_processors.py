from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from cart.models import Cart, CartItem
from cart.views import _cart_id, _get_user_or_none

import stripe
from django.conf import settings


def cart_details(request, total=0, counter=0, cart_items=None):
    """
    Check all items in cart, count qnty and total price and
    return dict as a context processors so it can be displayed in nav bar
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
    return context
