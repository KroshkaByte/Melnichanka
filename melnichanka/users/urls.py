from django.urls import include, path

from .views import (DepartmentListView, PositionListView, UserCreateView,
                    UserUpdatePasswordView, UserUpdateView, login_view,
                    logout_view, session_view, whoami_view)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("session/", session_view, name="session"),
    path("whoami/", whoami_view, name="whoami"),
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
