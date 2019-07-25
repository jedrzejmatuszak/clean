from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.urls import reverse
from ..models import Flat
from ..serializers import FlatSerializer, FlatDetailSerializer
from ..views import *
import json


class GetAllFlatTest(APITestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.view = FlatViewSet.as_view({'get': 'list'})
        self.flat_1 = Flat.objects.create(name='Test Flat 1')
        self.flat_2 = Flat.objects.create(name='Test Flat 2')

    def test_get_all_flats(self):
        # get API response
        request = self.factory.get(reverse('flat-list'))
        response = self.view(request)
        # get data from db
        flats = Flat.objects.all()
        serializer = FlatSerializer(flats, many=True, context={'request': request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_flat(self):
        # get API response
        response = self.client.get(reverse('flat-detail',
                                           kwargs={'pk': self.flat_1.pk}),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(reverse('flat-detail',
                                           kwargs={'pk': self.flat_2.pk}))
        serializer = FlatDetailSerializer(Flat.objects.get(pk=self.flat_2.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        response = self.client.get(reverse('flat-detail', kwargs={'pk': 4}),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_update_delete_flat(self):
        response = self.client.post(reverse('flat-list'), {'name': 'Post Flat'},
                                    format='json')
        flat_id = response.json()['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('flat-list'), {'naame': 'Flat Post'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.patch(reverse('flat-detail', kwargs={'pk': flat_id}),
                                     {'name': 'Flat update'},
                                     format='json')
        serializer = FlatDetailSerializer(Flat.objects.get(id=flat_id))
        self.assertNotEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(reverse('flat-detail', kwargs={'pk': flat_id}),
                                     {'naame': 'Dupa'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.delete(reverse('flat-detail', kwargs={'pk': flat_id}),
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
