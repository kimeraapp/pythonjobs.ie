from django.test import TestCase
from django.test import Client
from pythonjobs.services import generate_token
import re


class TestJob(TestCase):
    def setUp(self):
        self.client = Client()
        self.token = generate_token()

    def test_generate_token_returns_not_empty_string(self):
        self.assertNotEqual(len(self.token), 0)

    def test_generate_token_returns_uppercase_and_number(self):
        self.assertTrue(re.match(r'[A-Z0-9+]', self.token))
