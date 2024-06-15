from django.urls import path

from .views import DataDocView, CreateDocsView

urlpatterns = [
    path("filemake/", CreateDocsView.as_view(), name="file"),
    path("data/", DataDocView.as_view(), name="data"),
]
