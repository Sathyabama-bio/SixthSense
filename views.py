# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
#from .models import Quest
from typing import Dict


def index(request):
    template = loader.get_template('Dietplan_app/index.html')
    context = dict(latest_question_list="")
    return HttpResponse(template.render(context, request))


def Dietplan(request):

    name=request.POST.get("food_hbt")
    print name
    if name == 'Veg':
        template = loader.get_template('Dietplan_app/lowfatvegan.html')
    else:
        template = loader.get_template('Dietplan_app/lchf.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
