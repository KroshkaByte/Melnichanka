from django.urls import path

from . import views

urlpatterns = [
    path("", views.goods_home_view, name="goods_home"),
    path("add/", views.goods_add_view, name="goods_add"),
    path("edit/<int:pk>", views.goods_edit_view, name="goods_edit"),
    path("del/<int:pk>", views.goods_delete_view, name="goods_delete"),
]
