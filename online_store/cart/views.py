from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView
from django.contrib import messages
from cart.form import ShippingAddressForm
from cart.models import CartItem
from product.models import Product


class Cart(LoginRequiredMixin,ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

@login_required
def add_to_cart(request):
    product_id=request.POST.get('product_id')

    if Product.objects.filter(id=product_id).exists():
        if CartItem.objects.filter(user = request.user, product=Product.objects.get(id=product_id)).exists():
            cart_item = CartItem.objects.get(user = request.user,product=Product.objects.get(id=product_id))
            if cart_item.product.quantity > cart_item.quantity:
                cart_item.quantity += 1
                cart_item.save()
        else:
            if Product.objects.get(id=product_id).quantity > 0:
                CartItem.objects.create(product=Product.objects.get(id=product_id), quantity=1, user = request.user)

    return redirect("cart")

@login_required
def update_cart(request):
    """AJAX + and -"""
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        action = request.POST.get('action')

        cart_item = get_object_or_404(CartItem, id=item_id,user = request.user)

        if action == 'plus':
                if cart_item.product.quantity > cart_item.quantity:
                    cart_item.quantity += 1
                    cart_item.save()

        elif action == 'minus':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
                return JsonResponse({'deleted': True})

        total_price = cart_item.quantity * cart_item.product.price

        return JsonResponse({
            'quantity': cart_item.quantity,
            'total': total_price
        })


@login_required
def pay(request):
    user_cart_items = CartItem.objects.filter(user=request.user)
    for item in user_cart_items:
        if item.product.quantity < item.quantity:
            messages.error(request, f"Nedostatok tovaru: {item.product.name}.")
            return redirect("cart")

    return redirect("shipping_address")


@login_required
def shipping_address(request):

    user_cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in user_cart_items)

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)

        if form.is_valid():
            #old pay functionality from def pay(request)
            for item in user_cart_items:
                if item.product.quantity >= item.quantity:
                    item.product.quantity -= item.quantity
                    item.product.save()

            user_cart_items.delete()
            return redirect('thanks')
    else:
        form = ShippingAddressForm()

    if hasattr(request.user, 'profile'):
        profile = request.user.profile
        form.fields['first_name'].initial = request.user.first_name
        form.fields['last_name'].initial = request.user.last_name
        form.fields['phone_number'].initial = profile.phone_number
        form.fields['country'].initial = profile.country
        form.fields['city'].initial = profile.city
        form.fields['street'].initial = profile.street
        form.fields['zip_code'].initial = profile.zip_code

    return render(request, "shipping_address.html", {"form": form, "total_price": total_price})


@login_required
def thanks(request):
    return render(request, 'thanks.html')