from django.test import SimpleTestCase
from django.urls import reverse, resolve

from search.views import search, navbar_brand, navbar_type, carousel_search

class TestSearchUrls(SimpleTestCase):


    def test_search_url_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEqual(resolve(url).func, search)

    def test_navbar_brand_url_is_resolved(self):
        url = reverse('navbar_brand', args=[1])
        self.assertEqual(resolve(url).func, navbar_brand)

    def test_navbar_type_url_is_resolved(self):
        url = reverse('navbar_type', args=[1])
        self.assertEqual(resolve(url).func, navbar_type)

    def test_carousel_search_urls_is_resolved(self):
        url = reverse('carousel_search', args=[1])
        self.assertEqual(resolve(url).func, carousel_search)
