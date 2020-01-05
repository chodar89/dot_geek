from django.test import TestCase, Client
from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404

from products.models import ProductBrand, Product, ProductType



class TestProductsViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.all_products_url = reverse('all_products')
        self.product_url = reverse('product', args=[1])
        ProductBrand.objects.create(
            id=1,
            brand_name='brand_test_1',
            is_in_navbar_menu=True
        )
        ProductType.objects.create(
            id=1,
            types='type_test_1',
            is_in_navbar_menu=True
        )
        Product.objects.create(
            id=1,
            product_type=ProductType(id=1),
            name='product_test_1',
            brand=ProductBrand(id=1),
            price=9,
            stock=2,
            photo_main='photo_1',
            is_for_sale=True
        )

    def test_all_products_get(self):
        response = self.client.get(self.all_products_url)

        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        # Check if search product query (from view) match to type ID that was passed in view
        all_products = Product.objects.filter(is_for_sale=True).order_by('-created_at')
        self.assertEqual(all_products[:1].values('name').get().get('name'), 'product_test_1')

    def test_product_get(self):
        response = self.client.get(self.product_url)

        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product.html')
        # Check if search product query (from view) match to type ID that was passed in view
        get_product = get_object_or_404(Product, pk=1)
        self.assertEqual(get_product.name, 'product_test_1')
        # Check status code when product not exists
        with self.assertRaises(Http404):
            get_object_or_404(Product, pk=2)
