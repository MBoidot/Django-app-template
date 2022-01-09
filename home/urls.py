from django.urls import re_path
from django.contrib import admin

from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'home'

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(template_name='home/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
    re_path(r'^', views.HomeView, name='home'),
]
