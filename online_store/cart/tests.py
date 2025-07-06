from numbers import Number

from django.contrib.auth.models import User
from django.test import TestCase

from cart.form import ShippingAddressForm
from cart.models import CartItem
from product.models import Product


class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin',
            password='Neviemmm'
        )

        self.product = Product.objects.create(
            name='Test Product',
            price=10,
            quantity=5
        )
        self.cart_item = CartItem.objects.create(
            product=self.product,
            quantity=2,
            user=self.user
        )

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.quantity, 2)
        self.assertEqual(self.cart_item.user, self.user)

    def test_get_total_price(self):
        expected_total = self.cart_item.quantity * self.product.price
        self.assertEqual(self.cart_item.get_total_price(), expected_total)


class SimpleFormTest(TestCase):

    def test_spravne_vyplneny_formular(self):
        data = {
            'first_name': 'Patrik',
            'last_name': 'Polák',
            'phone_number': '+421901234567',
            'country': 'Slovensko',
            'city': 'Bratislava',
            'street': 'Neviem',
            'zip_code': '12345'
        }

        form = ShippingAddressForm(data=data)
        self.assertTrue(form.is_valid())