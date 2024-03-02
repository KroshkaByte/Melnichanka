from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    DepartmentListView,
    PositionListView,
    UserCreateView,
    UserUpdatePasswordView,
    UserUpdateView,
)

urlpatterns = [
    path('token/',
          jwt_views.TokenObtainPairView.as_view(),
          name ='token_obtain_pair'),
    path('token/refresh/',
          jwt_views.TokenRefreshView.as_view(),
          name ='token_refresh'),
    path("edit/", UserUpdateView.as_view(), name="edit"),
    path("edit_password/", UserUpdatePasswordView.as_view(), name="edit_password"),
    path("departments/", DepartmentListView.as_view(), name="departments"),
    path("positions/", PositionListView.as_view(), name="positions"),
    path("registration/", UserCreateView.as_view(), name="registration"),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
