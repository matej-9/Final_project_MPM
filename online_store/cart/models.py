from django.db import models
from django.db.models import ForeignKey, PositiveIntegerField

from product.models import Product


class CartItem(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE)
    quantity = PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    def __repr__(self):
        return f"{self.quantity}x {self.product.name}"