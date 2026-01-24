from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Cook, Dish, DishType, Ingredient


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
        queryset=Cook.objects.all(),
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


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "email", "years_of_experience"]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]
