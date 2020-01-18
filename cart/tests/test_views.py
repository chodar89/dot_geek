"""
Views test for cart app
"""
from django.test import TestCase, Client
from django.urls import reverse

from products.models import Product, SizeChart, ProductBrand, ProductType
from cart.models import Cart, CartItem

class TestCartViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.add_to_cart_url = reverse('add_to_cart', args=[1])
        self.remove_one_cart_url = reverse('remove_one_cart', args=[20])
        self.increase_one_cart_url = reverse('increase_one_cart', args=[20])
        self.delete_from_cart_url = reverse('delete_from_cart', args=[20])
        self.cart_details_url = reverse('cart_details')

        ProductBrand.objects.create(
            id=1,
            brand_name='brand_test_1',
            is_in_navbar_menu=True
        )
        SizeChart.objects.create(
            id=2,
            size='XL',
        )
        ProductType.objects.create(
            id=1,
            types='type_test_1',
            is_in_navbar_menu=True
        )
        Product.objects.create(
            id=1,
            product_type=ProductType(id=1),
            name='product_test_1',
            brand=ProductBrand(id=1),
            price=9,
            stock=2,
            photo_main='photo_1',
            is_for_sale=True
        )


    def test_add_to_cart_post(self):
        """
        Check status code
        """
        response = self.client.post(self.add_to_cart_url, {'quantity': 1, 'size': 2})
        self.assertEqual(response.status_code, 302)

    def test_remove_one_cart_get(self):
        """
        Check status code
        """
        response = self.client.get(self.remove_one_cart_url)
        self.assertEqual(response.status_code, 404)

    def test_increase_one_cart_get(self):
        """
        Check status code if can not find item
        """
        response = self.client.get(self.increase_one_cart_url)
        self.assertEqual(response.status_code, 404)

    def test_delete_from_cart_get(self):
        """
        Check status code if can not find item
        """
        response = self.client.get(self.delete_from_cart_url)
        self.assertEqual(response.status_code, 404)

    def test_cart_details_get(self):
        """
        Check status code
        """
        response = self.client.get(self.cart_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart_item(self):
        """
        Check if product was added to cart, and check if guest than,
        create new cart with user == None
        """
        self.client.post(self.add_to_cart_url, {'quantity': 1, 'size': 2})
        cart = Cart.objects.all().values('user').get()
        cart_item = CartItem.objects.all().values('product').get()
        self.assertEqual(cart.get('user'), None)
        self.assertEqual(cart_item.get('product'), 1)


    def test_remove_one_cart(self):
        """
        Create cart and cart item than remove
        one from qnty and check status code
        """
        Cart.objects.create(
            id=1,
        )
        CartItem.objects.create(
            id=20,
            product=Product(id=1),
            quantity=5,
            cart=Cart(id=1),
        )
        # Remove one item from cart
        self.client.get(self.remove_one_cart_url)
        cart_item_qnty = CartItem.objects.filter(id=20).values('quantity').get().get('quantity')
        self.assertEqual(cart_item_qnty, 4)
        # Check if status code is redirect
        response = self.client.post(self.remove_one_cart_url)
        self.assertEqual(response.status_code, 302)


    def test_increase_one_cart(self):
        """
        Create cart and cart item than increase
        one from qnty and check status code
        """
        Cart.objects.create(
            id=1,
        )
        CartItem.objects.create(
            id=20,
            product=Product(id=1),
            quantity=1,
            cart=Cart(id=1),
        )
        # Increase one item in cart
        self.client.get(self.increase_one_cart_url)
        cart_item_qnty = CartItem.objects.filter(id=20).values('quantity').get().get('quantity')
        self.assertEqual(cart_item_qnty, 2)
        # Check if status code is redirect
        response = self.client.post(self.increase_one_cart_url)
        self.assertEqual(response.status_code, 302)

    def test_delete_from_cart(self):
        """
        Create cart and cart item than delete
        item and check status code
        """
        Cart.objects.create(
            id=1,
        )
        CartItem.objects.create(
            id=20,
            product=Product(id=1),
            quantity=1,
            cart=Cart(id=1),
        )
        # Delete item from cart
        self.client.get(self.delete_from_cart_url)
        cart_item_qnty = CartItem.objects.filter(id=20)
        if not cart_item_qnty:
            cart_item_qnty = 'delete'
            # Check if status code is redirect
            response = self.client.post(self.delete_from_cart_url)
            self.assertEqual(response.status_code, 404)
        self.assertEqual(cart_item_qnty, 'delete')
