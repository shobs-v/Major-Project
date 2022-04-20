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
from django.core.files.storage import default_storage
from numpy import disp
import os
from apps.home.utils import MedDictionary,TextSummarizer,MedNER

from bs4 import BeautifulSoup
import requests

dictionary = MedDictionary()
summarizer = TextSummarizer()
ner = MedNER()

def new_index(request):
    input_text = ""
    if request.method == 'POST':
        text = request.POST['inputTextBox']
        url = request.POST['url']
        if(text):
            input_text = text
        elif(url):
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "lxml")

            soup1=soup.find("div", class_="abstract-content")
            input_text = soup1.get_text().replace('\n','').strip()
        else:
            uploaded_file = request.FILES['document']
            print(uploaded_file)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            media_path = os.path.join(BASE_DIR,'media')
            full_path=os.path.join(media_path,uploaded_file.name)
            f = default_storage.open(full_path, 'r')
            data = f.read()
            input_text = data
            f.close()

    summary = str(summarizer.summarize(input_text))
    ents = ner.ents(summary)
    key = meaning_dict(summary,ents)
    final_display_summary = {'key':key}

    return render(request,'home/new_index.html',final_display_summary)

def meaning_dict(text,ents):
    key = {}
    for ent in ents:
        text=text.replace(ent,"<ent>"+ent+"<ent>")
    for word in text.split('<ent>'):
        word = word.strip()
        if word in ents:
            key[word] = dictionary.meaning(word)
        else:
            key[word] = ''
    return key