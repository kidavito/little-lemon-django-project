from django.test import TestCase
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def test_getall(self):
        client = APIClient()
        client.post('/api/menu', {'title': 'Lemon'}, format='json')