from django.urls import path

from .views import DataDocView, CreateDocsView, DownloadDocView

urlpatterns = [
    path("filemake/", CreateDocsView.as_view(), name="file"),
    path("downloadfile/", DownloadDocView.as_view(), name="downloadfile"),
    path("data/", DataDocView.as_view(), name="data"),
]
