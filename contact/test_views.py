""" Import TestCase to use to test our views """
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """ Test contact views """

    def test_contact_view(self):
        """ Test contact.html rendered properly """
        response = self.client.get('/contact/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_view_url_accessible_by_name(self):
        """ Test contact link """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
