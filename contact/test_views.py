""" Import TestCase to use to test our views """
from django.test import TestCase
from django.core import mail
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .models import Contact
from .forms import ContactForm


class TestViews(TestCase):
    """ Test contact views """
    def setUp(self):
        """ Create test records to use """
        self.user = User.objects.create(
                username="tess",
                password="test1abc"
            )
        self.user1 = User.objects.create(
                username="toby",
                password="testa123"
            )
        self.userprofile = UserProfile.objects.get(user=self.user)
        self.userprofile.default_first_name = "Tess"
        self.userprofile.default_surname = "Test"
        self.userprofile.default_email = "tess@test.com"

    def test_contact_view(self):
        """ Test contact.html rendered properly """
        response = self.client.get('/contact/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_view_url_accessible_by_name(self):
        """ Test contact link """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        """ Test redirect upon successful form submission """
        response = self.client.post('/contact/contact/', {
            'first_name': "Tess",
            'surname': "Test",
            'email': "tess@test.com",
            'order_number': "",
            'query': "",
            'rate_us': 1})
        self.assertRedirects(response, reverse('shop'))

    def test_user_added(self):
        """ Test user added to contact record """
        self.client.force_login(self.user)
        self.client.post('/contact/contact/', {
            'first_name': "Tess",
            'surname': "Test",
            'email': "tess@test.com",
            'order_number': "",
            'query': "",
            'rate_us': 1})
        new_contact = Contact.objects.get(user=self.user)
        self.assertTrue(new_contact)

    def test_invalid_form(self):
        """ Test message and redirect when form invalid"""
        response = self.client.post('/contact/contact/', {
            'first_name': "",
            'surname': "",
            'email': "",
            'order_number': "",
            'query': "",
            'rate_us': ""})
        error_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(error_messages), 1)
        self.assertEqual(
            str(error_messages[0]), 'There was an error with your form. \
                Please double check your information.')
        self.assertRedirects(response, reverse('contact'))

    def test_form_prefills(self):
        """ Check form prefills when user has saved data """
        self.client.force_login(self.user)
        self.assertTrue(UserProfile.objects.get(user=self.user))
        self.assertTrue(ContactForm(initial={
                    'first_name': "Tess",
                    'surname': "Test",
                    'email': "tess@test.com"
                }))

    def test_form_empty_profile_uncomplete(self):
        """ Check form doesn't prefill when profile not completed """
        self.client.force_login(self.user1)
        self.assertTrue(UserProfile.objects.get(user=self.user1))
        self.assertTrue(ContactForm(initial={
                    'first_name': "",
                    'surname': "",
                    'email': ""
                }))

    def test_form_empty_for_unauthorised_user(self):
        """ Check form doesn't prefill for unauthoried user """
        self.assertTrue(ContactForm(initial={
                    'first_name': "",
                    'surname': "",
                    'email': ""
                }))


class TestEmails(TestCase):
    """ Test email sends """
    def test_send_email(self):
        """ Check upon form submission email is sent """
        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
