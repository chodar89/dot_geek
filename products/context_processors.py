from django.core.exceptions import ObjectDoesNotExist

from products.models import ProductBrand, ProductType


def get_brands_types_for_navbar(request):
    """
    Get brands and categories for dropdown menu
    """

    nav_menu_brands = ProductBrand.objects.all().filter(is_in_navbar_menu=True)

    nav_menu_category = ProductType.objects.all().filter(is_in_navbar_menu=True)

    brands_types_for_navbar = {
        "nav_menu_brands": nav_menu_brands,
        "nav_menu_category": nav_menu_category,
    }

    return brands_types_for_navbar
