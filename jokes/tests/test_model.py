"""
    Test the model.
"""

from django.test import TestCase
from jokes.models import Joke


class JokeTestCase(TestCase):
    """
    Test the model.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.joke = Joke.objects.create(
            message="This is a test joke."
        )

    def test_can_repr(self):    
        """
        Asserts that the repr works.
        """
        self.assertEqual(
            repr(self.joke),
            "<Joke: This is a test joke.>"
        )
