"""
Views for the accounts app: login, signup, logout, profile.
"""

from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.models import Profile

def accounts_landing(request):
    """
    View to render landing page with signup and login forms.
    """
    signup_form = SignUpForm()
    login_form = AuthenticationForm()
    return render(
        request,
        "accounts/landing_both.html",
        {
            "signup_form": signup_form,
            "login_form": login_form,
        },
    )

class SignUpView(CreateView):
    """
    View to handle user signup with SignUpForm.
    """
    form_class = SignUpForm
    template_name = "form.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_name"] = "SignUpView"
        return context

class MyLoginView(LoginView):
    """
    Custom login view using Django's LoginView.
    """
    template_name = "form.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_name"] = "MyLoginView"
        return context

@login_required(login_url="/accounts/login/")
def user_logout(request):
    """
    Log out the user and redirect back to referring page or home.
    """
    logout(request)
    return redirect(request.META.get("HTTP_REFERER", "/"))

@login_required(login_url="/accounts/login/")
def profile_view(request):
    """
    View to display and create user profile if not exists.
    """
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user) # pylint: disable=no-member
    return render(request, "profile.html", {"profile": profile})
