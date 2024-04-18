from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import City, RailwayStation, TripAuto, TripRailway
from .serializers import (
    CitySerializer,
    RailwayStationSerializer,
    TripAutoSerializer,
    TripRailwaySerializer,
)


class CityViewSet(viewsets.ModelViewSet[City]):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)


class TripAutoViewSet(viewsets.ModelViewSet[TripAuto]):
    queryset = TripAuto.objects.all()
    serializer_class = TripAutoSerializer
    permission_classes = (IsAuthenticated,)


class RailwayStationViewSet(viewsets.ModelViewSet[RailwayStation]):
    queryset = RailwayStation.objects.all()
    serializer_class = RailwayStationSerializer
    permission_classes = (IsAuthenticated,)


class TripRailwayViewSet(viewsets.ModelViewSet[TripRailway]):
    queryset = TripRailway.objects.all()
    serializer_class = TripRailwaySerializer
    permission_classes = (IsAuthenticated,)
