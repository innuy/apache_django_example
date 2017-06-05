# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Example(models.Model):
    example_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
