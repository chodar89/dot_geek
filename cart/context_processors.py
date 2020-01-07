from cart.models import Cart, CartItem
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
            cart = Cart.objects.filter(user=user_id)[:1]
            try:
                # Get all items from session cart and assign
                # to user cart when user logged in.
                cart_session = Cart.objects.get(cart_id=_cart_id(request))
                cart_session_items = CartItem.objects.all().filter(cart=cart_session)
                get_cart_id = cart.get()
                for item in cart_session_items:
                    item.cart = get_cart_id
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
            cart_items = CartItem.objects.all().filter(cart=cart)
            for item in cart_items:
                item_count += item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
