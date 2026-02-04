from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    SearchForm,
    DishForm,
    DishTypeForm,
    IngredientForm,
)
from .models import (
    Dish,
    DishType,
    Ingredient,
)


class QueryStringMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        params = self.request.GET.copy()
        params.pop("page", None)
        context["querystring"] = params.urlencode()
        return context


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "kitchen/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        context["num_cooks"] = User.objects.count()
        context["num_dishes"] = Dish.objects.count()
        context["num_dish_types"] = DishType.objects.count()
        return context


class DishTypeListView(LoginRequiredMixin, QueryStringMixin, generic.ListView):
    model = DishType
    paginate_by = 10
    template_name = "kitchen/dishtype_list.html"
    context_object_name = "dishtype_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search", "")
        context["form"] = SearchForm(initial={"search": context["search"]})
        return context


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen:dishtype-list")
    template_name = "kitchen/form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen:dishtype-list")
    template_name = "kitchen/form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dishtype-list")
    template_name = "kitchen/confirm_delete.html"


class DishListView(LoginRequiredMixin, QueryStringMixin, generic.ListView):
    model = Dish
    paginate_by = 10
    template_name = "kitchen/dish_list.html"
    queryset = (Dish.objects.select_related("dish_type").
                prefetch_related("cooks", "ingredients"))

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        dish_type_id = self.request.GET.get("dish_type")
        cook_id = self.request.GET.get("cook")
        if search:
            queryset = queryset.filter(name__icontains=search)
        if dish_type_id:
            queryset = queryset.filter(dish_type_id=dish_type_id)
        if cook_id:
            queryset = queryset.filter(cooks__id=cook_id)
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search", "")
        dish_type_raw = self.request.GET.get("dish_type")
        cook_raw = self.request.GET.get("cook")
        context["dish_type_id"] = int(
            dish_type_raw) if dish_type_raw and dish_type_raw.isdigit() else None
        context["cook_id"] = int(
            cook_raw) if cook_raw and cook_raw.isdigit() else None
        context["form"] = SearchForm(initial={"search": context["search"]})
        context["dish_types"] = DishType.objects.all()
        context["cooks"] = get_user_model().objects.all()
        return context


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type").prefetch_related("cooks", "ingredients")
    template_name = "kitchen/dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/form.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/confirm_delete.html"
    
    
class IngredientListView(LoginRequiredMixin, QueryStringMixin, generic.ListView):
    model = Ingredient
    paginate_by = 10
    template_name = "kitchen/ingredient_list.html"
    context_object_name = "ingredient_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search", "")
        context["form"] = SearchForm(initial={"search": context["search"]})
        return context


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/form.html"


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/form.html"


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/confirm_delete.html"
