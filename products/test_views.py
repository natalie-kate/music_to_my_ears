""" Import TestCase Vinyl and Genre to test our views """
from django.test import TestCase
from .models import Vinyl, Genre


class TestViews(TestCase):
    """ Test product views """

    def setUp(self):
        """ Create test records to use """
        self.genre = Genre.objects.create(
                genre="test",
                friendly_name="Test"
            )
        self.vinyl = Vinyl.objects.create(
            title="Test",
            artist="bla",
            release_year="1950",
            price="12.99",
            description="testing testing",
            track_list="test, test,test",
            stock_quantity=5,
            genre=self.genre
        )

    def test_shop_view(self):
        """ Test shop.html rendered properly """
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/shop.html')

    def test_product_view(self):
        """ Test product.html rendered properly """
        response = self.client.get(f'/{ self.vinyl.id }/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product.html')
