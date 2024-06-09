from django.urls import include, path
from rest_framework import routers

from .views import (
    CityViewSet,
    RailwayStationViewSet,
    TripAutoViewSet,
    TripRailwayViewSet,
    FactoryListAPIView,
)

router = routers.SimpleRouter()
router.register(r"city", CityViewSet)
router.register(r"auto", TripAutoViewSet)
router.register(r"stations", RailwayStationViewSet)
router.register(r"rw", TripRailwayViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("factories/", FactoryListAPIView.as_view(), name="factory-list"),
]
