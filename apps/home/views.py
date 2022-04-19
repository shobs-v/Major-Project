# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from statistics import mean
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from numpy import disp
# from apps.home.models import Meanings


def new_index(request):
    # meanings_list = Meanings.objects.order_by('word')
    # medical_words = [] 
    # for word in meanings_list.iterator():
    #     medical_words.append(word.word) 
    # ex_summary = {'test':'I do not like Biopsy and Cardiac arrest.'}
    # summary_words = ex_summary['test'].split()
    # display_summary = {}
    # for word in summary_words:
    #     if word in medical_words:
    #         medical_meaning = Meanings.objects.get(word = word).meaning
    #         display_summary.update({word:medical_meaning})

    #     else:
    #         display_summary.update({word:''})
    # print(display_summary)
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
    
    # Final disctionary with words and meanings
    final_display_summary = {'key':display_summary}

    return render(request,'home/new_index.html',final_display_summary)
