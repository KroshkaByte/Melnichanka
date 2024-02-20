from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    # path(
    #     "api/signup/",
    #     views.MyUserListCreateViewSet.as_view({"get": "list", "post": "create"}),
    # ),
    # path(
    #     "api/signup/<int:pk>/",
    #     views.MyUserRetrieveUpdateDestroyViewSet.as_view(
    #         {"get": "retrieve", "put": "update", "delete": "destroy"}
    #     ),
    #     name="user-detail",
    # ),
]


# urlpatterns = format_suffix_patterns(urlpatterns)
