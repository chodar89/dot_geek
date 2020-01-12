"""
Utility functions for cart views
"""


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
