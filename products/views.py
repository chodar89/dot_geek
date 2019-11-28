from django.shortcuts import render, get_object_or_404

from .models import Product, ProductBrand, ProductType, SizeChart

# Create your views here.
def all_products(request):

    all_products = Product.objects.all().filter(is_for_sale=True)

    size_chart = SizeChart.objects.all()

    context = {
        'all_products': all_products,
        'size_chart': size_chart,
    }
    return render(request, 'products/all_products.html', context)

def product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product.html', context)
