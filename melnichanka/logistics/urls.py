from django.urls import path

from . import views

urlpatterns = [
    path("", views.logistics_home_view, name="logistics_home"),
    path("log_add/", views.logistics_add_view, name="logistics_add"),
    path("log_edit/", views.logistics_edit_view, name="logistics_edit"),
    path("log_del/", views.logistics_delete_view, name="logistics_del"),
]
