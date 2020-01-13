from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from products.models import ProductBrand, Product, SizeChart
from .utility import _get_price

def search(request):
    """ Render search page with resualts"""

    # Get all products ordered by - newest first
    search_products = Product.objects.filter(
        is_for_sale=True).order_by('-created_at')

    # Keywords from search form
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        # If it's not empty string
        if keywords:
            search_products = search_products.filter(Q(description__icontains=keywords) |
                                                     Q(series__icontains=keywords) |
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
        gte, lte = _get_price(price_range)
        if lte != 0:
            search_products = search_products.filter(
                price__gte=gte, price__lte=lte)
        else:
            search_products = search_products.filter(
                price__gte=gte)

    size_chart = SizeChart.objects.all()

    paginator = Paginator(search_products, 9)

    page = request.GET.get('page')

    paged_search = paginator.get_page(page)

    context = {
        "search_products": paged_search,
        "size_chart": size_chart,
    }

    return render(request, 'search/search.html', context)


def navbar_brand(request, brand_id):
    """ Get all products with brand id from dropdown navbar """

    get_brands = ProductBrand.objects.all()

    size_chart = SizeChart.objects.all()

    get_nav_brand_name = get_brands.filter(id=brand_id).values('brand_name')

    # Get all filtered products ordered by(newest first)
    search_products = Product.objects.all().filter(
        is_for_sale=True).filter(Q(brand=brand_id) |
                                 Q(series__icontains=get_nav_brand_name)).order_by('-created_at')

    paginator = Paginator(search_products, 9)

    page = request.GET.get('page')

    paged_search = paginator.get_page(page)

    context = {
        "search_products": paged_search,
        "size_chart": size_chart,
    }

    return render(request, 'search/navbar_brand.html', context)


def navbar_type(request, type_id):
    """ Get all products with category id from dropdown navbar """

    # Get all filtered products ordered by(newest first)
    search_products = Product.objects.all().filter(is_for_sale=True).filter(
        product_type=type_id).order_by('-created_at')

    size_chart = SizeChart.objects.all()

    paginator = Paginator(search_products, 9)

    page = request.GET.get('page')

    paged_search = paginator.get_page(page)

    context = {
        "search_products": paged_search,
        "size_chart": size_chart,
    }

    return render(request, 'search/navbar_type.html', context)


def carousel_search(request, carousel_id):
    """ Get all products with category id from dropdown navbar """

    # Get all filtered products ordered by(newest first)
    search_products = Product.objects.all().filter(is_for_sale=True).filter(carousel=carousel_id).order_by('-created_at')

    size_chart = SizeChart.objects.all()

    paginator = Paginator(search_products, 9)

    page = request.GET.get('page')

    paged_search = paginator.get_page(page)

    context = {
        "search_products": paged_search,
        "size_chart": size_chart,
    }

    return render(request, 'search/carousel_search.html', context)
