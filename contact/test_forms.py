""" Import TestCase to use to test our form """
from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """ Test ContactForm """

    def test_empty_form_not_valid(self):
        """ Unfilled form not valid """
        form = ContactForm({})
        self.assertFalse(form.is_valid())

    def test_form_not_valid_without_name(self):
        """ Form without name not valid """
        form = ContactForm({
            "first_name": "",
            "surname": "Test",
            "email": "test@test.com",
            "order_number": "12345",
            "query": "Bla Bla Bla",
            "rate_us": "3"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')

    def test_form_not_valid_without_surname(self):
        """ Form without surname not valid """
        form = ContactForm({
            "first_name": "Test",
            "surname": "",
            "email": "test@test.com",
            "order_number": "12345",
            "query": "Bla Bla Bla",
            "rate_us": "3"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('surname', form.errors.keys())
        self.assertEqual(
            form.errors['surname'][0], 'This field is required.')

    def test_form_not_valid_without_email(self):
        """ Form without email not valid """
        form = ContactForm({
            "first_name": "Tess",
            "surname": "Test",
            "email": "",
            "order_number": "12345",
            "query": "Bla Bla Bla",
            "rate_us": "3"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_form_fields(self):
        """ All fields displayed """
        form = ContactForm({})
        self.assertEqual(form.Meta.exclude, ('user', 'email_date'))
