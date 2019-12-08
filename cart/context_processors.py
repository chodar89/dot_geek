from products.models import ProductBrand, ProductType

from django.contrib.auth.models import User


def _get_user_or_none(request):
    if request.user.is_authenticated:
        user_id_or_none = request.user.id
    else:
        user_id_or_none = None
    return user_id_or_none
