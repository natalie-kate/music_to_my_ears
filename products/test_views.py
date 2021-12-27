""" Import TestCase to use to test our views """
from django.test import TestCase
from .models import Vinyl, Genre


class TestViews(TestCase):
    """ Test product views """
    def test_shop_view(self):
        """ Test shop.html rendered properly """
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/shop.html')

    def test_product_view(self):
        """ Test product.html rendered properly """

        test_genre = Genre.objects.create(
            genre="test",
            friendly_name="Test"
        )
        test_vinyl = Vinyl.objects.create(
            title="Test",
            artist="bla",
            release_year="1950",
            price="12.99",
            description="testing testing",
            track_list="test, test,test",
            stock_quantity=5,
            genre=test_genre
        )
        response = self.client.get(f'/{test_vinyl.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product.html')

        