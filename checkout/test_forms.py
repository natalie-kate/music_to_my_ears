""" Import TestCase to use to test our form """
from django.test import TestCase
from .forms import OrderForm, DeliveryForm


class TestOrderForm(TestCase):
    """ Test OrderForm """

    def test_empty_form_not_valid(self):
        """ Unfilled form not valid """
        form = OrderForm({})
        self.assertFalse(form.is_valid())

    def test_form_not_valid_without_name(self):
        """ Form without first name not valid """
        form = OrderForm({
            "first_name": "",
            "surname": "Test",
            "email": "test@test.com",
            "phone_number": "12345",
            "street_address1": "5 Test Street",
            "street_address2": "Flat 2b",
            "town_or_city": "Test",
            "county": "Testshire",
            "country": "Testuania",
            "postcode": "G12 4HL"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')

    def test_form_not_valid_without_surname(self):
        """ Form without surname not valid """
        form = OrderForm({
            "first_name": "Tess",
            "surname": "",
            "email": "test@test.com",
            "phone_number": "12345",
            "street_address1": "5 Test Street",
            "street_address2": "Flat 2b",
            "town_or_city": "Test",
            "county": "Testshire",
            "country": "Testuania",
            "postcode": "G12 4HL"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('surname', form.errors.keys())
        self.assertEqual(
            form.errors['surname'][0], 'This field is required.')

    def test_form_not_valid_without_email(self):
        """ Form without email not valid """
        form = OrderForm({
            "first_name": "Tess",
            "surname": "Test",
            "email": "",
            "phone_number": "12345",
            "street_address1": "5 Test Street",
            "street_address2": "Flat 2b",
            "town_or_city": "Test",
            "county": "Testshire",
            "country": "Testuania",
            "postcode": "G12 4HL"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_form_not_valid_without_phone_number(self):
        """ Form without phone number not valid """
        form = OrderForm({
            "first_name": "Tess",
            "surname": "Test",
            "email": "test@test.com",
            "phone_number": "",
            "street_address1": "5 Test Street",
            "street_address2": "Flat 2b",
            "town_or_city": "Test",
            "county": "Testshire",
            "country": "Testuania",
            "postcode": "G12 4HL"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_form_not_valid_without_street_address(self):
        """ Form without street address not valid """
        form = OrderForm({
            "first_name": "Tess",
            "surname": "Test",
            "email": "test@test.com",
            "phone_number": "12345",
            "street_address1": "",
            "street_address2": "Flat 2b",
            "town_or_city": "Test",
            "county": "Testshire",
            "country": "Testuania",
            "postcode": "G12 4HL"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_form_not_valid_without_town(self):
        """ Form without town not valid """
        form = OrderForm({
            "first_name": "Tess",
            "surname": "Test",
            "email": "test@test.com",
            "phone_number": "12345",
            "street_address1": "5 Test Street",
            "street_address2": "Flat 2b",
            "town_or_city": "",
            "county": "Testshire",
            "country": "Testuania",
            "postcode": "G12 4HL"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_form_not_valid_without_country(self):
        """ Form without country not valid """
        form = OrderForm({
            "first_name": "Tess",
            "surname": "Test",
            "email": "test@test.com",
            "phone_number": "12345",
            "street_address1": "5 Test Street",
            "street_address2": "Flat 2b",
            "town_or_city": "Test",
            "county": "Testshire",
            "country": "",
            "postcode": "G12 4HL"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_form_fields(self):
        """ All fields displayed """
        form = OrderForm({})
        self.assertEqual(form.Meta.fields, (
            'first_name', 'surname', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'county', 'country', 'postcode',
            ))

    def test_attributes(self):
        """ Correct fields have required, autofocus attributes """
        form = OrderForm({})
        self.assertEqual(
            form.fields['first_name'].widget.attrs['autofocus'], True)
        self.assertEqual(form.fields['surname'].widget.attrs['required'], True)
        self.assertEqual(
            form.fields['email'].widget.attrs['required'], True)
        self.assertEqual(
            form.fields['phone_number'].widget.attrs['required'], True)
        self.assertEqual(
            form.fields['street_address1'].widget.attrs['required'], True)
        self.assertEqual(
            form.fields['town_or_city'].widget.attrs['required'], True)


class TestDeliveryForm(TestCase):
    """ Test DeliveryForm """
    def test_form_fields(self):
        """ All fields displayed """
        form = DeliveryForm({})
        self.assertEqual(form.Meta.fields, (
            'delivery_street_address1', 'delivery_street_address2',
            'delivery_town_or_city', 'delivery_county', 'delivery_country',
            'delivery_postcode',
            ))
