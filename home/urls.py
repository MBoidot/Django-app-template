from django.urls import re_path, path, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    re_path(r'^accounts/login/$', LoginView.as_view(template_name='home/login.html'), name='login'),
    re_path(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^accounts/register/$', views.UserFormView.as_view(), name='register'),
    re_path(r'^', views.HomeView, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/password_reset', PasswordResetCompleteView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='home/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="home/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='home/password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset"),
]
