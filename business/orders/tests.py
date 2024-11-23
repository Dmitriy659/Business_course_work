from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Order

User = get_user_model()


class OrderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@gmail.com", first_name="test",
                                             password="testpassword")

    def test_order_creation(self):
        order = Order.objects.create(user=self.user, buyer="Test buyer")
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.buyer, "Test buyer")


class OrderViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@gmail.com", first_name="test",
                                             password="testpassword")
        self.client.force_login(self.user)
        self.order = Order.objects.create(user=self.user, buyer="Test buyer")

    def test_order_view(self):
        resposne = self.client.get(reverse('orders:all_orders'))
        self.assertEqual(resposne.status_code, 200)
        self.assertContains(resposne, "Test buyer")

    def test_redirect_for_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse('orders:all_orders'))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('orders:all_orders')}")
