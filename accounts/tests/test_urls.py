from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import login, register, logout, dashboard


class TestAccountsUrls(SimpleTestCase):


    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard)
