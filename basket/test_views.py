""" Import TestCase to use to test our views """
from django.test import TestCase
from django.shortcuts import reverse
from products.models import Genre, Vinyl


class TestViews(TestCase):
    """ Test basket views """
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
        self.basket = {
            f'{self.vinyl.id}': "2",
        }

    def test_basket_view(self):
        """ Test basket.html rendered properly """
        response = self.client.get('/basket/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_url_accessible_by_name(self):
        """ Test basket link """
        response = self.client.get(reverse('view_basket'))
        self.assertEqual(response.status_code, 200)
