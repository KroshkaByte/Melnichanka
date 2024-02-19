from django.urls import path

from . import views

urlpatterns = [
    path("", views.goods_home_view, name="goods_home"),
    path("add/", views.goods_add_view, name="goods_add"),
    path("edit/", views.goods_edit_view, name="goods_edit"),
]
