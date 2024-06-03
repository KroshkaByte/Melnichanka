from django.urls import path

from . import views
from .views import DataDocView

urlpatterns = [
    path("filemake/", views.create_docs, name="file"),
    path("data/", DataDocView.as_view(), name="data"),
]
