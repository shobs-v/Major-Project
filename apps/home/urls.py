# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'home'
urlpatterns = [
    # The home page
    path('', views.new_index, name='home'),
    path('about_us/',views.about_us,name = 'About_Us'),

]

urlpatterns += staticfiles_urlpatterns()