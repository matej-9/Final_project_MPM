from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import profile_view, SignUpView, MyLoginView, user_logout, accounts_landing

app_name = 'accounts'

urlpatterns = [
    path('', accounts_landing, name='accounts-landing'),
    path('profile/', profile_view, name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
