from django.shortcuts import render, get_object_or_404

from .models import Product, SizeChart, ProductType, ProductBrand


def all_products(request):
    """ Get all products and size chart than pass it and render """

    # Get all products ordered by - newest first
    get_all_products = Product.objects.all().filter(is_for_sale=True).order_by('-created_at')

    size_chart = SizeChart.objects.all()

    get_brands = ProductBrand.objects.all()

    get_types = ProductType.objects.all()

    context = {
        'all_products': get_all_products,
        'size_chart': size_chart,
        "get_brands": get_brands,
        "get_types": get_types,
    }
    return render(request, 'products/all_products.html', context)

def product(request, product_id):
    """ Single product page, get product id and render html with product details """

    get_product = get_object_or_404(Product, pk=product_id)

    size_chart = SizeChart.objects.all()

    context = {
        'product': get_product,
        'size_chart': size_chart,
    }

    return render(request, 'products/product.html', context)
