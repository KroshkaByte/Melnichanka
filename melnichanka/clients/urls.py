from django.urls import path

from . import views

urlpatterns = [
    path("", views.clients_home_view, name="clients_home"),
    path("clients_add/", views.clients_add_view, name="clients_add"),
]
