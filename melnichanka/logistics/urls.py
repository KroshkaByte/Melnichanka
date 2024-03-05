from django.urls import include, path
from rest_framework import routers

from .views import (
    CityViewSet,
    RailwayStationsViewSet,
    TripsAutoViewSet,
    TripsRailwayViewSet,
)

router = routers.SimpleRouter()
router.register(r"city", CityViewSet)
router.register(r"autotrip", TripsAutoViewSet)
router.register(r"stations", RailwayStationsViewSet)
router.register(r"rwtrip", TripsRailwayViewSet)

urlpatterns = [path("", include(router.urls))]
