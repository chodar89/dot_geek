from django.core.exceptions import ObjectDoesNotExist

from products.models import ProductBrand, ProductType


def get_brands_types_for_navbar(request):
    """
    Get brands and categories for dropdown menu
    """

    get_brands = ProductBrand.objects.all()

    get_types = ProductType.objects.all()

    nav_menu_brands = get_brands.filter(is_in_navbar_menu=True)

    nav_menu_category = get_types.filter(is_in_navbar_menu=True)

    brands_types_for_navbar = {
        "nav_menu_brands": nav_menu_brands,
        "nav_menu_category": nav_menu_category,
        'get_brands': get_brands,
        'get_types': get_types,
    }

    return brands_types_for_navbar
