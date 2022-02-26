""" Import TestCase to use to test our views """
from django.test import TestCase
from django.core import mail
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .models import Contact


class TestViews(TestCase):
    """ Test contact views """
    def setUp(self):
        """ Create test records to use """
        self.user = User.objects.create(
                username="tess",
                password="test1abc"
            )
        self.userprofile = UserProfile.objects.get(user=self.user)

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


class TestEmails(TestCase):
    """ Test email sends """
    def test_send_email(self):
        """ Check upon form submission email is sent """
        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
