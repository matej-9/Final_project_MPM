from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product, Category
from django.contrib.auth.models import User
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('Product-list')
        self.detail_url = reverse('product', kwargs={"pk": 1})
        self.update_url = reverse('product_update', kwargs={"pk": 1})

        self.user = User.objects.create_superuser(username="admin", password="adminpass")

        # log in as superuser
        self.client.login(username="admin", password="adminpass")

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

    def test_product_list(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'product.html')

    def test_product_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'products.html')

    def test_product_update_POST(self):
        category2 = Category.objects.create(
            name = 'Electronic'
        )

        response = self.client.post(self.update_url, {
            'name': self.product1.name,
            'desc': self.product1.desc,
            'price': self.product1.price,
            'quantity': self.product1.quantity,
            'image': '',
            'category': category2.id
        })

        self.product1.refresh_from_db()
        print(f"Category after update: {self.product1.category.name}")


        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.product1.category.name, 'Electronic')
        self.assertTemplateNotUsed(response, 'product.html')
