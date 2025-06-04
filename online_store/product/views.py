from django.shortcuts import render
from django.views.generic import ListView, CreateView
from product.models import Product
from product.forms import ProductForm
from django.urls import reverse_lazy

class Products(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'

class ProductCreate(CreateView):
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('Product-list')