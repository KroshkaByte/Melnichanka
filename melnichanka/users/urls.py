from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import PositionListView, UserViewSet, RegisterView, DepartmentListView


router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/departments/", DepartmentListView.as_view(), name="departments"),
    path("api/positions/", PositionListView.as_view(), name="positions"),
    path("api/register", RegisterView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
