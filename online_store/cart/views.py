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
    if Product.objects.filter(id=product_id).exists():
        if CartItem.objects.filter(product=Product.objects.get(id=product_id)).exists():
            cart_item = CartItem.objects.get(product=Product.objects.get(id=product_id))
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(product=Product.objects.get(id=product_id), quantity=1)




    return redirect("cart")
