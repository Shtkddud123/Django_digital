# -*- coding: utf-8 -*
from __future__ import unicode_literals

from django.db import models
from organizer.models import Startup, Tag

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)
