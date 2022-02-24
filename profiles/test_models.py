""" Imports to test our profile models """
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class TestProfileModels(TestCase):
    """ Test product models """
    def setUp(self):
        """ Create test records to use """
        self.user = User.objects.create(
                username="tess",
                password="test1abc"
            )
        self.userprofile = UserProfile.objects.get(user=self.user)

    def test_profile_created(self):
        """ Test Profile created when new user create """
        self.assertTrue(self.userprofile)

    def test_profile_string(self):
        """ Test Profile string method """
        self.assertEqual(str(self.userprofile), "tess")
