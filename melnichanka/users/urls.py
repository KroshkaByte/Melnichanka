from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import (DepartmentListView, PositionListView, UserCreateView,
                    UserUpdateView)

urlpatterns = [
    path("edit/<int:pk>/", UserUpdateView.as_view(), name="edit"),
    path("departments/", DepartmentListView.as_view(), name="departments"),
    path("positions/", PositionListView.as_view(), name="positions"),
    path("registration/", UserCreateView.as_view(), name="registration"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
