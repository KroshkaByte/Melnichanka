from django.urls import path, include
from .views import PositionListView, UserUpdateView, UserCreateView, DepartmentListView


urlpatterns = [
    path("edit/<int:pk>/", UserUpdateView.as_view(), name="edit"),
    path("departments/", DepartmentListView.as_view(), name="departments"),
    path("positions/", PositionListView.as_view(), name="positions"),
    path("registration/", UserCreateView.as_view(), name="registration"),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
