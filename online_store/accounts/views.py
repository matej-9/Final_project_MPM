from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views

from accounts.models import Profile

def accounts_landing(request):
    signup_form = SignUpForm()
    login_form = AuthenticationForm()
    return render(request, 'accounts/landing_both.html', {
        'signup_form': signup_form,
        'login_form': login_form,
    })


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'SignUpView'
        return context


class MyLoginView(LoginView):
    template_name = 'form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'MyLoginView'
        return context


def user_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='/accounts/login/')
def profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'profile.html', {'profile': profile})
