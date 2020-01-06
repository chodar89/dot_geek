from django.test import SimpleTestCase
from django.urls import reverse, resolve

from cart.views import add_to_cart, cart_details, remove_one_cart, increase_one_cart, delete_from_cart


class TestCartUrls(SimpleTestCase):


    def test_add_to_cart_url_is_resolved(self):
        url = reverse('add_to_cart', args=[1])
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_cart_details_url_is_resolved(self):
        url = reverse('cart_details')
        self.assertEqual(resolve(url).func, cart_details)

    def test_remove_one_cart_url_is_resolved(self):
        url = reverse('remove_one_cart', args=[1])
        self.assertEqual(resolve(url).func, remove_one_cart)

    def test_increase_one_cart(self):
        url = reverse('increase_one_cart', args=[1])
        self.assertEqual(resolve(url).func, increase_one_cart)

    def test_delete_from_cart_url_is_resolved(self):
        url = reverse('delete_from_cart', args=[1])
        self.assertEqual(resolve(url).func, delete_from_cart)
