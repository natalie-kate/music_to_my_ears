""" Imports to test our checkout models """
from django.test import TestCase
from products.models import Genre, Vinyl
from .models import Order, OrderLineItem


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
            title="Test Vinyl",
            artist="Tester",
            price=12.99,
            stock_quantity=4,
            track_list="1. T, 2. Te, 3. Tes, 4.Test"
        )

        self.product1 = Vinyl.objects.create(
            genre=self.genre,
            title="Vinyl",
            artist="Test Artist",
            price=8.99,
            stock_quantity=2,
            track_list="1. T, 2. Te, 3. Tes, 4.Test"
        )

        self.product2 = Vinyl.objects.create(
            genre=self.genre,
            title="Product Vinyl",
            artist="Artist",
            price=10.99,
            stock_quantity=7,
            track_list="1. T, 2. Te, 3. Tes, 4.Test"
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

        self.lineitem1 = OrderLineItem.objects.create(
            order=self.order,
            product=self.product1,
            quantity=2
        )

        self.lineitem2 = OrderLineItem.objects.create(
            order=self.order,
            product=self.product2,
            quantity=3
        )

    def test_order_number_created(self):
        """ Check Order Number Generated """
        self.assertTrue(self.order.order_number)

    def test_grand_total_calculated(self):
        """ Check Grand Total Calculated """
        self.assertEqual(str(round(self.order.grand_total, 2)), '71.39')

    def test_order_string(self):
        """ Check order str method """
        self.assertEqual(str(self.order), str(self.order.order_number))

    def test_lineitem_total(self):
        """ Check Order Number Generated """
        self.assertTrue(self.lineitem.lineitem_total)
        self.assertEqual(round(self.lineitem.lineitem_total, 2), 12.99)

    def test_lineitem_str(self):
        """ Check lineitem str method """
        self.assertEqual(
            str(self.lineitem),
            f"Test Vinyl on order {self.order.order_number}")
