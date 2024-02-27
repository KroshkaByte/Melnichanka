from django.urls import include, path
from rest_framework import routers

from .views import ClientsViewSet

router = routers.SimpleRouter()
router.register(r"clients", ClientsViewSet, basename="clients")


urlpatterns = [
    path("", include(router.urls)),
]
