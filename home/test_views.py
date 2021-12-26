""" Import TestCase to use to test our views """
from django.test import TestCase


class TestViews(TestCase):
    """ Test home views """
    def test_home_view(self):
        """ Test index.html rendered properly """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
