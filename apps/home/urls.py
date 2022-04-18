# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # The home page
    path('', views.new_index, name='home'),

]

urlpatterns += staticfiles_urlpatterns()