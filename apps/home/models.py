# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meanings(models.Model):
	id = models.AutoField(primary_key=True)
	word = models.CharField(max_length=100, unique= True)
	meaning = models.CharField(max_length=300)

	def __str__(self):
		return self.word
