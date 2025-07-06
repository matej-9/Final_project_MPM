from django.test import TestCase
from product.models import Product, Category

class TestModels(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(
            name = 'App'
        )

        self.product1 = Product.objects.create(
            name = 'PC',
            desc = 'Good',
            price = 1000,
            quantity = 20,
            image = '',
            category = self.category1
        )

    def test_product_is_assigned(self):
        self.assertAlmostEquals(self.product1.name, 'PC')
        self.assertAlmostEquals(self.product1.category, self.category1)