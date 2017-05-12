# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def homepage(request):
    """
    Homepage
    """
    return render (
        request,
        'organizer/homepage.html'
    )
