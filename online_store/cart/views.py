from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView

from cart.models import CartItem
from product.models import Product


class Cart(ListView):

    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart'


def add_to_cart(request):
    product_id=request.POST.get('product_id')
    product = get_object_or_404(Product, pk=product_id)
    CartItem.objects.get_or_create(product=product)



    return redirect("cart")
