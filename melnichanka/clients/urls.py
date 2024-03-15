from django.urls import path

from .views import (
    ClientAPIDeleteView,
    ClientAPIUpdateView,
    ClientsAPIView,
)


urlpatterns = [
    path("", ClientsAPIView.as_view(), name="clients"),
    path("<int:pk>/", ClientAPIUpdateView.as_view(), name="clients_update"),
    path("delete/<int:pk>/", ClientAPIDeleteView.as_view(), name="clients_delete"),
]
