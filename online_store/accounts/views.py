from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'form.html'
    success_url = reverse_lazy('movies')


class MyLoginView(LoginView):
    template_name = 'form.html'
    success_url = reverse_lazy('movies')


def user_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))


"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
"""
