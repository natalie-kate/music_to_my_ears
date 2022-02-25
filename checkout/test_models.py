""" Imports to test our checkout models """
from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Genre, Vinyl, Image


class TestOrderModels(TestCase):
    """ Test order models """
    def setUp(self):
        """ Create test records to use """
        self.genre = Genre.objects.create(
            genre="test_genre",
            friendly_name="Test Genre"
        )

        self.product = Vinyl.objects.create(
            genre=self.genre,
            title=
            artist=
            price=
            stock_quantity=
            track_list=
        )

        self.product1 = Vinyl.objects.create(
            
        )

        self.product2 = Vinyl.objects.create(
            
        )

        self.image = Image.objects.create(
            default=True,
            vinyl=self.vinyl,
            image_name="image.png"
        )

        self.order = Order.objects.create(
            order_number =
            user_profile = 
            first_name = 
            surname =
            email = 
            phone_number = 
            street_address1 = 
            town_or_city = 
            country = 
            )

        self.lineitem = OrderLineItem.create(
            order = 
            product = 
            quantity = 
            lineitem_total = 
        )

        self.lineitem1 = OrderLineItem.create(
            order = 
            product = 
            quantity = 
            lineitem_total = 
        )

        self.lineitem2 = OrderLineItem.create(
            order = 
            product = 
            quantity = 
            lineitem_total = 
        )

