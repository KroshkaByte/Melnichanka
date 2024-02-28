from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import City, RailwayStations, TripsAuto, TripsRailway
from .serializers import (CitySerializer, RailwayStationsSerializer,
                          TripsAutoSerializer, TripsRailwaySerializer)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)


class TripsAutoViewSet(viewsets.ModelViewSet):
    queryset = TripsAuto.objects.all()
    serializer_class = TripsAutoSerializer
    permission_classes = (IsAuthenticated,)


class RailwayStationsViewSet(viewsets.ModelViewSet):
    queryset = RailwayStations.objects.all()
    serializer_class = RailwayStationsSerializer
    permission_classes = (IsAuthenticated,)


class TripsRailwayViewSet(viewsets.ModelViewSet):
    queryset = TripsRailway.objects.all()
    serializer_class = TripsRailwaySerializer
    permission_classes = (IsAuthenticated,)
