from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from cart.models import CartItem


class Cart(ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart'


