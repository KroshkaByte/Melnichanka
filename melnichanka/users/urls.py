from django.urls import include, path

from .views import (
    DepartmentListView,
    PositionListView,
    SessionView,
    UserCreateView,
    UserUpdatePasswordView,
    UserUpdateView,
    WhoAmIView,
    get_csrf,
    login_view,
    logout_view

)

urlpatterns = [
    path('csrf/', get_csrf, name='api-csrf'),
    path('login/', login_view, name='api-login'),
    path('logout/', logout_view, name='api-logout'),
    path('session/', SessionView.as_view(), name='api-session'),
    path('whoami/', WhoAmIView.as_view(), name='api-whoami'),
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
