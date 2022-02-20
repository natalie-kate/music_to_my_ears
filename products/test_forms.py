""" Import TestCase to use to test our form """
from django.test import TestCase
from .forms import ProductForm
from .models import Genre


class TestProductForm(TestCase):
    """ Test ProductForm """

    def setUp(self):
        self.genre = Genre.objects.create(
            genre='genre',
            friendly_name='Genre',
        )

    def test_empty_form_not_valid(self):
        """ Unfilled form not valid """
        form = ProductForm({})
        self.assertFalse(form.is_valid())

    def test_form_not_valid_without_title(self):
        """ Form without title not valid """
        form = ProductForm({
            "title": "",
            "artist": "Test",
            "genre": self.genre,
            "release_year": "1986",
            "price": "12.99",
            "description": "Testing testing",
            "stock_quantity": "5",
            "track_list": "T, Te, Tes, Test"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(
            form.errors['title'][0], 'This field is required.')

    def test_form_not_valid_without_artist(self):
        """ Form without artist not valid """
        form = ProductForm({
            "title": "Test",
            "artist": "",
            "genre": self.genre,
            "release_year": "1986",
            "price": "12.99",
            "description": "Testing testing",
            "stock_quantity": "5",
            "track_list": "T, Te, Tes, Test"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('artist', form.errors.keys())
        self.assertEqual(
            form.errors['artist'][0], 'This field is required.')

    def test_form_not_valid_without_genre(self):
        """ Form without genre not valid """
        form = ProductForm({
            "title": "Test",
            "artist": "Test",
            "genre": "",
            "release_year": "1986",
            "price": "12.99",
            "description": "Testing testing",
            "stock_quantity": "5",
            "track_list": "T, Te, Tes, Test"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('genre', form.errors.keys())
        self.assertEqual(
            form.errors['genre'][0], 'This field is required.')

    def test_form_not_valid_without_price(self):
        """ Form without price not valid """
        form = ProductForm({
            "title": "Test",
            "artist": "Test",
            "genre": self.genre,
            "release_year": "1986",
            "price": "",
            "description": "Testing testing",
            "stock_quantity": "5",
            "track_list": "T, Te, Tes, Test"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')

    def test_form_not_valid_without_quantity(self):
        """ Form without quantity not valid """
        form = ProductForm({
            "title": "Test",
            "artist": "Test",
            "genre": self.genre,
            "release_year": "1986",
            "price": "12.99",
            "description": "Testing testing",
            "stock_quantity": "",
            "track_list": "T, Te, Tes, Test"
            })
        self.assertFalse(form.is_valid())
        self.assertIn('stock_quantity', form.errors.keys())
        self.assertEqual(
            form.errors['stock_quantity'][0], 'This field is required.')

    def test_form_not_valid_without_tracklist(self):
        """ Form without tracklist not valid """
        form = ProductForm({
            "title": "Test",
            "artist": "Test",
            "genre": self.genre,
            "release_year": "1986",
            "price": "12.99",
            "description": "Testing testing",
            "stock_quantity": "5",
            "track_list": ""
            })
        self.assertFalse(form.is_valid())
        self.assertIn('track_list', form.errors.keys())
        self.assertEqual(
            form.errors['track_list'][0], 'This field is required.')

    def test_form_not_valid_without_comma_in_tracklist(self):
        """ Form without comma in tracklist not valid """
        form = ProductForm({
            "title": "Test",
            "artist": "Test",
            "genre": self.genre,
            "release_year": "1986",
            "price": "12.99",
            "description": "Testing testing",
            "stock_quantity": "5",
            "track_list": "1. T 2. Te "
            })
        self.assertFalse(form.is_valid())

    def test_form_fields(self):
        """ All fields displayed """
        form = ProductForm({})
        self.assertEqual(form.Meta.fields, '__all__')

    def required_attribute(self):
        """ Correct fields have required attribute """
        form = ProductForm({})
        self.assertEqual(form.fields['title'].widget.attrs['required'], True)
        self.assertEqual(form.fields['artist'].widget.attrs['required'], True)
        self.assertEqual(
            form.fields['release_year'].widget.attrs['required'], True)
        self.assertEqual(
            form.fields['price'].widget.attrs['required'], True)
        self.assertEqual(
            form.fields['stock_quantity'].widget.attrs['required'], True)
        self.assertEqual(
            form.fields['track_list'].widget.attrs['required'], True)
