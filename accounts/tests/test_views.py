"""
Views test for accounts app
"""
from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User


class TestAccountsViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.dashboard_url = reverse('dashboard')

        User.objects.create_user(
            username='test',
            password='something1',
            email='test@test.com',
            first_name='first_name',
            last_name='last_name')

    def test_register_get(self):
        response = self.client.get(self.register_url)
        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_login_get(self):
        response = self.client.get(self.login_url)
        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_logout_get(self):
        response = self.client.get(self.logout_url)
        # Check status code
        self.assertEqual(response.status_code, 302)

    def test_dashboard_get_if_not_user(self):
        response = self.client.get(self.dashboard_url)
        # Check status code if user not signed in
        self.assertEqual(response.status_code, 302)

    def test_dashboard_get_if_user(self):
        self.client.login(username='test', password='something1')
        response = self.client.get(self.dashboard_url)
        # Check status code if user is signed in
        self.assertEqual(response.status_code, 200)
