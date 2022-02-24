""" Import TestCase Vinyl, Genre and Image to test our models """
from django.test import TestCase
from .models import Genre, Vinyl, Image


class TestProductModels(TestCase):
    """ Test product models """
    def setUp(self):
        """ Create test records to use """
        self.genre = Genre.objects.create(
                genre="test",
                friendly_name="Test"
            )
        self.vinyl = Vinyl.objects.create(
            title="Test Vinyl",
            artist="bla",
            release_year="1950",
            price="12.99",
            description="testing testing",
            track_list="test, test,test",
            stock_quantity=5,
            genre=self.genre
        )
        self.image = Image.objects.create(
            vinyl=self.vinyl,
            image="test.png",
            image_name="Test Image"
        )

    def test_genre_string(self):
        """ Test Genre string method """
        self.assertEqual(str(self.genre), "test")

    def test_genre_friendly(self):
        """ Test Genre friendly_name string method """
        self.assertEqual(str(self.genre.friendly_name), "Test")

    def test_vinyl_string(self):
        """ Test Vinyl string method """
        self.assertEqual(str(self.vinyl), "Test Vinyl")

    def test_image_string(self):
        """ Test Image string method """
        self.assertEqual(str(self.image), "Test Image")
