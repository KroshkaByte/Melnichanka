from django.urls import include, path
from rest_framework import routers

from .views import (
    CityViewSet,
    RailwayStationViewSet,
    TripAutoViewSet,
    TripRailwayViewSet,
)

router = routers.SimpleRouter()
router.register(r"city", CityViewSet)
router.register(r"autotrip", TripAutoViewSet)
router.register(r"stations", RailwayStationViewSet)
router.register(r"rwtrip", TripRailwayViewSet)

urlpatterns = [path("", include(router.urls))]
