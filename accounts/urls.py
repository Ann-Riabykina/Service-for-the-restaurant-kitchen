from django.urls import path
from .views import SignUpView, CookListView, CookDetailView, CookUpdateView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
]
