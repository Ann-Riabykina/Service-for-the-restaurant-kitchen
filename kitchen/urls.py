from django.urls import path

from .views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
)

app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),

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

    # Cooks
    path("cooks/", CookListView.as_view(), 
         name="cook-list"),
    path("cooks/create/", CookCreateView.as_view(), 
         name="cook-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), 
         name="cook-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), 
         name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), 
         name="cook-delete"),
]
