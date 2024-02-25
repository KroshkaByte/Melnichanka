from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import PositionListView, UserUpdateView, UserCreateView, DepartmentListView


urlpatterns = [
    path("api/edit/<int:pk>/", UserUpdateView.as_view(), name="edit"),
    path("api/departments/", DepartmentListView.as_view(), name="departments"),
    path("api/positions/", PositionListView.as_view(), name="positions"),
    path("api/registration/", UserCreateView.as_view(), name="registration"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
