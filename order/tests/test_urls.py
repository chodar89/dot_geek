from django.test import SimpleTestCase
from django.urls import reverse, resolve

from order.views import order, thankyou


class TestOrderUrls(SimpleTestCase):


    def test_order_url_is_resolved(self):
        url = reverse('order', args=[1])
        self.assertEqual(resolve(url).func, order)

    def test_thankyou_url_is_resolved(self):
        url = reverse('thankyou')
        self.assertEqual(resolve(url).func, thankyou)
