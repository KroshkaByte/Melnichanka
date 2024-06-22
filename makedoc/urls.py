from django.urls import path

from .views import DataDocView, CreateDocsView, DownloadDocAPIView

urlpatterns = [
    path("filemake/", CreateDocsView.as_view(), name="file"),
    path("downloadfile/", DownloadDocAPIView.as_view(), name="downloadfile"),
    path("data/", DataDocView.as_view(), name="data"),
]
