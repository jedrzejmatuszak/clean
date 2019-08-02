from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from ..models import CustomUser
from api.models import Flat
from django.urls import reverse


class TestAuth(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.flat = Flat.objects.create(name='test')

    def test_api_user_app(self):
        # CustomUser creation
        data = {
            'username': 'test',
            'password': 'alpine12',
            'email': 'test@test.pk'
        }
        response = self.client.post(reverse('customuser-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = CustomUser.objects.get(username='test')
        # simulation of email authentication
        user.is_active = True
        user.save()
        # Authentication test
        data = {
            'username': 'test',
            'password': 'alpine12'
        }
        response = self.client.post(reverse('login'), data, format='json')
        token = response.json()['auth_token']
        self.assertTrue(token)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+token)
        response = self.client.get(reverse('flat-detail', kwargs={'pk': 1}))
        self.assertEqual(response.json()['name'], 'test')
