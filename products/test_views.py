""" Import TestCase Vinyl and Genre to test our views """
from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import Vinyl, Genre, Image


class TestViews(TestCase):
    """ Test product views """

    def setUp(self):
        """ Create test records to use """
        self.admin_user = User.objects.create(
            username="tess",
            password="test1abc",
            is_superuser=True
        )
        self.client.force_login(self.admin_user)

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
            genre=self.genre,
        )

        self.default_image = Image.objects.create(
            vinyl=self.vinyl,
            image="default_image.png",
            image_name="default image",
            default=True
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

    def test_search(self):
        """ Test search redirect and message if no match """
        response = self.client.get('/shop/shop/', {
            'search': "Nope"
             })
        error_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(error_messages), 1)
        self.assertEqual(
            str(error_messages[0]),
            "Sorry your query didn't match any of our products")
        self.assertRedirects(response, reverse('shop'))

    def test_search_not_empty(self):
        """ Test search redirect and message if empty """
        response = self.client.get('/shop/shop/', {
            'search': ""
             })
        error_messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(error_messages), 1)
        self.assertEqual(
            str(error_messages[0]),
            "Oops you need to enter a search keyword first")
        self.assertRedirects(response, reverse('shop'))
