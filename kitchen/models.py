from django.conf import settings
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    dish_type = models.ForeignKey(
        DishType, on_delete=models.CASCADE, related_name="dishes"
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="dishes", blank=True
    )
    ingredients = models.ManyToManyField(
        Ingredient, related_name="dishes", blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("kitchen:dish-detail", kwargs={"pk": self.pk})
