from django.test import SimpleTestCase
from django.urls import reverse, resolve

from products.views import all_products, product


class TestProductsUrls(SimpleTestCase):


    def test_all_products_url_is_resolved(self):
        url = reverse('all_products')
        self.assertEqual(resolve(url).func, all_products)

    def test_product_url_is_resolved(self):
        url = reverse('product', args=[1])
        self.assertEqual(resolve(url).func, product)
