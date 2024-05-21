from django.urls import path

from . import views

urlpatterns = [
    path("filemake/", views.create_docs, name="file"),
]
