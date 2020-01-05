from django.test import TestCase, Client
from django.urls import reverse

from products.models import ProductBrand, Product, ProductType
from pages.models import IndexCarousel


class TestSearchViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.search_url = reverse('search')
        self.navbar_type_url = reverse('navbar_type', args=[1])
        self.navbar_brand_url = reverse('navbar_brand', args=[1])
        self.carousel_search_url = reverse('carousel_search', args=[1])
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
        IndexCarousel.objects.create(
            id=1,
            image='photo',
            first=True
        )
        Product.objects.create(
            product_type=ProductType(id=1),
            name='product_test_1',
            brand=ProductBrand(id=1),
            price=9,
            stock=2,
            carousel=IndexCarousel(id=1),
            photo_main='photo_1',
            is_for_sale=True
        )

    def test_search_get(self):
        response = self.client.get(self.search_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search.html')

    def test_navbar_type_get(self):
        response = self.client.get(self.navbar_type_url)

        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/navbar_type.html')
        # Check if search product query (from view) match to type ID that was passed in view
        search_products = Product.objects.all().filter(is_for_sale=True).filter(
        product_type=ProductType(id=1)).order_by('-created_at')
        self.assertEqual(search_products[:1].values('name').get().get('name'), 'product_test_1')

    def test_navbar_brand_get(self):
        response = self.client.get(self.navbar_brand_url)

        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/navbar_brand.html')
        # Check if search product query (from view) match to type ID that was passed in view
        search_products = Product.objects.all().filter(is_for_sale=True).filter(
        brand=ProductBrand(id=1)).order_by('-created_at')
        self.assertEqual(search_products[:1].values('name').get().get('name'), 'product_test_1')

    def test_carousel_search_get(self):
        response = self.client.get(self.carousel_search_url)

        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/carousel_search.html')
        # Check if search product query (from view) match to type ID that was passed in view
        search_products = Product.objects.all().filter(is_for_sale=True).filter(
        carousel=IndexCarousel(id=1)).order_by('-created_at')
        self.assertEqual(search_products[:1].values('name').get().get('name'), 'product_test_1')
