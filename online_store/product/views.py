from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from product.models import Product, Category
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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        category_name = self.request.GET.get('category')
        if category_name:
            queryset = queryset.filter(category__name__iexact=category_name)
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset.order_by('category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(products__isnull=False).distinct()
        context['selected_category'] = self.request.GET.get('category')
        return context

class ProductCreate(CreateView):
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('Product-list')

class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('Product-list')

    def test_func(self):
        return self.request.user.is_superuser

class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ProductForm
    template_name = 'product_update.html'
    model = Product
    success_url = reverse_lazy('Product-list')

    def test_func(self):
        return self.request.user.is_superuser
    