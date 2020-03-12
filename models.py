# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dob = models.DateTimeField('dob')
    sex = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    howlong = models.IntegerField()
    vegnonveg = models.CharField(max_length=200)

class patient_history(models.Model):
    vegornonveg = models.CharField(max_length=200)