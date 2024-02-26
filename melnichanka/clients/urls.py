from rest_framework import routers
from django.urls import path, include


from .views import ClientsViewSet

router = routers.SimpleRouter()
router.register(r"clients", ClientsViewSet, basename="clients")


urlpatterns = [
    path("", include(router.urls)),
]
