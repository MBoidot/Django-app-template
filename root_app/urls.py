from django.urls import re_path, include, path
from django.contrib import admin
from home import views
from . import views
from django.contrib.auth.views import PasswordResetCompleteView



urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^',include('home.urls')),

]
