""" Import TestCase Vinyl and Genre to test our views """
from django.test import TestCase
from django.urls import reverse
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
        response = self.client.get('/shop/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/shop.html')

    def test_shop_url_accessible_by_name(self):
        """ Test shop link """
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)

    def test_product_view(self):
        """ Test product.html rendered properly """
        response = self.client.get(f'/shop/{ self.vinyl.id }/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product.html')

    def test_product_url_accessible_by_name(self):
        """ Test shop link """
        response = self.client.get(reverse('product', args=[self.vinyl.id]))
        self.assertEqual(response.status_code, 200)
