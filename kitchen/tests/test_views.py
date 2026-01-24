from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, DishType, Dish


class PublicViewsTests(TestCase):
    def test_redirect_if_not_logged_in(self):
        url = reverse("kitchen:dish-list")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("/accounts/login/", response.url)


class PrivateViewsTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="user1",
            password="testpass123",
            years_of_experience=1,
        )
        self.client.login(username="user1", password="testpass123")

    def test_dashboard_page(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)

    def test_dish_type_list_page(self):
        response = self.client.get(reverse("kitchen:dishtype-list"))
        self.assertEqual(response.status_code, 200)

    def test_dish_list_page(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)

    def test_dish_detail_page(self):
        dish_type = DishType.objects.create(name="Soup")
        dish = Dish.objects.create(
            name="Chicken soup",
            description="desc",
            price="7.50",
            dish_type=dish_type,
        )
        response = self.client.get(reverse("kitchen:dish-detail", args=[dish.id]))
        self.assertEqual(response.status_code, 200)
