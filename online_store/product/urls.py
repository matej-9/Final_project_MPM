from django.urls import path, include
from product.views import Products, ProductCreate

urlpatterns = [
    path("", Products.as_view(), name='Product-list'),
    path("create/", ProductCreate.as_view(), name='product_create'),

]