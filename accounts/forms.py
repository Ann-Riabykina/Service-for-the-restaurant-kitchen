from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Cook


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
