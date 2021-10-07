# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bookmark(models.Model): #Inherit the class from models
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    created_at = models.CharField(max_length=50)
