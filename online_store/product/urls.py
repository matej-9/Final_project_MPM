from django.urls import path, include
from product.views import Products, ProductCreate, ProductDelete, ProductDetail, ProductUpdate

urlpatterns = [
    path("", Products.as_view(), name='Product-list'),
    path("create/", ProductCreate.as_view(), name='product_create'),
    path("delete/<int:pk>/", ProductDelete.as_view(), name='product_delete'),
    path("<int:pk>/", ProductDetail.as_view(), name='product'),
    path("update/<int:pk>/", ProductUpdate.as_view(), name='product_update'),
]