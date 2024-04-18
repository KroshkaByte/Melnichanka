from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("filemake_auto/", views.write_to_excel_auto, name="file"),
    path("filemake_rw/", views.write_to_excel_rw, name="file"),
]
