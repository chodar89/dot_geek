from cart.models import Cart, CartItem
from django.contrib.auth.models import User
from cart.views import _cart_id, _get_user_or_none

def item_counter(request):
    """
    Cart item counter for navbar, get user cart if logged,
    if not check for cart id from function or create one.
    Iterate in cart items and count them.
    """
    item_count = 0
    if 'admin' not in request.path:
        user_id = _get_user_or_none(request)
        if user_id:
            user = User.objects.get(id=user_id)
            try:
                cart = Cart.objects.get(user=user)
            except Cart.DoesNotExist:
                user_cart = Cart.objects.filter(cart_id=_cart_id(request))
                if user_cart:
                    user_cart.update(user=user)
                else:
                    user_cart = Cart.objects.create(
                        cart_id=_cart_id(request),
                        user=user
                    )
                cart = Cart.objects.get(user=user)
            try:
                # Get all items from session cart and assign
                # to user cart when user logged in.
                cart_session = Cart.objects.get(cart_id=_cart_id(request))
                cart_session_items = CartItem.objects.filter(cart=cart_session)
                user_cart_items = CartItem.objects.filter(cart=cart)
                if cart_session != cart:
                    for item in cart_session_items:
                        try:
                            user_cart_item = user_cart_items.get(product=item.product)
                            user_cart_item.quantity += item.quantity
                            item.delete()
                            user_cart_item.save()
                        except CartItem.DoesNotExist:
                            item.cart = cart
                            item.save()
            except Cart.DoesNotExist:
                pass
        else:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    cart_id=_cart_id(request)
                    )
                cart.save()
        try:
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                item_count += item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
