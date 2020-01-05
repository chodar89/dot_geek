from django.test import TestCase, Client
from django.urls import reverse

from products.models import Product, ProductBrand, ProductType
from pages.models import IndexCarousel



class TestPagesViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.contact_url = reverse('contact')
        self.index_url = reverse('index')
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
            heading='heading_test_1',
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


    def test_contact_get(self):
        response = self.client.get(self.contact_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/contact.html')

    def test_index_get(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_index_get_context_data(self):
        response = self.client.get(self.index_url)

        get_bestsellers = response.context['bestseller'].get().name
        get_new_in = response.context['new_in'].get().name
        get_carousel = response.context['carousels'].get().heading

        self.assertEqual(get_bestsellers, 'product_test_1')
        self.assertEqual(get_new_in, 'product_test_1')
        self.assertEqual(get_carousel, 'heading_test_1')
