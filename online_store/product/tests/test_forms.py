from django.test import TestCase
from product.forms import ProductForm
from product.models import Product, Category

class TestForms(TestCase):

    def test_form_valuid(self):
        self.category1 = Category.objects.create(
            name = 'App'
        )
        form = ProductForm(data={
            'name' : 'PC',
            'desc' : 'Good',
            'price' : 1000,
            'quantity' : 20,
            'image' : '',
            'category' : self.category1
        })

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = ProductForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)