""" Import TestCase to use to test our views """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.contrib.messages import get_messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Genre, Vinyl, Image


class TestViews(TestCase):
    """ Test profile views """
    def setUp(self):
        """ Create test records to use """
        self.user = User.objects.create(
            username="tess",
            password="test1abc"
            )

        self.genre = Genre.objects.create(
            genre="test_genre",
            friendly_name="Test Genre"
        )

        self.product = Vinyl.objects.create(
            genre=self.genre,
            title="Test Vinyl",
            artist="Tester",
            price=12.99,
            stock_quantity=4,
            track_list="1. T, 2. Te, 3. Tes, 4.Test"
        )

        self.image = Image.objects.create(
            vinyl = self.product,
            image = "product.png",
            image_name = "product",
            default = True
        )

        self.order = Order.objects.create(
            first_name="Tess",
            surname="Tester",
            email="tess@test.com",
            phone_number="0123456789",
            street_address1="29 Test Street",
            town_or_city="Testwick",
            country="Test"
            )

        self.lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

        self.client.force_login(self.user)

    def test_profile_view(self):
        """ Test profile.html rendered properly """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_url_accessible_by_name(self):
        """ Test profile link """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_order_history_view(self):
        """ Test correct template used for order history rendered properly """
        response = self.client.get(f'/profile/order_history/{self.order.order_number}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
