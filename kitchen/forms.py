from django import forms
from django.contrib.auth.forms import get_user_model

from .models import Dish, DishType, Ingredient


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search...", "class": "form-control"}
        ),
    )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]
