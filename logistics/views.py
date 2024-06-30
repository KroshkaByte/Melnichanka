from django.core.cache import cache
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import City, RailwayStation, TripAuto, TripRailway, Factory
from .serializers import (
    CitySerializer,
    RailwayStationSerializer,
    TripAutoSerializer,
    TripRailwaySerializer,
    FactorySerializer,
)


class CityViewSet(viewsets.ModelViewSet[City]):
    """
    A viewset for handling CRUD operations on City objects.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)


class TripAutoViewSet(viewsets.ModelViewSet[TripAuto]):
    """
    A viewset for handling CRUD operations on TripAuto objects.
    """

    queryset = TripAuto.objects.all()
    serializer_class = TripAutoSerializer
    permission_classes = (IsAuthenticated,)


class RailwayStationViewSet(viewsets.ModelViewSet[RailwayStation]):
    """
    A viewset for handling CRUD operations on RailwayStation objects.
    """

    queryset = RailwayStation.objects.all()
    serializer_class = RailwayStationSerializer
    permission_classes = (IsAuthenticated,)


class TripRailwayViewSet(viewsets.ModelViewSet[TripRailway]):
    """
    A viewset for handling CRUD operations on TripRailway objects.
    """

    queryset = TripRailway.objects.all()
    serializer_class = TripRailwaySerializer
    permission_classes = (IsAuthenticated,)


class FactoryListAPIView(generics.ListAPIView[Factory]):
    """
    A view for listing factories, with caching implemented.
    """

    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Overrides the queryset retrieval to implement caching.
        """
        cached_factories = cache.get("factories_list")
        if cached_factories:
            return cached_factories
        else:
            factories = super().get_queryset()
            cache.set("factories_list", factories, 3600)
            return factories
