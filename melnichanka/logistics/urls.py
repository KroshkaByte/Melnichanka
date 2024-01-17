from django.urls import path

from . import views

urlpatterns = [
    path("", views.logistics_home_view, name="logistics_home"),
    path("log_add/", views.logistics_add_view, name="logistics_add"),
]
