# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bookmark(models.Model): #Inherit the class from models
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
