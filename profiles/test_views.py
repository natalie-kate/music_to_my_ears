""" Import TestCase to use to test our views """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import UserProfile


class TestViews(TestCase):
    """ Test profile views """
    def setUp(self):
        """ Create test records to use """
        self.user = User.objects.create(
                username="tess",
                password="test1abc"
            )
        self.client.force_login(self.user)

    def test_profile_view(self):
        """ Test profile.html rendered properly """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_url_accessible_by_name(self):
        """ Test shop link """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
