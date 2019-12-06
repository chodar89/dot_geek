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
        # If it's not empty string
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
        # If it's not empty
        if get_type:
            search_products = search_products.filter(product_type=get_type)

    # Check prce range from search form
    if 'price-range' in request.GET:
        price_range = request.GET['price-range']
        # If it's not empty
        if price_range == "0-10":
            search_products = search_products.filter(price__gte=0, price__lte=10)
        if price_range == "10-20":
            search_products = search_products.filter(price__gte=10, price__lte=20)
        if price_range == "20-30":
            search_products = search_products.filter(price__gte=20, price__lte=30)
        if price_range == "30-40":
            search_products = search_products.filter(price__gte=30, price__lte=40)
        if price_range == "40-50":
            search_products = search_products.filter(price__gte=40, price__lte=50)
        if price_range == "50+":
            search_products = search_products.filter(price__gte=50)

    get_brands = ProductBrand.objects.all()

    get_types = ProductType.objects.all()

    size_chart = SizeChart.objects.all()

    context = {
        "get_brands": get_brands,
        "get_types": get_types,
        "search_products": search_products,
        "size_chart": size_chart,
    }

    return render(request, 'search/search.html', context)

def navbar_brand(request, brand_id):
    """ Get all products with brand id from dropdown navbar """

    get_brands = ProductBrand.objects.all()

    get_types = ProductType.objects.all()

    size_chart = SizeChart.objects.all()

    get_nav_brand_name = get_brands.filter(id=brand_id).values('brand_name')

    # Get all filtered products ordered by(newest first)
    search_products = Product.objects.all().filter(
        is_for_sale=True).filter(Q(brand=brand_id)|
                                 Q(series__icontains=get_nav_brand_name)).order_by('-created_at')

    context = {
        "get_brands": get_brands,
        "get_types": get_types,
        "search_products": search_products,
        "size_chart": size_chart,
    }

    return render(request, 'search/navbar_brand.html', context)

def navbar_type(request, type_id):
    """ Get all products with category id from dropdown navbar """

     # Get all filtered products ordered by(newest first)
    search_products = Product.objects.all().filter(is_for_sale=True).filter(product_type=type_id).order_by('-created_at')

    get_brands = ProductBrand.objects.all()

    get_types = ProductType.objects.all()

    size_chart = SizeChart.objects.all()

    context = {
        "get_brands": get_brands,
        "get_types": get_types,
        "search_products": search_products,
        "size_chart": size_chart,
    }

    return render(request, 'search/navbar_type.html', context)
