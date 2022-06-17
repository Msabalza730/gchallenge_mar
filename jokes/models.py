# -*- coding: utf-8 -*-
"""
    Models for the Joke API
    
"""

from django.db import models


class Joke(models.Model):
    """
        JokeAPI model for save jokes.
    """
    
    
    joke = models.CharField(max_length=255, blank=True, null=True)
    
    
    def __str__(self):
        return self.joke
    
    class Meta:
        verbose_name = 'Joke'
        verbose_name_plural = 'Jokes'
