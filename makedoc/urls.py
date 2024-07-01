from django.urls import path

from .views import DataDocAPIView, CreateDocsAPIView, DownloadDocAPIView, SendArchiveAPIView

urlpatterns = [
    path("file-make/", CreateDocsAPIView.as_view(), name="file-make"),
    path("download-file/", DownloadDocAPIView.as_view(), name="download-file"),
    path("data/", DataDocAPIView.as_view(), name="data"),
    path("send-archive/", SendArchiveAPIView.as_view(), name="send-archive"),
]
