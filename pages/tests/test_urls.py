from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import index, contact

print('xxx')

class TestPagesUrls(SimpleTestCase):


    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)
