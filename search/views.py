from django.shortcuts import render
from django.db.models import Q

from products.models import ProductBrand, ProductType, Product, SizeChart

# Create your views here.

def search(request):
    """ Render search page with resualts"""

    # Get all products ordered by - newest first
    search_products = Product.objects.all().filter(is_for_sale=True).order_by('-created_at')

    # Keywords from search form
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        # If its not empty string
        if keywords:
            search_products = search_products.filter(Q(description__icontains=keywords)|
                                                     Q(series__icontains=keywords)|
                                                     Q(character__icontains=keywords))

    # Brand from select search form
    if 'brand' in request.GET:
        brand = request.GET['brand']
        # If it's not empty
        if brand:
            search_products = search_products.filter(brand_id=brand)

    # Category from select search form
    if 'type' in request.GET:
        get_type = request.GET['type']
        if get_type:
            search_products = search_products.filter(product_type=get_type)

    get_brands = ProductBrand.objects.all()

    get_types = ProductType.objects.all()

    context = {
        "get_brands": get_brands,
        "get_types": get_types,
        "search_products": search_products,
    }

    return render(request, 'search/search.html', context)
