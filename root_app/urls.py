from django.urls import re_path, include
from django.contrib import admin
from home import views
from . import views
from home import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^',include('home.urls')),
]
