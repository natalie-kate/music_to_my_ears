""" Import TestCase to use to test our form """
from django.test import TestCase
from .forms import EventForm


class TestEventForm(TestCase):
    """ Test EventForm """

    def test_empty_form_not_valid(self):
        """ Unfilled form not valid """
        form = EventForm({})
        self.assertFalse(form.is_valid())

    def test_form_not_valid_without_name(self):
        """ Form without name not valid """
        form = EventForm({
            "name": "",
            "date": "Test",
            "time": "18:00",
            "image": "test.png",
            "ticket_price": "12.99",
            "details": "Testing testing",
            "location": "Test, Test Street, Testshire"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_form_not_valid_without_date(self):
        """ Form without date not valid """
        form = EventForm({
            "name": "Test",
            "date": "",
            "time": "18:00",
            "image": "test.png",
            "ticket_price": "12.99",
            "details": "Testing testing",
            "location": "Test, Test Street, Testshire"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(
            form.errors['date'][0], 'This field is required.')

    def test_form_not_valid_without_time(self):
        """ Form without time not valid """
        form = EventForm({
            "name": "Test",
            "date": "Test",
            "time": "",
            "image": "test.png",
            "ticket_price": "12.99",
            "details": "Testing testing",
            "location": "Test, Test Street, Testshire"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(
            form.errors['time'][0], 'This field is required.')

    def test_form_not_valid_without_ticket_price(self):
        """ Form without ticket price not valid """
        form = EventForm({
            "name": "Test",
            "date": "Test",
            "time": "18:00",
            "image": "test.png",
            "ticket_price": "",
            "details": "Testing testing",
            "location": "Test, Test Street, Testshire"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('ticket_price', form.errors.keys())
        self.assertEqual(
            form.errors['ticket_price'][0], 'This field is required.')

    def test_form_not_valid_without_details(self):
        """ Form without details not valid """
        form = EventForm({
            "name": "Test",
            "date": "Test",
            "time": "18:00",
            "image": "test.png",
            "ticket_price": "12.99",
            "details": "",
            "location": "Test, Test Street, Testshire"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('details', form.errors.keys())
        self.assertEqual(
            form.errors['details'][0], 'This field is required.')

    def test_form_not_valid_without_location(self):
        """ Form without location not valid """
        form = EventForm({
            "name": "Test",
            "date": "Test",
            "time": "18:00",
            "image": "test.png",
            "ticket_price": "12.99",
            "details": "Testing testing",
            "location": ""
            })
        self.assertFalse(form.is_valid())
        self.assertIn('location', form.errors.keys())
        self.assertEqual(
            form.errors['location'][0], 'This field is required.')

    def test_placeholders(self):
        """ Check placeholders """
        form = EventForm({})
        self.assertEqual(form.fields['name'].widget.attrs['placeholder'],
                         'e.g Open Mic Night')
        self.assertEqual(form.fields['date'].widget.attrs['placeholder'],
                         'e.g 25th June 2022')
        self.assertEqual(form.fields['time'].widget.attrs['placeholder'],
                         'e.g 19:30')
        self.assertEqual(
            form.fields['location'].widget.attrs['placeholder'],
            'e.g Red Lion, Main St, Prestwick, Ayrshire')
        self.assertEqual(form.fields['details'].widget.attrs['placeholder'],
                         "e.g Open Mic night, all welcome"
                         " we have everything bar your talent.")
        self.assertEqual(form.fields['ticket_price'].widget.attrs['placeholder'],
                         "e.g 22.00 or 0 if free")

    def test_form_fields(self):
        """ All fields displayed """
        form = EventForm({})
        self.assertEqual(form.Meta.exclude, ('user',))
