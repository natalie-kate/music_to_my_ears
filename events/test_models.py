""" Imports to test our event models """
from django.test import TestCase
from .models import Event


class TestEventModels(TestCase):
    """ Test product models """
    def setUp(self):
        """ Create test records to use """
        self.event = Event.objects.create(
                name="Test Event",
                date="Everyday",
                time="16:00",
                ticket_price="0.00",
                details="Testing test test",
                location="Red Lion"
            )

    def test_event_string(self):
        """ Test Profile string method """
        self.assertEqual(str(self.event), "Test Event")
