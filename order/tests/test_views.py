from django.test import TestCase, Client
from django.urls import reverse

from order.models import OrderItem, Order


class TestOrderViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.order_url = reverse('order', args=[1])
        self.thankyou_url = reverse('thankyou')

        OrderItem.objects.create(
            product='test_product_1',
            quantity=2,
            price=10,
            order=Order(id=1)
        )
        OrderItem.objects.create(
            product='test_product_2',
            quantity=1,
            price=5,
            order=Order(id=1)
        )
        Order.objects.create(
            token='1234',
            id=1,
            total=10,
        )

    def test_order_get(self):
        response = self.client.get(self.order_url)
        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/order.html')

    def test_thankyou_get(self):
        # Create session for view
        session = self.client.session
        session['thankyou'] = 1
        session.save()

        response = self.client.get(self.thankyou_url)
        # Check status code and does it use correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/thankyou.html')

    def test_get_order_items(self):
        response = self.client.get(self.order_url)

        get_order_items = response.context['get_order_items']
        items = []
        for item in get_order_items:
            items.append(item.product)
        self.assertEqual(items, ['test_product_1', 'test_product_2'])
