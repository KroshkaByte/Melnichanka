from django.urls import path

from . import views

urlpatterns = [
    path("", views.clients_home_view, name="clients_home"),
    path("add/", views.clients_add_view, name="clients_add"),
    path("edit/<int:pk>/", views.clients_edit_view, name="clients_edit"),
    path("delete/<int:pk>/", views.clients_delete_view, name="clients_delete"),
]
