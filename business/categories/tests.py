from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Category

User = get_user_model()


class CategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@gmail.com", first_name="test",
                                             password="testpassword")

    def test_category_creation(self):
        category = Category.objects.create(user=self.user, title="Test Category", description="Description")

        self.assertEqual(category.title, "Test Category")
        self.assertEqual(category.description, "Description")
        self.assertEqual(category.user, self.user)

    def test_categories_list_view(self):
        Category.objects.create(user=self.user, title="Test Category", description="Description")

        self.client.force_login(self.user)
        response = self.client.get(reverse("categories:all_categories"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")

    def test_categories_detail_view(self):
        category = Category.objects.create(user=self.user, title="Test Category", description="Test_desc")
        category.delete()
        self.client.force_login(self.user)
        response = self.client.get(reverse("categories:all_categories"))
        self.assertNotContains(response, "Test Category")

    def test_redirect_for_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse("categories:all_categories"))
        self.assertRedirects(response, f"{reverse('login')}?next=/categories/")
