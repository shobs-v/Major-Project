# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render


def new_index(request):
    output=""
    if request.method == 'POST':
        text = request.POST['inputTextBox']
        if(text):
            print(text)
            output="hi"
        else:
            uploaded_file = request.FILES['document']
            print(uploaded_file.name)
            print(uploaded_file.size)

    return render(request,'home/new_index.html',{'output':output})
