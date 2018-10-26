# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime


def suckimage(request):
    return HttpResponse('<h1>Page was found</h1>')