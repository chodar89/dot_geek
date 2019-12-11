from django.core.exceptions import ObjectDoesNotExist

from products.models import ProductBrand, ProductType

from cart.models import Cart, CartItem
from cart.views import _cart_id, _get_user_or_none


def get_brands_types_for_navbar(request):

    user_id = _get_user_or_none(request)
    session_cart_id = _cart_id(request)
    cart_qnty = 0

    nav_menu_brands = ProductBrand.objects.all().filter(is_in_navbar_menu=True)

    nav_menu_category = ProductType.objects.all().filter(is_in_navbar_menu=True)

    get_brands_types_for_navbar = {
        "nav_menu_brands": nav_menu_brands,
        "nav_menu_category": nav_menu_category,
    }

    return get_brands_types_for_navbar
