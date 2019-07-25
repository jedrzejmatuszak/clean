import json
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse, reverse_lazy
from ..models import *
from ..serializers import *


# initialize client
client = APIClient()


class GetAllFlatTest(APITestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        self.flat_1 = Flat.objects.create(name='Test Flat 1')
        self.flat_2 = Flat.objects.create(name='Test Flat 2')

    # TODO: not finished - sth wrong with HyperlinkedIdentityField - needs some aditional context
    # TODO: but were is that context?

    def test_get_all_flats(self):
        # get API response
        response = client.get(reverse('flat-list'))
        # get data from db
        flats = Flat.objects.all()
        serializer = FlatSerializer(flats, many=True, context={'request': client.request()})
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_flat(self):
        # get API response
        response = client.get(reverse('flat-detail', kwargs={'pk': self.flat_1.pk}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.get(reverse('flat-detail', kwargs={'pk': 4}), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
