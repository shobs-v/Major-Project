# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path,include
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from apps.home import views


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("",views.new_index, name = "index"),
    path("home/", include("apps.home.urls")),
]
