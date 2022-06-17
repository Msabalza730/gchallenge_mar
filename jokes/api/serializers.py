# -*- coding: utf-8 -*-
"""
    Serializers for the Joke Api  
"""

from jokes.models import Joke
from rest_framework import serializers


class JokeAPISerializer(serializers.ModelSerializer):
    """
        Serializer for the JokeAPI model
    """
    joke = serializers.JSONField()
    
    
    class Meta:
        model = Joke
        fields ='__all__'

class genericSerializer(serializers.Serializer):
    
    data = serializers.ReadOnlyField()
