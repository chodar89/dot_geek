from django.shortcuts import render

from products.models import Product, SizeChart
from .models import IndexCarousel


def index(request):
    """
    Render index page with carousel imgs, new in and bestseller products
    """
    carousels = IndexCarousel.objects.all()

    all_products = Product.objects.all().filter(is_for_sale=True)

    new_in = all_products.order_by('-id')[:9]

    bestseller = all_products.order_by('-buys')[:6]

    size_chart = SizeChart.objects.all()

    context = {
        'carousels': carousels,
        'new_in': new_in,
        'bestseller': bestseller,
        'size_chart': size_chart,
    }

    return render(request, 'pages/index.html', context)


def contact(request):
    """
    Render contact page
    """
    return render(request, 'pages/contact.html')
