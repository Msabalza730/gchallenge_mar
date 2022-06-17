# -*- coding: utf-8 -*-
"""
    Views for the challenge Joke API    
    - C.R.U.D
"""

import requests
from jokes.api import serializers
from jokes.models import Joke
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response


class JokeApiViewSet(generics.ListAPIView):
    
    serializer_class = serializers.genericSerializer
    
    # Endpoint that will be passed a query param called “numbers” with a list of integers. The response from this endpoint must be the least common multiple of them.
    def get_queryset(self):
        numbers = self.request.query_params.get('numbers', None)
        if numbers is not None:
            numbers = numbers.split(',')
            numbers = [int(i) for i in numbers]
            return Joke.objects.filter(id__in=numbers)
    
    
    
    # Endpoint to which a query param called “number” with an integer will be passed. The answer will be that number + 1.
    def get_queryset(self):
        number = self.request.query_params.get('number', None)
        if number is not None:
            return Joke.objects.filter(id=number)
    
        
        
    # C.R.U.D
    def get(self, request, format=None):
        params = self.request.query_params.get('param', None)
        #params = self.get_object(txt)

        url = ''
        data = {}
        
        if params == 'Chuck': #http://0.0.0.0:8000/api/v1/joke/?param=Chuck
            url = 'https://api.chucknorris.io/jokes/random'
            response = requests.get(url)
            resp = response.json()
            data = {
                "message": resp['value']
            }
            
        elif params == 'Dad': #http://0.0.0.0:8000/api/v1/joke/?param=Dad
            url = 'https://icanhazdadjoke.com/'
            headers = {
                'Accept': 'application/json',
                'User-Agent': 'my-app/0.0.1',
                'Accept': 'application/json',
                'Connection': 'keep-alive',
            }
            response = requests.get(url, headers=headers)
            resp = response.json()

                    
            data = {
                "message": resp['joke']
            }
            
        else:
            data = {
                "message": "No param specified"
                }
            
        return Response(data=data)


    def post(self, request, format=None):
        
        jokes = self.request.data.get('joke', None)
        
        joke = Joke.objects.create(joke=jokes)
        joke.save()
        
        data = {
                "message": "Saved",
                "id": joke.id,
                "joke": joke.joke
                }
        
        return Response(data=data)
    
    
    def put(self, request, format=None):
        
        jokes = self.request.data.get('joke', None)
        id = self.request.data.get('id', None)
        
        joke = Joke.objects.get(id=id)
        joke.joke = jokes
        joke.save()
        
        data = {
                "message": "Updated",
                "id": joke.id,
                "joke": joke.joke
                }
        
        return Response(data=data)
    
    
    def delete(self, request, format=None):
        
        id = self.request.data.get('id', None)
        
        
        joke = Joke.objects.get(id=id)
        joke.delete()
        
        data = {
                "message": "Deleted"
                }
        
        return Response(data=data)

