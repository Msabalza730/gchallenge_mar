# -*- coding: utf-8 -*-
"""
    Admin views for the Joke Api   
"""

from django.contrib import admin

from jokes.models import Joke

admin.site.register(Joke)
