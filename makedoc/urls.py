from django.urls import path

from .views import DataDocView, CreateDocsView, DownloadDocView

urlpatterns = [
    path("filemake/", CreateDocsView.as_view(), name="file"),
    path("downloadxls/", DownloadDocView.as_view(), name="downloadxls"),
    path("data/", DataDocView.as_view(), name="data"),
]
