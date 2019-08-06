import datetime
from api.models import CustomUser
from django.test import TestCase
from ..models import *


class ModelTests(TestCase):
    """Test module for all models"""

    def setUp(self):
        # createing new flat
        test_flat = Flat.objects.create(name=f'Test Flat')
        # creating new room instances for test flat
        room_bath = Room.objects.create(name='Bathroom', flat=test_flat)
        room_bed = Room.objects.create(name='Bedroom', flat=test_flat)
        # creating clenups instances for rooms
        cleanup_bath_1 = CleanUp.objects.create(name='cleanup_bath_1', points=25, room=room_bath)
        cleanup_bed_1 = CleanUp.objects.create(name='cleanup_bed_1', points=32, room=room_bed)
        # creating user & flatmate
        test_user = CustomUser.objects.create_user(username='test_user', password='test_user')
        test_flatmate = Flatmate.objects.create(user=test_user, flat=test_flat)
        test_record_1 = Record.objects.create(
            flat=test_flat,
            room=room_bath,
            cleanup=cleanup_bath_1,
            flatmate=test_flatmate,
            author=test_user,
            to_date="2019-09-01"
        )
        test_record_2 = Record.objects.create(
            flat=test_flat,
            room=room_bed,
            cleanup=cleanup_bed_1,
            flatmate=test_flatmate,
            author=test_user,
            to_date="2019-09-01"
        )

    def test_flat_name(self):
        test_flat = Flat.objects.get(name='Test Flat')
        self.assertEqual(test_flat.name, 'Test Flat')

    def test_room(self):
        test_room = Room.objects.get(name='Bathroom')
        self.assertEqual(test_room.flat.name, 'Test Flat')
        self.assertEqual(test_room.name, 'Bathroom')
        test_room = Room.objects.get(name='Bedroom')
        self.assertEqual(test_room.flat.name, 'Test Flat')
        self.assertEqual(test_room.name, 'Bedroom')

    def test_cleanups(self):
        test_cleanup = CleanUp.objects.get(name='cleanup_bath_1')
        self.assertEqual(test_cleanup.points, 25)
        self.assertEqual(test_cleanup.room.name, 'Bathroom')
        test_cleanup = CleanUp.objects.get(name='cleanup_bed_1')
        self.assertEqual(test_cleanup.points, 32)
        self.assertEqual(test_cleanup.room.name, 'Bedroom')

    def test_flatmates(self):
        user = CustomUser.objects.get(username='test_user')
        test_flatmate = Flatmate.objects.get(user=user)
        self.assertTrue(test_flatmate.user.username, 'test_user')
        self.assertEqual(test_flatmate.flat.name, 'Test Flat')

    def test_records(self):
        flat = Flat.objects.get(name='Test Flat')
        test_record = Record.objects.filter(flat=flat).first()
        self.assertEqual(test_record.room.name, 'Bathroom')
        self.assertEqual(test_record.flatmate.user.username, 'test_user'),
        self.assertTrue(test_record.points, 25)
        self.assertNotEqual(test_record.to_date, datetime.date(2019, 8, 1)),
        flat = Flat.objects.get(name='Test Flat')
        test_record = Record.objects.filter(flat=flat).last()
        self.assertEqual(test_record.room.name, 'Bedroom')
        self.assertEqual(test_record.flatmate.user.username, 'test_user'),
        self.assertNotEqual(test_record.points, 25)
        self.assertNotEqual(test_record.to_date, datetime.date(2019, 8, 1)),
