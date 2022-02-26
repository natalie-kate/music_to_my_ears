""" Import TestCase to use to test our views """
from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import Event


class TestViews(TestCase):
    """ Test contact views """
    def setUp(self):
        """ Create test records to use """
        self.user = User.objects.create(
                username="tess",
                password="test1abc"
            )
        self.client.force_login(self.user)
        self.event = Event.objects.create(
            name="Test Event",
            date="4th July 2022",
            time="16:00",
            ticket_price="14.00",
            details="Playing all your favourites",
            location="The Pub, Main Street"
        )

    def test_event_view(self):
        """ Test event.html rendered properly """
        response = self.client.get('/events/events/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')

    def test_view_url_accessible_by_name(self):
        """ Test event link """
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)

    def test_event_add_view(self):
        """ Test add_event.html rendered properly """
        response = self.client.get('/events/add_event/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/add_event.html')

    def test_add_url_accessible_by_name(self):
        """ Test add_event link """
        response = self.client.get(reverse('add_event'))
        self.assertEqual(response.status_code, 200)

    def test_event_edit_view(self):
        """ Test add_event.html rendered properly """
        response = self.client.get(f'/events/edit_event/{self.event.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/edit_event.html')

    def test_search(self):
        """ Test search redirect and message if no match """
        response = self.client.get('/events/events/', {
            'search': "Nope"
             })
        error_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(error_messages), 1)
        self.assertEqual(
            str(error_messages[0]),
            "Sorry your search didn't match any of our events")
        self.assertRedirects(response, reverse('events'))

    def test_search_not_empty(self):
        """ Test search redirect and message if empty """
        response = self.client.get('/events/events/', {
            'search': ""
             })
        error_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(error_messages), 1)
        self.assertEqual(
            str(error_messages[0]),
            "Oops you need to enter a search keyword first")
        self.assertRedirects(response, reverse('events'))

    def test_add_event_that_exists(self):
        """ Test redirect and message when event already exists """
        response = self.client.post('/events/add_event/', {
            "name": "Test Event",
            "date": "4th July 2022",
            "time": "16:00",
            "ticket_price": "14.00",
            "details": "Playing all your favourites",
            "location": "The Pub, Main Street"
            })
        error_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(error_messages), 1)
        self.assertEqual(
            str(error_messages[0]),
            'Product already exists in database.')
        self.assertRedirects(response, reverse('events'))

    def test_add_event(self):
        """ Test redirect and message when event added """
        response = self.client.post('/events/add_event/', {
            "name": "New Event",
            "date": "27th June 2022",
            "time": "18:00",
            "ticket_price": "18.00",
            "details": "Karaoke Night",
            "location": "Red Lion, High Street"
            })
        success_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(success_messages), 1)
        self.assertEqual(
            str(success_messages[0]),
            'Successfully added event!')
        self.assertRedirects(response, reverse('events'))

    def test_invalid_event_form(self):
        """ Test redirect and message when invalid event form posted """
        response = self.client.post('/events/add_event/', {
            "name": "",
            "date": "",
            "time": "",
            "ticket_price": "",
            "details": "",
            "location": ""
            })
        error_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(error_messages), 1)
        self.assertEqual(
            str(error_messages[0]),
            'Failed to add event. '
            'Please ensure the form is valid.')
        self.assertRedirects(response, reverse('add_event'))

    def test_edit_event(self):
        """ Test redirect and message when event editied """
        response = self.client.post(f'/events/edit_event/{self.event.id}/', {
            "name": "New Event",
            "date": "27th June 2022",
            "time": "18:00",
            "ticket_price": "18.00",
            "details": "Karaoke Night",
            "location": "Red Lion, High Street"
            })
        success_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(success_messages), 1)
        self.assertEqual(
            str(success_messages[0]), 'Thats updated!')
        self.assertRedirects(response, reverse('events'))

    def test_invalid_edit_event_form(self):
        """ Test redirect and message when invalid edit form posted"""
        response = self.client.post(f'/events/edit_event/{self.event.id}/', {
            "name": "",
            "date": "",
            "time": "",
            "ticket_price": "",
            "details": "",
            "location": ""
            })
        error_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(error_messages), 1)
        self.assertEqual(
            str(error_messages[0]),
            'Failed to update event. '
            'Please ensure the form is valid.')
        self.assertRedirects(response, reverse(
            'edit_event', kwargs={'event_id': self.event.id}))

    def test_delete_event(self):
        """ Test redirect and message when event deleted exists """
        response = self.client.get(f'/events/delete_event/{self.event.id}/')
        success_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(success_messages), 1)
        self.assertEqual(
            str(success_messages[0]), 'Event deleted!')
        self.assertRedirects(response, reverse('events'))
