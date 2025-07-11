"""
URL configuration for online_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from accounts.views import SignUpView, user_logout, MyLoginView
from cart.models import CartItem
from cart.views import Cart, add_to_cart, update_cart, pay, thanks, shipping_address

from . import views
from .views import ContactView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home, name='home'),
    path("", views.home),
    path("products/", include("product.urls")),

    path('accounts/logout/', user_logout, name='logout'),
    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    path("cart/",Cart.as_view(), name='cart'),
    path("cart/add_to_cart/", add_to_cart, name='add_to_cart'),
    path('cart/update_cart/', update_cart, name='update_cart'),
    path('cart/pay', pay, name='pay'),
    path('cart/shipping_address', shipping_address, name='shipping_address'),
    path('cart/thanks/', thanks, name='thanks'),

    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('contact/', ContactView.as_view(), name='contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


