from django.urls import resolve
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import (
    LoginView,
    LogoutView,
    UserCreateView,
    UserUpdatePasswordView,
    UserUpdateView,
)


def test__url_resolves_to_correct_view():
    match = resolve("/api/v1/users/login/")
    assert match.func.view_class == LoginView
    match = resolve("/api/v1/users/token/refresh/")
    assert match.func.view_class == TokenRefreshView
    match = resolve("/api/v1/users/logout/")
    assert match.func.view_class == LogoutView
    match = resolve("/api/v1/users/edit/")
    assert match.func.view_class == UserUpdateView
    match = resolve("/api/v1/users/edit_password/")
    assert match.func.view_class == UserUpdatePasswordView
    match = resolve("/api/v1/users/registration/")
    assert match.func.view_class == UserCreateView
