from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CookCreationForm, CookUpdateForm


class SignUpView(generic.CreateView):
    model = get_user_model()
    form_class = CookCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    paginate_by = 10
    template_name = "accounts/cook_list.html"
    context_object_name = "cook_list"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = "accounts/cook_detail.html"


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = CookUpdateForm
    template_name = "kitchen/form.html"
    success_url = reverse_lazy("accounts:cook-list")
