from django.urls import path

from . import views

urlpatterns = [
    path("", views.logistics_home_view, name="logistics_home"),
    path("auto/", views.auto_home_view, name="auto_home"),
    path("auto/add/", views.auto_add_view, name="auto_add"),
    path("auto/edit/", views.auto_edit_view, name="auto_edit"),
    path("auto/del/", views.auto_delete_view, name="auto_del"),
    path("auto/req/add/", views.auto_add_requisites_view, name="auto_add_requisites"),
    path(
        "auto/req/edit/", views.auto_edit_requisites_view, name="auto_edit_requisites"
    ),
    path(
        "auto/req/del/", views.auto_delete_requisites_view, name="auto_del_requisites"
    ),
    path("rw/", views.rw_home_view, name="rw_home"),
    path("rw/add/", views.rw_add_view, name="rw_add"),
    path("rw/edit/", views.rw_edit_view, name="rw_edit"),
    path("rw/del/", views.rw_delete_view, name="rw_del"),
    path("rw/req/add/", views.rw_add_requisites_view, name="rw_add_requisites"),
    path("rw/req/edit/", views.rw_edit_requisites_view, name="rw_edit_requisites"),
    path("rw/req/del/", views.rw_delete_requisites_view, name="rw_del_requisites"),
]