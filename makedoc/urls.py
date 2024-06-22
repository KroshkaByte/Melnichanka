from django.urls import path

from .views import DataDocAPIView, CreateDocsAPIView, DownloadDocAPIView

urlpatterns = [
    path("filemake/", CreateDocsAPIView.as_view(), name="file"),
    path("downloadfile/", DownloadDocAPIView.as_view(), name="downloadfile"),
    path("data/", DataDocAPIView.as_view(), name="data"),
]
