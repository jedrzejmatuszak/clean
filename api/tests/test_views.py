from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.urls import reverse
from ..views import *
from ..models import *
from ..serializers import *


class GetAllFlatTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.view = FlatViewSet.as_view({'get': 'list'})
        self.flat_1 = Flat.objects.create(name='Test Flat 1')
        self.flat_2 = Flat.objects.create(name='Test Flat 2')

    def test_get_all_flats(self):
        """ Test module for GET all flat API """
        # get API response
        request = self.factory.get(reverse('flat-list'))
        response = self.view(request)
        # get data from db
        flats = Flat.objects.all()
        serializer = FlatSerializer(flats, many=True, context={'request': request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_flat(self):
        """ Test module for GET single flat API """
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
        """ Test module for create, update, delete single flat instance """
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


class GetAllFlatmateTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FlatmateViewSet.as_view({'get': 'list'})
        self.client = APIClient()
        self.test_flat = Flat.objects.create(name='Test Flat')
        self.test_flat2 = Flat.objects.create(name='Test Flat 2')
        self.test_user1 = User.objects.create_user(username='User1', password='User1')
        self.test_user2 = User.objects.create_user(username='User2', password='User2')
        self.test_user3 = User.objects.create_user(username='User3', password='User3')

    def test_create_get_all_flatmates(self):
        """ Test module for create flatmate to self.test_flat and
        get all flatmates for self.test_flat """
        # createing flatmates
        flatmate1 = self.client.post(reverse('flatmate-list'),
                                     {'user': self.test_user1.pk, 'flat': self.test_flat.pk},
                                     format='json')
        # get API response
        request = self.factory.get(reverse('flatmate-list'))
        response = self.view(request)
        # get Flatmates from db
        flatmates = Flatmate.objects.all()
        serializer = FlatmateSerializer(flatmates, many=True, context={'request': request})
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_flatmate_detail(self):
        """ Test module for flatmate details """
        # creating flatmate instance
        response = self.client.post(reverse('flatmate-list'),
                                    {'user': self.test_user2.pk, 'flat': self.test_flat.pk},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # get API response
        response = self.client.get(reverse('flatmate-detail', kwargs={'pk': response.json()['id']}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_update_delete_flatmate(self):
        """ Test module for create, update and delete flatmate instance """
        # Create flatmate instance
        response = self.client.post(reverse('flatmate-list'),
                                    {'flat': self.test_flat.pk, 'user': self.test_user3.pk},
                                    format='json')
        flatmate_id = response.json()['id']
        flatmate = Flatmate.objects.last()
        serializer = FlatmateDetailSerializer(flatmate)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data, serializer.data)
        self.assertEqual(flatmate.id, flatmate_id)
        # Update flatmate instance
        response = self.client.patch(reverse('flatmate-detail', kwargs={'pk': flatmate_id}),
                                     {'user': self.test_user3.pk, 'flat': self.test_flat2.pk},
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.patch(reverse('flatmate-detail', kwargs={'pk': 23}),
                                     {'user': self.test_user3.pk, 'flat': self.test_flat2.pk},
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Delete flatmate instance
        response = self.client.delete(reverse('flatmate-detail', kwargs={'pk': flatmate_id}),
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.delete(reverse('flatmate-detail', kwargs={'pk': 22}),
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
