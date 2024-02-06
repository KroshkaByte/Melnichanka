from django.urls import path

from . import views

urlpatterns = [
    path("", views.logistics_home_view, name="logistics_home"),
    path("auto/", views.auto_home_view, name="auto_home"),
    path("auto/add/", views.auto_add_view, name="auto_add"),
    path("auto/edit/", views.auto_edit_view, name="auto_edit"),
    path("auto/del/", views.auto_delete_view, name="auto_del"),
    path("rw/", views.rw_home_view, name="rw_home"),
    path("rw/add/", views.rw_add_view, name="rw_add"),
    path("rw/edit_price/", views.rw_edit_price_view, name="rw_edit_price"),
    path(
        "rw/edit_requisites/", views.rw_edit_requisites_view, name="rw_edit_requisites"
    ),
    path("rw/del/", views.rw_delete_view, name="rw_del"),
]
