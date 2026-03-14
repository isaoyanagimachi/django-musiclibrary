from django.test import TestCase
from .models import Category, MenuItem, Order, OrderItem


class OrderModelTests(TestCase):
    def test_total_amount_calculates_correctly(self):
        cat = Category.objects.create(name="Pizza")
        item = MenuItem.objects.create(
            category=cat, name="Margherita", price=200, is_available=True
        )
        order = Order.objects.create(
            customer_name="Test User", customer_phone="12345"
        )
        OrderItem.objects.create(order=order, menu_item=item, quantity=2)

        self.assertEqual(order.total_amount, 400)