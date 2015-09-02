from django.test import TestCase
from django.test import Client


class TestIndex(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_return_200(self):
        response = self.client.get("/")
        self.assertEquals(200, response.status_code)

    def test_index_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")
