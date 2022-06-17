"""
Testing the django rest framework configuration
"""

import json
from audioop import reverse

import requests
from django.http import JsonResponse, request
from django.test import TestCase
from django.urls import reverse
from jokes.models import Joke
from rest_framework import status
from rest_framework.test import APIClient


class JokeAPITestCase(TestCase):
    """
    Basic test case that asserts that we can actually call the API
    """

    def test_can_reach_api_invalid_param(self):
        """
        Asserts that calling the API with an invalid param actually works
        """
        response = self.client.get('/api/v1/joke/?param=invalid')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def setUp_api_valid_dad(self):
        """
        Set up the test case
        """
        url = 'https://icanhazdadjoke.com/'
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'my-app/0.0.1',
            'Accept': 'application/json',
            'Connection': 'keep-alive',
        }
        response = requests.get(url, headers=headers)
        resp = response.json()
            
        self.valid_joke_data = {
            "message": resp['joke']
        }
    
        self.response_200(response)
        data = response.json()
        self.assertEqual(data["code_transaction"], "OK")

    
    def test_can_reach_api_dad(self):
        """
        Asserts that calling the API actually works
        """        
        response = self.client.get('/api/v1/joke/?param=Dad')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def setUp_api_valid_chuck(self):
        """
        Set up the test case
        """
        url = 'https://api.chucknorris.io/jokes/random'
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'my-app/0.0.1',
            'Accept': 'application/json',
            'Connection': 'keep-alive',
        }
        response = requests.get(url, headers=headers)
        resp = response.json()
            
        self.valid_joke_data = {
            "message": resp['value']
        }
        
        self.response_200(response)
        data = response.json()
        self.assertEqual(data["code_transaction"], "OK")


    def test_can_reach_api_chuck(self):
        """
        Asserts that calling the API actually works
        """        
        response = self.client.get('/api/v1/joke/?param=Chuck')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
