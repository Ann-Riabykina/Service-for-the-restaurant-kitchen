from django.urls import path

from .views import (
    IndexView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)

app_name = "kitchen"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    # Dish types
    path("dish-types/", DishTypeListView.as_view(),
         name="dishtype-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(),
         name="dishtype-create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(),
         name="dishtype-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(),
         name="dishtype-delete"),

    # Dishes
    path("dishes/", DishListView.as_view(),
         name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(),
         name="dish-create"),
    path("dishes/<int:pk>/", DishDetailView.as_view(),
         name="dish-detail"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(),
         name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(),
         name="dish-delete"),

    # Ingredients
    path("ingredients/", IngredientListView.as_view(),
         name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(),
         name="ingredient-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(),
         name="ingredient-update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(),
         name="ingredient-delete"),
]
