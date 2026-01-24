from django.test import TestCase

from kitchen.models import Cook, DishType, Dish, Ingredient


class ModelTests(TestCase):
    def test_dishtype_str(self):
        dish_type = DishType.objects.create(name="Soup")
        self.assertEqual(str(dish_type), "Soup")

    def test_ingredient_str(self):
        ing = Ingredient.objects.create(name="Tomato")
        self.assertEqual(str(ing), "Tomato")

    def test_cook_str(self):
        cook = Cook.objects.create_user(
            username="anna",
            password="testpass123",
            first_name="Anna",
            last_name="Smith",
            years_of_experience=3,
        )
        self.assertIn("anna", str(cook))

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Dessert")
        dish = Dish.objects.create(
            name="Pancakes",
            description="Tasty pancakes",
            price="5.00",
            dish_type=dish_type,
        )
        self.assertEqual(str(dish), "Pancakes")
