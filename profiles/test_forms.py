""" Import TestCase to use to test our form """
from django.test import TestCase
from .forms import UserProfileForm, SavedAddressForm


class TestUserProfileForm(TestCase):
    """ Test UserProfileForm """

    def test_form_is_valid(self):
        """ None of the fields are required """
        form = UserProfileForm({})
        self.assertTrue(form.is_valid())

    def test_form_fields_not_user(self):
        """ User field is not displayed """
        form = UserProfileForm({})
        self.assertEqual(form.Meta.exclude, ('user',))


class TestSavedAddressForm(TestCase):
    """ Test SavedAddressForm """

    def test_form_is_valid(self):
        """ None of the fields are required """
        form = SavedAddressForm({})
        self.assertTrue(form.is_valid())

    def test_form_fields_not_user(self):
        """ User field is not displayed """
        form = SavedAddressForm({})
        self.assertEqual(form.Meta.exclude, ('user',))
