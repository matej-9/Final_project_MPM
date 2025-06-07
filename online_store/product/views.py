from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from product.models import Product
from product.forms import ProductForm
from django.urls import reverse_lazy

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

class ProductCreate(CreateView):
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('Product-list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('Product-list')

class ProductUpdate(UpdateView):
    form_class = ProductForm
    template_name = 'product_update.html'
    model = Product
    success_url = reverse_lazy('Product-list')