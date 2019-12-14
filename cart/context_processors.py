from django.core.exceptions import ObjectDoesNotExist

from cart.models import Cart, CartItem
from cart.views import _cart_id, _get_user_or_none


def item_counter(request):
    """
    Cart item counter for navbar
    """
    item_count = 0
    if 'admin' not in request.path:
        user_id = _get_user_or_none(request)
        if user_id:
            try:
                cart = Cart.objects.filter(user=user_id)
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
                for item in cart_items:
                    item_count += item.quantity
            except Cart.DoesNotExist:
                item_count = 0
    return dict(item_count=item_count)
