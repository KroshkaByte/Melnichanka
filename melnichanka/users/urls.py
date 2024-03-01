from django.urls import include, path

from .views import (
    DepartmentListView,
    PositionListView,
    UserCreateView,
    UserUpdatePasswordView,
    UserUpdateView,
    LoginView,
    LogoutView,
    SessionView,
    WhoAmIView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("session/", SessionView.as_view(), name="session"),
    path("whoami/", WhoAmIView.as_view(), name="whoami"),
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
