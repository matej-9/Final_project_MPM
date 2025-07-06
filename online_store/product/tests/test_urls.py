from django.test import SimpleTestCase
from django.urls import reverse, resolve
from product.views import ProductDetail, Products, ProductCreate

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('Product-list')
        self.assertEquals(resolve(url).func.view_class, Products)

    def test_add_url_is_resolved(self):
        url = reverse('product_create')
        self.assertEquals(resolve(url).func.view_class, ProductCreate)

    def test_detail_url_is_resolved(self):
        url = reverse('product', kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, ProductDetail)