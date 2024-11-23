from django.contrib.auth import get_user_model
from django.test import TestCase

from categories.models import Category
from django.urls import reverse

from .models import Product

User = get_user_model()


class ProductCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@gmail.com", first_name="test",
                                             password="testpassword")
        self.client.force_login(self.user)

    def test_products(self):
        category = Category.objects.create(user=self.user, title="Test Category", description="Description")
        product = Product.objects.create(user=self.user, title="testtitle", description="test_desc",
                                         selling_price=100, amount=10, category=category)

        self.assertEqual(product.title, "testtitle")
        self.assertEqual(product.description, "test_desc")
        self.assertEqual(product.selling_price, 100)
        self.assertEqual(product.amount, 10)
        self.assertEqual(product.category, category)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Category.objects.count(), 1)

        response = self.client.get(reverse('products:all_products', args=[category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testtitle")
