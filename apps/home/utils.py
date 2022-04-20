from PyDictionary import PyDictionary
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

from transformers import AlbertTokenizer, AlbertModel
from summarizer import Summarizer

import scispacy
import spacy
import en_ner_bionlp13cg_md

import requests
import json

class MedDictionary():
    
    def __init__(self):
        self.tags = {'JJ':'Adjective','JJR':'Adjective',
                     'JJS':'Adjective','NN':'Noun',
                     'NNP':'Noun','NNS':'Noun',
                    'VB':'Verb','VBD':'Verb',
                    'VBG':'Verb','VBN':'Verb',
                    'VBP':'Verb','VBZ':'Verb'}
        self.dictionary = PyDictionary()
        self.lemmatizer = WordNetLemmatizer()
    
    def meaning(self,word):
        lemm = self.lemmatizer.lemmatize(word)
        try:
            response = requests.get(
            url="https://app.scrapingbee.com/api/v1/store/google",
            params={
                "api_key": "N49DKTJ556ALVKJ7932OPCCFI6KVOPTKUJXAFCXNYQGT59AJXCD2002DB8U34RZBUVEVW3KI316NARF8",
                "search": word,
                "nb_results":1
            },
            )
            res = response.content.decode('utf-8')
            js = json.loads(res)
            return js['organic_results'][0]['description'].split('.')[0]
        
        except:
            return ''

class TextSummarizer():
    
    def __init__(self):
        self.albert_model = AlbertModel.from_pretrained('albert-base-v2', output_hidden_states=True)
        self.albert_tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
        self.albert = Summarizer(custom_model=self.albert_model, custom_tokenizer=self.albert_tokenizer, random_state = 7)
    
    def summarize(self,text):
        return self.albert(text,num_sentences=int(0.4*len(text.split('.'))))

class MedNER():

    def __init__(self):
        self.nlp = spacy.load('en_ner_bionlp13cg_md')
    
    def ents(self,text):
        doc = self.nlp(text)
        return list(set(list(map(str,doc.ents))))
